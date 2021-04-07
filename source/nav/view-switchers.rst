View Switchers
==============

A view switcher is a control that allows switching between a number of predefined views. It appears as a set of toggle buttons that are placed in the center of a header bar.

When to use
-----------

There are two primary cases when a view switcher is appropriate:

* When presenting content, and it is useful to be able to view different sets or sub-sets of content. For example, a music application could show different views for artists, albums and playlists.
* If your application provides discrete groups of functionality which are typically used independently.

As a rule of thumb, a view switcher should contain between three and five views. If you have more views, a :doc:`sidebar <sidebars>` might be a more appropriate view switching control.

Additional guidelines
---------------------

* Each view should have a short and clear title.
* Buttons in the view switcher widget can indicate when there is activity in a view.

API reference
-------------

* `GtkStack <https://developer.gnome.org/gtk3/stable/GtkStack.html>`_
* `GtkStackSwitcher <https://developer.gnome.org/gtk3/stable/GtkStackSwitcher.html>`_