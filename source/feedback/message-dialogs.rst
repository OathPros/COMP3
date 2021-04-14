Message Dialogs
===============

Message dialogs present a message or question, along with 1-3 buttons with which to respond. They are modal, meaning that they prevent access to their parent window. Message dialogs are an appropriate choice when it is essential that the user sees and responds to a message.

When to use
-----------

Standard examples of message dialogs include confirmation and error dialogs:

* Confirmation dialogs use a message dialog to check — or confirm — that the user wants to carry out an action. They have two buttons: one to confirm that the action should be carried out and one to cancel the action.
* Error dialogs present an error message to the user. They often include a single button that allows the user to acknowledge and close the dialog.

Both of these patterns have their uses. In particular, confirmation dialogs should be used for destructive operations, both to alert the user to the risk, to clarify which action will be taken, and to give them the opportunity to change their mind.

Nevertheless, message dialogs are a source of interruption and should therefore always be questioned. Additionally, users will often habitually click through message dialogs without fully reading or considering them. 

Undo is typically a superior alternative to confirmation dialogs, since it avoids interrupting the user, allows users to recover from errors, and gives them more time to change their mind. (In cases where it is not possible to offer an undo feature, a confirmation dialog is still recommended for destructive actions.)

Guidelines
----------

* Always ensure that the cancel button appears first, before the affirmative button. In left-to-right locales, this is on the left. This button order ensures that users become aware of, and are reminded of, the ability to cancel prior to encountering the affirmative button.
* Assign the return key to activate the affirmative button. However, this should not be done if its action is irreversible, destructive or otherwise inconvenient to the user. If there is no appropriate button to designate as the default button, do not set one.
* Ensure that the escape key activates the cancel button, if there is one. Message dialogs with a single button can have both escape and return bound to the same button.

API Reference
-------------

* GtkMessageDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.MessageDialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkMessageDialog.html>`_