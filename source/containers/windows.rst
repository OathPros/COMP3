Windows
=======

Windows are the main containers for application user interfaces.

Primary Windows
---------------

Primary windows host the main functionality of your application, and are what is displayed when your application is launched.

* Primary windows should always be independent — closing one primary window should not result in other primary windows being closed.
* Apps can be single primary window only, or they can have multiple primary windows open at any one time. Multiple primary windows are common for viewer or editor apps.

Secondary Windows
-----------------

Secondary windows are used to contain supplemental controls or information, which are infrequently used.Standard secondary windows include **About Windows** and **Preferences Windows**.

* Secondary windows should always be dependent on a primary window, so that closing the primary also closes the secondary.
* Secondary windows can contain information and preferences that are relevant to the entire application, or they can contain information and options for a single content item, such as a document **Properties Window**.
* Typically, secondary windows are modal to a parent window. This ensures that windows are grouped together.
* In more unusual cases, secondary windows can be non-modal to their parent window. This is typically when they provide equivalent functionality to the primary window, such as an email app that allows individual email can be popped out into its own window.

General Guidelines
------------------

Guidelines for all types of windows:

* Windows should have a :doc:`header bar <header-bars>`.
* Windows should follow the standard *Ctrl+W* keyboard shortcut to close. Additionally, modal windows should close on *Esc*.
* Applications which restore a particular view or content item when they are restarted should also restore their previous window size.

Additional guidance on window sizing can be found in the :doc:`scaling and responsiveness guidelines </guidelines/responsive>`.

API Reference
-------------

* GtkApplicationWindow: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ApplicationWindow.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html>`_
* GtkAboutDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.AboutDialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html>`_
* `AwdPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwPreferencesWindow.html>`_
* `HdyPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyPreferencesWindow.html>`_