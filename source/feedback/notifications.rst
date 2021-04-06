Notifications
=============

Notifications enable you to inform the users about events when they are not using your application. They also provide the ability for users to quickly respond to those events, using notification actions.

When to use
-----------

Use notifications to inform the user about events they will be interested in while they are not using your application. This can include new messages in messaging applications, the completion of long-running tasks, reminders for calendars, and so on.

Notifications shouldn’t be used as a substitute for feedback that is provided by your application windows, which should be able to inform the user about events without the need for notifications.

Notification elements
---------------------

Notifications in GNOME have a number of standard components:

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Element
    - Description
  * - Application Icon
    - Indicates which application sent the notification.
  * - Title
    - The heading for the notification.
  * - Body
    - An optional block of text which gives extra detail about the notification. The notification body can include multiple paragraphs. For example: a snippet from the beginning of an email.
  * - Default Action
    - This is the action that is triggered when the notification is activated.
  * - Actions
    -  Each notification can include up to three buttons.
  
Titles
------

The title should provide a short and concise summary of the event that triggered the notification. The notification body may not always be visible, so it is important to ensure that the notification can be understood from the title alone.

Default actions
---------------

The default action should always dismiss the notification and raise a window belonging to the application that sent the notification. If the notification relates to a particular part of your application’s user interface, the default action should display that part of the UI. The default action for a notification about a new email should show the relevant email message when activated, for example.

Notification actions
--------------------

You can provide useful functionality by embedding buttons in notifications. This allows users to quickly and easily respond to the notification.

* Notification actions should be related to the content of the notification, and should not provide generic actions for your application. This ensures that each notification has a clear focus and purpose.
* Only use notification actions when the functionality that they provide is commonly required.
* Actions should not replace user interface controls elsewhere — it should be possible to take the same actions from your application’s windows.
* It is not necessary to always use notification actions, and many notifications will not require them.
* Notification actions should not duplicate the default action. For example, a new email notification does not need to include an Open button, since the default action should already perform this action.

General guidance
----------------

* It is important not to needlessly distract users with notifications. This can easily become annoying and frustrating, and will not incline users to like your application. Therefore, always be critical when using notifications, and question whether users really need to be informed about the events you want to communicate.
* Applications that deal with lots of events, such as email or social media messages, run a particular risk of distracting users with too many notifications. These applications should place restrictions on how frequently they send notification messages. Instead of showing a notification for each new message, it is a good idea for each notification to provide a summary of new messages.
* Notifications in GNOME persist after they have been initially displayed. It is therefore important to remove notification messages that are no longer relevant to the user.
* Your application window should provide feedback on all the events that have been communicated by notifications. As a result, when your application window is focused, notification messages should be treated as having been read, and should be removed.
* Ensure that your application removes notifications that are no longer valid. For example, a notification for a weather warning that has been revoked should be removed.

API reference
-------------
* `GNotification <https://developer.gnome.org/gio/stable/GNotification.html>`_