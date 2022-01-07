Boxed Lists
===========

.. image:: /img/screenshots/list.png

Boxed lists are a common type of list that can contain both controls and information. Examples include application preferences or a short list of recent documents in a picker.

The boxed list pattern is appropriate for relatively small static lists. For large or dynamic lists, see :doc:`list views <list-column-views>`.

Guidelines
----------

Organize lists semantically, using the :ref:`same guidelines as menus <menu-organization>`. Multiple lists can be included in the same view, to act as different sections. If necessary, each list can be given a heading.

Boxed list rows can include purely informational content or controls. They can also act as a link to another view (rows which do this should have a ``go-next-symbolic`` arrow placed at the end).

Rows that include controls should generally just have one, and should have a maximum of two. When there is a control, clicking the list background should trigger the control.

Lists have a number of style and layout considerations:

* If a list row includes multiple text elements, differentiate them using :doc:`text size, weight and color </guidelines/typography>`.
* If icons are included in a list row, they should typically have the :doc:`symbolic style </guidelines/ui-icons>`. The lower visual footprint of these icons will mean that they do not visually overload or dominate your list.
* Lists should have a minimum and maximum width, in order to support :doc:`adaptive scaling </guidelines/adaptive>`.

Predefined List Rows
--------------------

For convenience, GNOME provides a number of predefined list rows. These can also be used as the basis of custom row designs of your own.

* `Action rows <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ActionRow.html>`_ include a title, subtitle, and a control.
* `Expander rows <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ExpanderRow.html>`_ expand to reveal additional rows below.
* `Combo rows <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ComboRow.html>`_ include a drop down list, from which a single option can be selected.

Editable Lists
--------------

Design conventions exist for editable boxed lists, which allow users to add, remove and reorder rows.


* Rows can be added using an add button that is shown at the top of the list, or with an add list row, which is placed at the end of the list.
* Place a remove button at the end of each row.
* If changing list order is required:
   * Include drag handles at the beginning of the rows, to allow moving them.
   * Instead of showing a remove button at the end of each row, include a button menu, with items for "move up", "move down," and "remove" (menu items for move actions are required for accessibility purposes).
    
API Reference
-------------

* `GTK 4: GtkListBox <https://docs.gtk.org/gtk4/class.ListBox.html>`_
* `GTK 3: GtkListBox <https://docs.gtk.org/gtk3/class.ListBox.html>`_
* `Adwaita .boxed-list documentation <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/boxed-lists.html>`_
