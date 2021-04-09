Windows
=======

Windows are the main, primary container for application user interfaces.

General guidelines
------------------

* A single primary window should always be displayed when your application is launched.
* Primary windows should host the main functionality of your application. Do not rely on dialogs or secondary windows in order to present basic functionality.
* Primary windows should be independent — closing one primary window should not result in other primary windows being closed.
* *Quit* should close all primary windows.

Single instance applications
----------------------------

Single instance applications have a single primary window. This model is common for messaging applications, such as email, or media applications, like music players.

Multiple instance applications
------------------------------

Multiple instance applications can have either multiple primary windows, or one primary and multiple secondary windows.

Multiple primary windows is the more common pattern, and is typically used by viewer or editor apps. Here, each primary window is independent: closing one should not close the others.

One primary and multiple secondary windows is less common. An example might be an email app, in which a single email can be opened in a separate window. If taking this approach, there should only be one primary window. Closing that window should also close all secondary windows.

API reference
-------------

* `GtkApplicationWindow <https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html>`_