# Dialog Windows

Dialogs are secondary windows that appear over a primary, parent window. They are used to present additional information or controls, including preferences and properties, or to present messages or questions.

GTK provides a number of stock dialogs that can be used, such as for printing or color selection.

There are three basic types of dialogs.

## When to use

Dialogs are a commonly recognized design pattern, and there are established conventions for the different types of dialogs that you might want to use. The guidelines on each type of dialog provides further information on this.

While dialogs can be an effective way to disclose additional controls or information, they can also be a source of interruption for the user. For this reason, always question whether a dialog is necessary, and work to avoid the situations in which they are required.

There are many ways to avoid using dialogs:

 * Use inline composition for new messages, records or contacts.
 * In-application notifications are an alternative to message dialogs.
 * [Popovers][] can be a way to display additional controls or options in a less disruptive manner.

## Message Dialogs

Message dialogs are the simplest type of dialog. They present a message or question, along with 1-3 buttons with which to respond. They are always modal, meaning that they prevent access to their parent window. Message dialogs are an appropriate choice when it is essential that the user sees and responds to a message.

### Examples

Confirmation dialogs use a message dialog to check — or confirm — that the user wants to carry out an action. They have two buttons: one to confirm that the action should be carried out and one to cancel the action.

Note: confirmation dialogs will often be accidentally or automatically acknowledged, and will not always prevent mistakes from happening. It is often better to provide undo functionality instead.

Error dialogs present an error message to the user. They often include a single button that allows the user to acknowledge and close the dialog.

Note: error dialogs should generally be a last resort. You should design your application so that errors do not occur, and to automatically recover if something does go wrong.

## Action Dialogs

Action dialogs present options and information about a specific action before it is carried out. They have a heading (which typically describes the action) and two primary buttons — one which allows the action to be carried out and one which cancels it.

Sometimes, the user may be required to choose options before an action can be carried out. In these cases, the affirmative dialog button should be insensitive until the required options have been selected.

### Examples

Many of the stock GTK dialogs are action dialogs. The print dialog is a good example: it is displayed in response to the user using the print action, and presents information and options for that print action. The two header bar buttons allow the print action to either be cancelled or carried out.

## Presentation Dialogs

Presentation dialogs present information or controls. Like action dialogs, they have a header bar and a subject. However, instead of prefixing an action, their content relates to an application or content item.

### Examples

Preferences and properties are both examples of presentation dialogs, and both present information and settings in relation to a specific entity (either an application or a content item). Properties dialogs are a good example of how dialogs can be used to disclose additional information which is not always needed in the main application window.

Note: resist the temptation to provide a preference window for your application. Always question whether additional settings are really necessary. Most people will not bother to investigate the preferences that you provide, and configuration options will contribute to the complexity of your application. Make an effort to ensure that your application design works for everybody without the need to change its settings.

## Instant and Explicit Apply

Presentation dialogs are either instant or explicit apply. In instant apply dialogs, changes to settings or values are immediately updated. In contrast, explicit apply dialogs include a button for applying changes.

Instant apply should be used wherever possible. Instant apply presentation dialogs have a close button in their header bar, like a primary window (see [Primary Windows][]).

Explicit apply is only necessary if changes in the dialog have to be applied simultaneously in order to have the desired behaviour. Explicit apply dialogs include a *Done* and *Cancel* button (*Cancel* resets all values in the dialog to the state before it was opened and Done applies all changes and closes the window).

## Primary buttons

Message and action dialogs include primary buttons which affect the whole window. The order of these buttons, as well as the labels used, are a key part of the dialog.

### Order

When a dialog includes an affirmative and a cancel button, always ensure that the cancel button appears first, before the affirmative button. In left-to-right locales, this is on the left.

This button order ensures that users become aware of, and are reminded of, the ability to cancel prior to encountering the affirmative button.

### Labels

Label the affirmative primary button with a specific imperative verb, for example: *Save*, *Print*, *Remove*. This is clearer than a generic label like *OK* or *Done*.

Error dialogs typically include a single button which dismisses the dialog. In this case, a specific action does not need to be referenced, and this can be a good opportunity to use humor. *Apology Accepted* or *Got It* are both examples of good labels.

### Default action and escape

Assign the return key to activate the primary affirmative button in a dialog (for example *Print* in a print dialog). This is called the default action, and is indicated by a different visual style. Do not make a button the default if its action is irreversible, destructive or otherwise inconvenient to the user. If there is no appropriate button to designate as the default button, do not set one.

You should also ensure that the escape key activates the cancel or close button, should either of them be present. Message dialogs with a single button can have both escape and return bound to the button.

Binding return and escape in this way provides a predictable and convenient way to continue through a dialog, or to go back.

## General guidelines

 * Dialog windows should never pop up unexpectedly, and should only ever be displayed in immediate response to a deliberate user action.
 * Dialogs should always have a parent window.
 * Follow the layout guidelines when designing the content of windows.
 * Use [view switchers][] or [tabs][] to break up controls and information.
 * Avoid stacking dialog windows on top of one another. Only one dialog window should be displayed at a time.
 * When opening a dialog, provide initial keyboard focus to the component that you expect users to operate first. This focus is especially important for users who must use a keyboard to navigate your application.

## API reference

 * [GtkAboutDialog](https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html)
 * [GtkDialog](https://developer.gnome.org/gtk3/stable/GtkDialog.html)
 * [GtkMessageDialog](https://developer.gnome.org/gtk3/stable/GtkMessageDialog.html)

