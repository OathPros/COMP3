Header Bars
===========

Header bars are a common horizontal element which are placed at the top of windows. They play a number of roles:

* Window controls — header bars allow windows to be moved by dragging, include window control buttons (typically a single close button), and provide access to a window controls menu.
* Headings — a key role of a header bar is to provide context for the content of the window, either through a heading or view switcher.
* Controls — header bars provide a place for key controls, typically in the form of buttons.

When to use
-----------

Header bars are recommended for all application windows. They provide a number of advantages over the traditional combination of title bar, menu bar and toolbar, including a smaller vertical footprint, and dynamic navigation and mode changes (such as with selection mode).

Header bars are incompatible with menu bars. If your application already incorporates a menu bar, you should evaluate the alternatives suggested in these guidelines.

Controls
--------

Header bars can contain key controls for the window, which can be placed on the left and right-hand side of the header bar. Examples of these controls include buttons for navigating back and forward, search, and selecting content.

Ensure that your header bar only contains a small number of key controls — this will help users to understand the primary functionality provided by the window, and will ensure that the window can be resized to narrow widths.

If a window requires more controls than can be comfortably accommodated within the header bar, additional functionality can be included within a header bar menu.

Header bars are dynamic
-----------------------

A header bar can — and should — update along with view or mode changes. This ensures that header bar controls are always relevant to the current context.

If the window includes multiple views (accessed through a :doc:`view switcher </nav/view-switchers>`), the header bar can include different controls for each view.

If the window incorporates navigation, different controls can be shown depending on the location displayed in the window itself. It is common to show a back button on the left side of the header bar when navigating.

Additional guidance
-------------------

* A header bar should always provide context for the window it belongs to. This aids window identification, and clarifies what is displayed in the window itself. This can either be done by placing a heading in the center of the header bar, or by including a :doc:`view switcher </nav/view-switchers>`.
* Arrange controls within the header bar according to the three alignment points — left, center and right.
* New and back buttons should be placed on the left side of the header bar.
* Always ensure that there is room for a header bar to be dragged. This is necessary to enable windows to be moved or resized.

API reference
-------------

* `GtkHeaderBar <https://developer.gnome.org/gtk3/stable/GtkHeaderBar.html>`_