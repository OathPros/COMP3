Flow Boxes
==========

.. image:: ../img/screenshots/flow-box.png

Flow boxes provide a generic grid container which can be used to arrange controls or content items. They can be used for the main view of an application or for laying out smaller areas. Examples of flow box usage include:

* a background chooser, with a grid of images from which the user can select
* a tool palette, with a grid of :ref:`toggle buttons <toggle-buttons>`
* a document browser, with a grid of document thumbnails 

Flow boxes are suitable for relatively small static grids. For very large, dynamic grids, see :ref:`grid views <grid-views>`.

General Guidelines
~~~~~~~~~~~~~~~~~~

The following guidelines primarily apply to cases where flow boxes are used to present a grid of content items, as opposed to controls:

* Wherever possible, each grid item should have a unique thumbnail.
* Order the items in the grid according to what will be most useful to users. Ordering content according to most recently added is often the best arrangement.
* The visual styling of the grid should be appropriate to the type of content being displayed. In general, the goal should be to minimize visual distractions and allow the content itself to shine. However, in cases where grid images have irregular shapes or inconsistent appearance, it may be necessary to outline each grid cell.
* Grids and list layouts can be combined, to offer different views of the same content collection. An alternative list view can be useful for displaying additional metadata associated, such as creation dates or authorship.
* Test the grid layout at a variety of widths, in order to ensure that it looks good in the various states it might be used.

API Reference
-------------

* GtkFlowBox: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.FlowBox.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkFlowBox.html>`_