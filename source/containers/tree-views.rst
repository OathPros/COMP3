Tree Views
==========

Tree views can be used for multi-column lists, where sorting the table by columns is common, where performance considerations are important, or where a dense table of data is required.

Tree view cells can contain icons, text, and controls.

Column headers
--------------

Only use column headers when the list has more than one column, or the list has only one column, but the user may wish to re-order the list. (This is rarely useful with single column lists). In most other situations, column headers take up unnecessary space, and the extra label adds visual clutter.

Indicate which column is currently sorted by showing an upward or downward facing arrow in its header:

When using column headers, indicate the sort order using arrows on the header:

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

Trees
-----

Sections of a tree view can be expanded and collapsed with an arrow control.

* Always give tree controls a label, positioned above or to the left of the tree, in sentence capitalization.
* Provide an access key in the label that allows the user to give focus directly to the tree.

API reference
-------------

* `GtkTreeView <https://developer.gnome.org/gtk3/stable/GtkTreeView.html>`_