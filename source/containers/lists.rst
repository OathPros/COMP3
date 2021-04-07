Lists
=====

Lists are a basic user interface element that can be used to present information, content items, or controls. There are two primary types of list in GNOME: standard lists and tables.

:doc:`Sidebar lists <sidebars>` are a separate design pattern which also make use of a list.

When to use
-----------

A list is an appropriate way to present content items that have a distinct name as their primary identifier. If the content is visual in nature, such as with photos or videos, you might want to consider using a :doc:`grid <grids>` instead.

In some cases, it is advantageous to show both a list and a grid view for the same content items. Used in this way, a list view allows additional information to be displayed about the content through columns of information.

Standard lists
--------------

Standard lists are most common list type, and should generally be used in favor of tables.

In standard lists, each row is divided by separators, and changing the sort order is achieved by using a control outside the list itself.

Styles
------

Standard lists have two styles: full-width and embedded. Full-width lists fill their container, while embedded lists are surrounded by padding.

Full-width lists are visually simpler, and therefore more elegant. They should be used where possible. At the same time, it is not always possible to use a full-width list, and there are some situations where embedded lists are a better choice:

* When the list contains columns of information that need to be kept close together for readability purposes, and there is a need to have the list inside a wide container.
* When a window contains several lists.
* When the list needs to be aligned with other controls inside the window.

Editable lists
--------------

Editable lists allow a user to add or remove items from the list (for this reason, they are sometimes known as add/remove lists). Both full-width and embedded lists can be editable.

Each row contains a remove button. If the number of items is short, the final list row should be used as an add button.

Tables
------

Tables can be used for more complex multi-column lists, where sorting the table by a variety of columns is common. Column headers allow people to identify the type of information in each column and to reorder the list according to the content of each column.

When using column headers, indicate the sort order using arrows on the header.

.. list-table::
  :widths: 20 20 60
  :header-rows: 1

  * - Order
    - Arrow Direction
    - Example
  * - Natural
    - Down
    - Alphabetical, smallest number first, earliest date first, checked items first
  * - Reverse
    - Up
    - Reverse alphabetical, largest number first, most recent date first, unchecked items first

Row behavior
------------

Depending on the type of list, rows have different behaviors when they are clicked or pressed. There are three types of list in this regard:

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - List Type
    - Row Behavior
  * - Navigation
    - Selecting a row opens the corresponding item, whether it is by browsing to a new view or opening a dialog. This pattern is common for lists of content items, or for presenting groups of settings.
  * - Select
    - The list item is selected when it is clicked or pressed. This approach is often used for selecting one of a series of configuration options. In the case of drop-down lists, one option is always selected. The selected row is indicated by a check mark.
  * - Edit
    - Selecting the row item turns the row into a text entry field, which allows the item to be edited.

Navigation style lists can be combined with selection mode in order to allow rows to be both opened and manipulated. Using double-click to open list items should be avoided, since it is undiscoverable and is incompatible with touch input.

General guidelines
------------------

* Differentiate the different types of information using different alignments, :doc:`text colors and weights </guidelines/typography>`. Highlight the most important and relevant information by giving other information a lighter weight and/or color.
* Be careful not to overpopulate lists with different columns and elements, and ensure that you only use them to present essential information.
* As a rule of thumb, avoid using several lists in the same window, particularly primary windows.
* Do not use lists with fewer than about five items, unless the number of items may increase over time. For options lists, check boxes or radio buttons can be used as an alternative in this case.
* Ensure that lists are ordered to be helpful to those who are using them. Recent documents might be more useful than alphabetically ordered documents, or contacts that are online might be more interesting than those who are offline, for example.
* If you use icons in your list, use :doc:`symbolic icons </guidelines/icons>`. The lower visual footprint of these icons will mean that they do not visually overload or dominate your list.
* If the list is long, make it possible to search it using the standard :doc:`search design pattern </nav/search>`.

API reference
-------------
* `GtkListBox <https://developer.gnome.org/gtk3/stable/GtkListBox.html>`_
* `GtkTreeView <https://developer.gnome.org/gtk3/stable/GtkTreeView.html>`_