Model-Based Containers
======================

The standard :doc:`lists <lists>` and :doc:`grids <flow-boxes>` provide user interface containers which are appropriate for the majority of simple use cases. In addition, the GNOME platform also provides a set of model-based containers, which support very large and/or highly dynamic content collections. These model-based containers include :ref:`list views <list-views>`, :ref:`column views <column-views>`, and :ref:`grid views <grid-views>`.

These containers can be used in combination, to provide different views on the same content.

While offering performance advantages, these containers have other design limitations. Therefore, before designing an application that presents content using a list, grid or table, it is recommended to familiarize yourself with the options available.

.. _list-views:

List Views
----------

List view rows can contain text, images or controls. Rows can also be filtered and searched. Support is currently limited for creating the kind of standard list styles described :doc:`elsewhere in the HIG <lists>`.

A list view example can be found under *Lists → Settings*, in the GTK 4 demo application.

.. _column-views:

Column Views
------------

Column views are similar to list views, with the difference that they can display multiple columns. The top of each column has a header, which can be used for sorting.

A column view example can be found under *Lists → Settings*, in the GTK4 demo application.

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

.. _grid-views:

Grid Views
----------

A model-based grid view can follow the same guidance as :doc:`flow boxes <flow-boxes>`. The main difference is that it can be combined with a :ref:`model-based list view <list-views>`, for providing a different view of the same content collection.

A grid view example can be found under *Lists → Colors*, in the GTK 4 demo application.

API Reference
-------------

* `GTK 4: GtkListView <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ListView.html>`_ 
* `GTK 4: GtkColumnView <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ColumnView.html>`_
* `GTK 4: GtkGridView <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.GridView.html>`_