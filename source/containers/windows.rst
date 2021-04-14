Windows
=======

Windows are the main containers for application user interfaces.

Primary Windows
---------------

Primary windows host the main functionality of your application, and are what is displayed when your application is launched.

* Primary windows should always be independent — closing one primary window should not result in other primary windows being closed.
* Most application windows should have a :doc:`header bar <header-bars>`.
* Apps can be single instance, meaning that they only ever have one primary window open, or multiple instance, meaning that they can have multiple primary windows open at any one time. Multiple instance windows are common for view or editor apps.

Secondary Windows
-----------------

Secondary windows are used to contain supplemental controls or information, which are infrequently used. Standard secondary windows include **About Windows** and **Preferences Windows**.

A secondary window should always be dependent on a primary window, so that closing the primary also closes the secondary.

Typically, secondary windows are modal to a parent window. This ensures that windows are grouped together.

However, secondary windows can be non-modal when they provide equivalent functionality to the primary window. In an email app, an individual email can be popped out into a secondary window, for example. In this case, the secondary window does not need to be modal.

General guidelines
------------------

* TODO: default window sizing
* TODO: when should windows be resizable/non-resizable?

API Reference
-------------

* GtkApplicationWindow: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ApplicationWindow.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html>`_
* GtkAboutDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.AboutDialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html>`_
* `AwdPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwPreferencesWindow.html>`_
* `HdyPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyPreferencesWindow.html>`_