Toasts
======

.. image:: /img/adw-screenshots/toast-overlay.png
   :class: light
.. image:: /img/adw-screenshots/toast-overlay-dark.png
   :class: dark

Toasts are popup banners that contain a label and sometimes a button. They are always transient and user dismissible.

When to Use
-----------

Toasts can be used to show messages and actions in the context of using an application. Typically they are shown in response to a user action. One common use for toasts is to show an undo button after a destructive action.

Toasts are transient and are therefore best suited to communicating individual events, as opposed to ongoing states. The latter are better served by :doc:`info bars <info-bars>`.

Since toasts are only shown in the context of an application's window, they are only appropriate for feedback that is useful while the application is being used. If it is useful for a message to be visible while the app is not being used, a :doc:`notification <notifications>` is probably a better choice.

Guidelines
----------

* Each toast should have a short and simple title.
* Toasts shouldn't always include a button. Only include one if it is directly relevant to the message that is being communicated, and will be generally useful.
* Toast titles should use the :ref:`informal heading style <informal-headings>`.

API Reference
-------------

* `AdwToast <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.Toast.html>`_
