Grids
=====

Two dimensional grids of images or icons are a common way to present content. Selecting an item in the grid will typically switch to a dedicated view of that item.

When to use
-----------

Since the grid view utilizes an image for each item it presents, it is best suited to content that has a visual component, such as documents or photos. If content items don't have a visual component, a :doc:`list view <lists>` might be more appropriate.

Grids and lists can be combined, to offer different views of the same content. This can be useful if content items have additional metadata associated with them, such as creation dates or authorship.

General guidelines
------------------

* Wherever possible, each grid item should have a unique thumbnail.
* Order the items in the grid according to what will be most useful to people using your application. Ordering content according to most recently used is often the best arrangement.
* TODO: surely there's more to say here...

API reference
-------------

* `GtkFlowBox <https://developer.gnome.org/gtk3/stable/GtkFlowBox.html>`_