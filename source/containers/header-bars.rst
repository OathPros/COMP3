Header Bars
===========

Header bars are placed at the top of windows. They allow the window to be dragged, are the site for window management features, and contain application controls.

Guidelines
----------

* Arrange controls within the header bar according to the three alignment points — left, center and right.
* “New”, “add”, “open” and “back” buttons should be placed on the left side of the header bar.
* Header bars should only contains a small number of key controls — this will help users to understand the primary functionality provided by the window, and will ensure that the window can be resized to narrow widths.
* The content of header bars can — and should — update along with view or mode changes. This ensures that header bar controls are always relevant to the current context:
   * If the window includes multiple views (accessed through a :doc:`view switcher </nav/view-switchers>`), the header bar can show different controls for each view.
   * If the window incorporates navigation, different controls can be shown depending on the location displayed in the window. It is common to show a back button on the left side of the header bar when navigating.
* Always ensure that there is some blank space in the header bar to allow it to be dragged. This is necessary to enable windows to be moved or resized.

API reference
-------------

* `GtkHeaderBar <https://developer.gnome.org/gtk3/stable/GtkHeaderBar.html>`_