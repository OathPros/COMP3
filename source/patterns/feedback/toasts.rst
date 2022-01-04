Toasts
======

.. image:: /img/screenshots/toast.png

Toasts are popup banners which contain a label and sometimes a button. They are always transient and user dismissable.

When to Use
-----------

Toasts can be used to show messages and offer actions in response to user interaction with an app. One common use for toasts is to show an undo button after a destructive action.

Toasts are transient and are therefore best suited to communicating individual events, as opposed to ongoing states. The latter are better served by :doc:`info bars <info-bars>`.

Additionally, since toasts are only shown in the context of an application's window, they are only appropriate for feedback that is useful while the application is being used. If it is important that the message be visible while the app is not being used, a :doc:`notification <notifications>` is probably a better choice.

Guidelines
----------

* Each toast should have a short and simple title.
* Toasts shouldn't always include a button. Only include one if it is directly relevant to the message that is being communicated, and will be generally useful.
* Toast titles should use the :ref:`informal heading style <informal-headings>`.

API Reference
-------------

* `AdwToast <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.Toast.html>`_
