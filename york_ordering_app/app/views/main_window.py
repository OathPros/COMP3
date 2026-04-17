from __future__ import annotations

from pathlib import Path

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, Gdk, Gtk

from ..cart import Cart
from ..data_loader import Catalog
from ..email_utils import build_body, build_mailto
from ..models import CheckoutState, Order, Product, SetupPackage


class ProductCard(Gtk.Button):
    def __init__(self, product: Product, on_open):
        super().__init__(css_classes=["card"], halign=Gtk.Align.FILL, valign=Gtk.Align.FILL)
        self.product = product
        self.set_hexpand(True)
        self.connect("clicked", lambda *_: on_open(self.product))

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, margin_top=10, margin_bottom=10, margin_start=10, margin_end=10)
        self.set_child(box)

        picture = Gtk.Picture.new_for_filename(product.thumbnail)
        picture.set_content_fit(Gtk.ContentFit.COVER)
        picture.set_size_request(220, 110)
        picture.set_can_shrink(True)
        picture.set_alt_text(product.name)
        box.append(picture)

        title = Gtk.Label(label=product.name, xalign=0, wrap=True)
        title.add_css_class("heading")
        box.append(title)

        tag_row = Gtk.Box(spacing=4)
        for tag in product.tags[:2]:
            pill = Gtk.Label(label=tag)
            pill.add_css_class("pill")
            tag_row.append(pill)
        box.append(tag_row)

        desc = Gtk.Label(label=product.description, xalign=0, wrap=True)
        desc.add_css_class("dim-label")
        box.append(desc)

        price = Gtk.Label(label=f"${product.price:,.2f}", xalign=0)
        price.add_css_class("title-4")
        box.append(price)


