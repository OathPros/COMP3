Flow Boxes
==========

Flow boxes provide a generic grid container which can be used to arrange controls or content items. They can occupy the main view of an application or a smaller container.

Examples include a palette of colors or tools, or selecting an image from a small collection.

Flow boxes are suitable for relatively small static grids. For large, dynamic grids, see :doc:`model-based containers <model-based>`.

A flow box example can be found in the GTK4 demo app.

General guidelines
~~~~~~~~~~~~~~~~~~

* Wherever possible, each grid item should have a unique thumbnail.
* Order the items in the grid according to what will be most useful to people using your application. Ordering content according to most recently added is often the best arrangement.
* The visual styling of the grid should be appropriate to the type of content being displayed. In general, the goal should be to minimize visual distractions and allow the content itself to shine. However, in cases where grid images have irregular shapes or inconsistent appearance, it may be necassary to identify the grid outline in order to maintain its visual structure.
* Grids and list layouts can be combined, to offer different views of the same content collection. An additional list view can be useful for displaying additional metadata associated, such as creation dates or authorship.
* Test the grid layout at a variety of widths, in order to ensure that it looks good in the various states it might be used.

API reference
-------------

* `GTK4: GtkFlowBox <https://developer.gnome.org/gtk4/stable/GtkFlowBox.html>`_