List & Column Views
===================

List views are a type of list, in which each row is a generic container that can include text, images and controls. Column views are similar to list views, with the difference that they can display multiple columns. The top of each column has a header, which can allows sorting the view by that column.

List views are an alternative to the :doc:`boxed list design pattern <boxed-lists>`. Boxed lists are appropriate for simple use cases, in which the number of items is static and low. In contrast, list views are able to handle very large lists, including those with dynamic content.

List views and column views also share the same data model as :doc:`grid views <grid-views>`, and can therefore be used to offer an alternative view of content which is also displayed as a grid.

General Guidelines
------------------

* Keep list rows simple and regular. Most should only contain one or two elements each.
* When a list row contains multiple text elements, adjust the font size and weight to differentiate each element (see the :doc:`typography guidelines </guidelines/typography>` for more information).
* If icons are included in a list, they should use the :doc:`symbolic style </guidelines/ui-icons>`.
* By default, use a list order that will be most useful to users.
* List views and column views should have a minimum and maximum width, in order to support :doc:`adaptive scaling </guidelines/adaptive>`.

Column View Sorting
-------------------

Indicate which column is sorting the view by showing an upward or downward facing arrow in its header:

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

Clicking an unsorted column header sorts the column in natural order, indicated by showing a down arrow in its header.

Clicking a column header sorted in natural order re-sorts it in reverse order, indicated by showing an up arrow in its header.

API Reference
-------------

* `GTK 4: GtkListView <https://docs.gtk.org/gtk4/class.ListView.html>`_
* `GTK 4: GtkColumnView <https://docs.gtk.org/gtk4/class.ColumnView.html>`_
