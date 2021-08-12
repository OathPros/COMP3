Boxed Lists
===========

.. image:: /img/screenshots/list.png

Boxed lists are a list design pattern which can be used to organize sets of controls and information. Examples include application preferences or a short list of recent documents in a picker.

The boxed list pattern is appropriate for small static lists. For larger or dynamic lists, see :doc:`list views <list-column-views>`.

Guidelines
----------

* If a boxed list is long, make it possible to search it using the standard :doc:`search design pattern </patterns/nav/search>`.
* Rows typically contain between one and three elements. Different text elements can be differentiated using :doc:`text size, weight and color </guidelines/typography>`.
* If icons are included in a list row, they should use the :doc:`symbolic style </guidelines/ui-icons>`. The lower visual footprint of these icons will mean that they do not visually overload or dominate your list.
* Rows which expand or open another view when activated should have a ``go-next-symbolic`` arrow placed at the end.
* Lists should have a minimum and maximum width, in order to support :doc:`adaptive scaling </guidelines/adaptive>`.

When a boxed list contains controls:

* Follow the example lists for row layout. Typically, the row label should be placed at the start of the row, and controls at the end.
* While rows can contain multiple controls, they can become crowded quickly. Where possible, try and have only a single control in each list row, and don't include more than two.
* Activating a list row background (such as by clicking) should trigger its control.

Design conventions exist for editable boxed lists, with rows that can be added and removed. Each row should contain a remove button. If the number of items is short, the final list row should be used as an add button.

API Reference
-------------

* `GTK 4: GtkListBox <hhttps://docs.gtk.org/gtk4/class.ListBox.html>`_
* `Adwaita: AdwActionRow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ActionRow.html>`_
* `Adwaita: AdwExpanderRow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ExpanderRow.html>`_
* `GTK 3: GtkListBox <https://developer-old.gnome.org/gtk3/3.24/GtkListBox.html>`_
* `Handy: HdyActionRow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwExpanderRow.html>`_
* `Handy: HdyExpanderRow <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyActionRow.html>`_
* Use the ``.content`` style class to ensure proper spacing.
