Message Dialogs
===============

Message dialogs are the simplest type of dialog. They present a message or question, along with 1-3 buttons with which to respond. They are always modal, meaning that they prevent access to their parent window. Message dialogs are an appropriate choice when it is essential that the user sees and responds to a message.

When to use
-----------

While message dialogs can be an effective way to disclose additional controls or information, they can also be a source of interruption for the user. For this reason, always question whether a message dialog is necessary, and work to avoid the situations in which they are required.

Examples
--------

Confirmation dialogs use a message dialog to check — or confirm — that the user wants to carry out an action. They have two buttons: one to confirm that the action should be carried out and one to cancel the action.

Note: confirmation dialogs will often be accidentally or automatically acknowledged, and will not always prevent mistakes from happening. It is often better to provide undo functionality instead.

Error dialogs present an error message to the user. They often include a single button that allows the user to acknowledge and close the dialog.

Note: error dialogs should generally be a last resort. You should design your application so that errors do not occur, and to automatically recover if something does go wrong.

Guidelines
----------

* Always ensure that the cancel button appears first, before the affirmative button. In left-to-right locales, this is on the left. This button order ensures that users become aware of, and are reminded of, the ability to cancel prior to encountering the affirmative button.
* Assign the return key to activate the affirmative button. However, this should not be done if its action is irreversible, destructive or otherwise inconvenient to the user. If there is no appropriate button to designate as the default button, do not set one.
* Ensure that the escape key activates the cancel button, if there is one. Message dialogs with a single button can have both escape and return bound to the same button.

API Reference
-------------

* GtkMessageDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.MessageDialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkMessageDialog.html>`_