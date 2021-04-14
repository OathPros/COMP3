Lists
=====

Lists are a common container, and are often used to organize sets of controls as well as content. They can be used for the main view of an application or for smaller containers. Examples include application preferences, a contacts list, or a list of recent documents.

The standard list in GNOME is appropriate for relatively small static lists. For larger lists, see :doc:`model-based containers <model-based>`.

A lists example can be found in the LibAdwaita demo app.

Guidelines
----------

* If a list is long, make it possible to search it using the standard :doc:`search design pattern </nav/search>`.
* Rows typically contain between one and three elements. Different text elements can be differentiated using :doc:`text size and color </guidelines/typography>`.
* Icons in a list should use the :doc:`symbolic style </guidelines/icons>`. The lower visual footprint of these icons will mean that they do not visually overload or dominate your list.
* Rows which expand or open another view should have an arrow placed at the end.
* Activating a row background (such as by clicking) should trigger its control.
* Design conventions exist for editable lists, with rows that can be added and removed. Each row should contain a remove button. If the number of items is short, the final list row should be used as an add button.

Advice for lists that contain controls:

* Follow the example lists for row layout. Typically, the row label should be placed at the start of the row, and controls at the end.
* While rows can contain multiple controls, they can become crowded quickly. A single control is more comfortable than two, and try to avoid any more than two.

API Reference
-------------

* GtkListBox: `GTK 4 <hhttps://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ListBox.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkListBox.html>`_
* `AdwActionRow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwActionRow.html>`_
* `HdyActionRow <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyActionRow.html>`_
* Use the ``.content`` style class to ensure proper spacing.