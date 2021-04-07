Primary Windows
===============

Primary windows are the basic high-level container for your application user interface, and should present the core functionality of your application.

When to use
-----------

Every application should show a primary window when its launcher is activated. This includes applications that mainly provide a background service.

Application types
-----------------

There are two main models for primary windows:

Single instance applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single instance applications have a single primary window. This model is common for messaging applications, such as email, chat, or contacts.

Multiple instance applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple instance applications can have multiple primary windows. Typically, each primary window will be identical. Multi-instance applications are frequently viewers or editors, such as for documents or images.

Both single and multiple instance applications can allow multiple content items to be opened, either through the use of :doc:`tabs </nav/tabs>` or :doc:`browsing </nav/browsing>`. However, multiple windows do offer additional capabilities, which include:

* Viewing several content items alongside each other.
* Placing content on different workspaces.
* Organizing sets of content into different windows (if using tabs).

Parent/child primary windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple instance applications typically have identical primary windows (in the case multiple web browser windows, for example). However, this is not always the case.

Primary windows can have a parent/child relationship. In this type of application, there is only ever one parent window. This typically contains an overview of content items which can be opened in the parent window, or in a separate child window. This allows multiple content items to be simultaneously open.

While child windows can only be opened through a parent window, they are not dependent on them in order to stay open: closing the parent window does not result in the closure of the application's child windows.

General guidelines

* A single primary window should always be displayed when your application is launched.
* If your application launcher is activated while your application is running, all its primary windows should be displayed.
* Primary windows should host the main functionality of your application. Do not rely on dialogs or secondary windows in order to present basic functionality.
* Primary windows should be independent — closing one primary window should not result in other primary windows being closed.
* Dialog windows should always be dependent on a primary window. (See :doc:`the dialogs guidelines </containers/dialogs>`.)
* *Quit* should close all primary windows.

API reference
-------------

* `GtkWindow <https://developer.gnome.org/gtk3/stable/GtkWindow.html>`_
* `GtkApplicationWindow <https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html>`_