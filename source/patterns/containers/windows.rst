Windows
=======

.. image:: /img/adw-screenshots/application-window.png
   :class: only-light
.. image:: /img/adw-screenshots/application-window-dark.png
   :class: only-dark

Windows are the main containers for app user interfaces.

Primary Windows
---------------

Primary windows host the main functionality of your app, and are what is displayed when your app is launched.

* Primary windows should always be independent — closing one primary window should not result in other primary windows being closed.
* Apps can be restricted to a single primary window, or can make it possible to have multiple primary windows open at the same time (the latter being common in viewer and editor apps).
* All primary windows should be resizable.
* The default size of primary windows should be appropriate to their content. Windows that display large content like documents or videos should be big enough to support viewing and editing without the need to increase the window size. On the other hand, windows with a limited amount of UI can and should default to a smaller size, in order to avoid large amounts of blank space.

Secondary Windows
-----------------

Secondary windows are created by the primary window, but are able to be moved and resized independently of it. Their primary use is to present information or options in a new container, without blocking the parent window.

Secondary windows should be used sparingly, and only in specific circumstances. Potential uses of secondary windows include:

* A development application launching a preview window.
* An email application allowing you to "pop out" an email into its own window.

Secondary windows are always dependent on their primary windows: when the primary window closes, the secondary window should close, too.

Secondary windows are distinct from :doc:`dialogs </patterns/feedback/dialogs>`. In most cases, if you need to present additional information in its own container, a dialog is a better fit.

General Guidelines
------------------

* Windows should follow the standard Ctrl+W keyboard shortcut to close.
* Apps which restore a particular view or content item when they are restarted should also restore their previous window size.

Additional guidance on window sizing can be found in the :doc:`scaling and adaptiveness guidelines </guidelines/adaptive>`.

API Reference
-------------

* `Libadwaita: AdwApplicationWindow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.ApplicationWindow.html>`_
* `Libadwaita: AdwWindow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/class.Window.html>`