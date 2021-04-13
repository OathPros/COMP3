Windows
=======

Windows are the main container for application user interfaces.

General guidelines
------------------

* A single primary window should always be displayed when your application is launched.
* Primary windows should host the main functionality of your application. Do not rely on dialogs or secondary windows in order to present basic functionality.
* Primary windows should be independent — closing one primary window should not result in other primary windows being closed.
* TODO: default window sizing
* TODO: when should windows be resizable/non-resizable?
* Most application windows should have a :doc:`header bar <header-bars>`.

Single instance applications
----------------------------

Single instance applications have a single primary window. This model is common for messaging applications, such as email, or media applications, like music players.

Multiple instance applications
------------------------------

Multiple instance applications have multiple windows. These can be organized in two ways:

#. **Sibling windows**: this is the more common pattern, and is typically used by viewer or editor apps. Here, each window is identical and independent. Closing a window just closes that window and no others.
#. **Parent-child windows**: in this less common pattern, there is one primary window and multiple dependent secondary windows. Closing a secondary window does not affect any others. On the other hand, closing the primary parent window should close every window belonging to the app. An example might be an email app, in which a single email can be opened in a separate window.

API reference
-------------

* GtkApplicationWindow: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ApplicationWindow.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html>`_