class MainWindow(Adw.ApplicationWindow):
    def __init__(self, app: Adw.Application, catalog: Catalog):
        super().__init__(application=app, title="UIT Computer Ordering")
        self.catalog = catalog
        self.cart = Cart()
        self.checkout_state = CheckoutState()
        self.detail_navigation: Adw.NavigationView | None = None
        self.set_default_size(1200, 760)

        self.toast_overlay = Adw.ToastOverlay()
        self.set_content(self.toast_overlay)

        toolbar_view = Adw.ToolbarView()
        self.toast_overlay.set_child(toolbar_view)

        header = Adw.HeaderBar()
        toolbar_view.add_top_bar(header)

        self.cart_button = Gtk.Button(icon_name="shopping-cart-symbolic", visible=False, tooltip_text="Open order")
        self.cart_button.connect("clicked", self._open_cart_dialog)
        header.pack_end(self.cart_button)

        self.category_dropdown = Gtk.DropDown.new_from_strings(["All"] + self.catalog.categories)
        self.category_dropdown.connect("notify::selected", lambda *_: self._rebuild_product_grid())
        header.pack_start(self.category_dropdown)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
        toolbar_view.set_content(content)

        setup_title = Gtk.Label(label="Suggested setups", xalign=0)
        setup_title.add_css_class("title-3")
        content.append(setup_title)

        self.setup_flow = Gtk.FlowBox(max_children_per_line=3, min_children_per_line=1, selection_mode=Gtk.SelectionMode.NONE, row_spacing=8, column_spacing=8)
        content.append(self.setup_flow)
        self._build_setup_cards()

        product_title = Gtk.Label(label="Catalog", xalign=0)
        product_title.add_css_class("title-3")
        content.append(product_title)

        self.product_flow = Gtk.FlowBox(max_children_per_line=3, min_children_per_line=1, selection_mode=Gtk.SelectionMode.NONE, row_spacing=8, column_spacing=8, vexpand=True)
        scroller = Gtk.ScrolledWindow(vexpand=True, child=self.product_flow)
        content.append(scroller)
        self._rebuild_product_grid()

        css = Gtk.CssProvider()
        css.load_from_data(
            b"""
            .pill {background: alpha(#c41230, 0.12); color: #8b1021; border-radius: 999px; padding: 2px 8px;}
            .setup-card {min-height: 150px;}
            """
        )
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def _selected_category(self) -> str:
        selected = self.category_dropdown.get_selected_item()
        return selected.get_string() if selected else "All"

    def _rebuild_product_grid(self) -> None:
        while child := self.product_flow.get_first_child():
            self.product_flow.remove(child)

        category = self._selected_category()
        products = [
            product for product in self.catalog.products.values() if category == "All" or product.category == category
        ]

        for product in products:
            card = ProductCard(product, self._open_product_detail)
            self.product_flow.insert(card, -1)

    def _build_setup_cards(self) -> None:
        for setup in self.catalog.setups:
            button = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
            button.add_css_class("card")
            button.add_css_class("setup-card")

            title = Gtk.Label(label=setup.name, xalign=0)
            title.add_css_class("title-4")
            desc = Gtk.Label(label=setup.description, xalign=0)
            desc.add_css_class("dim-label")
            desc.set_wrap(True)

            action_row = Gtk.Box(spacing=6)
            add_button = Gtk.Button(label="Quick Add")
            add_button.connect("clicked", lambda _, s=setup: self._add_setup_to_cart(s))

            compare_button = Gtk.Button(label="View & Compare")
            compare_button.connect("clicked", lambda _, s=setup: self._open_setup_compare(s))

            action_row.append(add_button)
            action_row.append(compare_button)

            button.append(title)
            button.append(desc)
            button.append(action_row)

            self.setup_flow.insert(button, -1)

    def _open_product_detail(self, product: Product) -> None:
        dialog = Adw.Dialog(content_width=540, content_height=460)
        dialog.set_title(product.name)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
        picture = Gtk.Picture.new_for_filename(product.thumbnail)
        picture.set_content_fit(Gtk.ContentFit.COVER)
        picture.set_size_request(460, 180)
        picture.set_alt_text(product.name)
        content.append(picture)

        content.append(Gtk.Label(label=product.description, xalign=0, wrap=True))
        content.append(Gtk.Label(label=f"Price: ${product.price:,.2f}", xalign=0, css_classes=["title-4"]))

        specs = Gtk.ListBox(css_classes=["boxed-list"])
        for key, value in product.specs.items():
            row = Adw.ActionRow(title=key, subtitle=value)
            specs.append(row)
        content.append(specs)

        add_button = Gtk.Button(label="Add to Order", css_classes=["suggested-action"])
        add_button.connect("clicked", lambda *_: (self.cart.add(product), self._sync_cart_button(), dialog.force_close()))
        content.append(add_button)

        dialog.set_child(content)
        dialog.present(self)

    def _add_setup_to_cart(self, setup: SetupPackage) -> None:
        for product_id in setup.items:
            self.cart.add(self.catalog.products[product_id])
        self._sync_cart_button()
        self._toast(f"Added {setup.name}")

    def _open_setup_compare(self, setup: SetupPackage) -> None:
        dialog = Adw.Dialog(content_width=620, content_height=480, title=f"{setup.name} comparison")
        listbox = Gtk.ListBox(css_classes=["boxed-list"], selection_mode=Gtk.SelectionMode.NONE)

        for product_id in setup.items:
            product = self.catalog.products[product_id]
            row = Adw.ActionRow(title=product.name, subtitle=f"${product.price:,.2f} · {product.description}")
            open_button = Gtk.Button(label="Open")
            open_button.connect("clicked", lambda _, p=product: self._open_product_detail(p))
            row.add_suffix(open_button)
            listbox.append(row)

        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
        root.append(listbox)
        total = sum(self.catalog.products[item].price for item in setup.items)
        root.append(Gtk.Label(label=f"Package total: ${total:,.2f}", xalign=0, css_classes=["title-4"]))
        dialog.set_child(root)
        dialog.present(self)

    def _sync_cart_button(self) -> None:
        count = sum(item.quantity for item in self.cart.items)
        self.cart_button.set_visible(count > 0)
        self.cart_button.set_label(str(count) if count > 0 else "")

    def _open_cart_dialog(self, *_args) -> None:
        dialog = Adw.Dialog(content_width=660, content_height=680, title="Order")
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)

        cart_list = Gtk.ListBox(css_classes=["boxed-list"], selection_mode=Gtk.SelectionMode.NONE)

        for item in self.cart.items:
            row = Adw.ActionRow(title=item.product.name, subtitle=f"${item.product.price:,.2f}")
            qty = Gtk.SpinButton.new_with_range(1, 99, 1)
            qty.set_value(item.quantity)
            qty.connect("value-changed", lambda spin, pid=item.product.id: self.cart.set_quantity(pid, spin.get_value_as_int()))
            remove = Gtk.Button(icon_name="user-trash-symbolic")
            remove.connect("clicked", lambda *_ignore, pid=item.product.id: (self.cart.remove(pid), dialog.force_close(), self._open_cart_dialog()))
            row.add_suffix(qty)
            row.add_suffix(remove)
            cart_list.append(row)

        main_box.append(Gtk.Label(label="Line items", xalign=0, css_classes=["title-4"]))
        main_box.append(cart_list)
        main_box.append(Gtk.Label(label=f"Subtotal: ${self.cart.subtotal:,.2f}", xalign=0, css_classes=["title-4"]))
        main_box.append(Gtk.Separator())
        main_box.append(Gtk.Label(label="Checkout", xalign=0, css_classes=["title-4"]))

        form = Gtk.ListBox(css_classes=["boxed-list"], selection_mode=Gtk.SelectionMode.NONE)
        name_row, name_entry = self._entry_row("Name", self.checkout_state.requester_name)
        dept_row, dept_entry = self._entry_row("Department", self.checkout_state.department)
        budget_row, budget_entry = self._entry_row("Budget Number", self.checkout_state.budget_number)
        form.append(name_row)
        form.append(dept_row)
        form.append(budget_row)

        crp_row = Adw.SwitchRow(title="Is this CRP?")
        crp_row.set_active(self.checkout_state.is_crp)
        form.append(crp_row)

        crp_code_row, crp_code_entry = self._entry_row("CRP Project Code", self.checkout_state.crp_project_code)
        crp_approver_row, crp_approver_entry = self._entry_row("CRP Approver", self.checkout_state.crp_approver)
        crp_code_row.set_visible(self.checkout_state.is_crp)
        crp_approver_row.set_visible(self.checkout_state.is_crp)
        form.append(crp_code_row)
        form.append(crp_approver_row)

        crp_row.connect("notify::active", lambda row, *_: (
            crp_code_row.set_visible(row.get_active()),
            crp_approver_row.set_visible(row.get_active())
        ))

        main_box.append(form)

        submit = Gtk.Button(label="Generate Order Email", css_classes=["suggested-action"])
        submit.connect(
            "clicked",
            lambda *_: self._submit_order(
                name_entry.get_text(),
                dept_entry.get_text(),
                budget_entry.get_text(),
                crp_row.get_active(),
                crp_code_entry.get_text(),
                crp_approver_entry.get_text(),
            ),
        )
        main_box.append(submit)

        dialog.set_child(main_box)
        dialog.present(self)

    def _entry_row(self, title: str, value: str) -> tuple[Adw.EntryRow, Gtk.Entry]:
        row = Adw.EntryRow(title=title)
        row.set_text(value)
        return row, row

    def _submit_order(
        self,
        requester_name: str,
        department: str,
        budget_number: str,
        is_crp: bool,
        crp_project_code: str,
        crp_approver: str,
    ) -> None:
        self.checkout_state = CheckoutState(
            requester_name=requester_name,
            department=department,
            budget_number=budget_number,
            is_crp=is_crp,
            crp_project_code=crp_project_code,
            crp_approver=crp_approver,
        )
        is_valid, message = self.checkout_state.validate()
        if not is_valid:
            self._toast(message)
            return

        order = Order(checkout=self.checkout_state, items=self.cart.items)
        mailto_url = build_mailto(order)

        try:
            Gtk.show_uri(self, mailto_url, Gdk.CURRENT_TIME)
            self._toast("Opened default mail client.")
            return
        except Exception:
            pass

        try:
            clipboard = Gdk.Display.get_default().get_clipboard()
            clipboard.set_content(Gdk.ContentProvider.new_for_value(build_body(order)))
            self._toast("Order copied to clipboard.")
            return
        except Exception:
            pass

        output_path = Path.cwd() / "order-export.txt"
        output_path.write_text(build_body(order), encoding="utf-8")
        self._toast(f"Saved order to {output_path.name}")

    def _toast(self, message: str) -> None:
        self.toast_overlay.add_toast(Adw.Toast(title=message, timeout=2))
