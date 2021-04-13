.. image:: ../img/placeholder-dialogs.jpg

Dialogs
=======

Dialogs are windows that appear over, and are bound to, a parent window. They are a basic way to show information and controls. There are three types of dialog in GNOME:

* **Message dialogs**: a special type of dialog which is primarily used for feedback, which is :doc:`covered elsewhere </feedback/message-dialogs>`.
* **Action dialogs**: these present options and/or information about an action, before it is carried out. Print dialogs are a classic example of action dialogs.
* **Presentation dialogs**: these contain information or controls, such as properties.

GNOME also provides a number of predefined dialogs for common situations, including preferences and about dialogs.

General guidelines
------------------

* Dialog windows should never pop up unexpectedly, and should only ever be displayed in immediate response to a deliberate user action.
* Dialogs should always have a parent window.
* Avoid stacking dialog windows on top of one another. Ideally, only one dialog window should be displayed at a single time.
* When opening a dialog, provide initial keyboard focus to the component that you expect users to operate first. This focus is especially important for users who must use a keyboard to navigate.

Avoid dialogs where possible
----------------------------

Dialogs obscure other content and require a context switch on the part of a user. As a result, in many situations, more discrete or inline disclosure is often preferable. Examples of how to do this include:

* Using inline composition for new messages, records or contacts.
* Using :doc:`menus </controls/menus>` or :doc:`popovers <popovers>` to display additional controls or options in a less disruptive manner.
* Restricting preferences to a small number of controls, which are placed in a menu.

This principle of avoiding dialogs also applies to preferences dialogs. While these are a common design pattern, it is often better not to have one, if that is possible. Always question whether additional settings are really necessary, and make an effort to ensure that your application design works for everybody without the need to change its settings.

Action Dialogs
--------------

Action dialogs have a header bar, a heading which describes the action, and two primary buttons — one which carries out the action and one which cancels it.

* Label the affirmative button with a specific imperative verb, for example: *Save* or *Print*. This is clearer than a generic label like *OK* or *Done*.
* Always ensure that the cancel button appears first, before the affirmative button. In left-to-right locales, this is on the left.
* Sometimes, the user may be required to choose options before an action can be carried out. In these cases, the affirmative dialog button should be insensitive until the required options have been selected.
* Ensure that the escape key activates the cancel button.

Presentation Dialogs
--------------------

Presentation dialogs present information or controls. Like action dialogs, they have a header bar and a subject.

:doc:`View switchers </nav/view-switchers>` can be used to break up controls and information.
  
API reference
-------------

* GtkDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.Dialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkDialog.html>`_
* GtkAboutDialog: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.AboutDialog.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html>`_
* `AwdPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwPreferencesWindow.html>`_
* `HdyPreferencesWindow <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyPreferencesWindow.html>`_