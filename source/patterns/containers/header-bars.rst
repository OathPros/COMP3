Header Bars
===========

.. image:: /img/screenshots/header-bar.png

Header bars are a standard element that span the top of windows. They allow windows to be dragged, are the site for window management features, and contain application controls.

Header bars often include:

* :doc:`Buttons </patterns/controls/buttons>` for the main user actions, such as *new*, *add*, *open* and *back*. These are placed at the start of the header bar (on the left in left-to-right locales).
* A window heading, which is placed in the center (sometimes this is replaced with a :doc:`view switcher </patterns/nav/view-switchers>`.)
* :doc:`Menus </patterns/controls/menus>`, which are typically placed at the end.

Guidelines
----------

* Arrange controls within the header bar according to the three alignment points — left, center and right.
* Header bars should only contain a small number of key controls. This helps people to understand the primary functionality provided by the window, and ensures that the window can be resized to narrow widths. Additional controls can be included elsewhere.
* The content of header bars can — and should — update along with view or mode changes, so that different controls are shown depending on the content of the window. This ensures that header bar controls are always relevant to the current context.
* Always ensure that there is some blank space in the header bar to allow it to be dragged.
* Primary window header bar controls should all have :doc:`tooltips </patterns/feedback/tooltips>`.

API Reference
-------------
* `Adwaita: AdwHeaderBar <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.HeaderBar.html>`_
* `Handy: HdyHeaderBar <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyHeaderBar.html>`_
* `GTK 4: GtkHeaderBar <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.HeaderBar.html>`_
* `GTK 3: GtkHeaderBar <https://developer.gnome.org/gtk3/stable/GtkHeaderBar.html>`_
