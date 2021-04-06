Text Fields
===========

A text entry field is an interface element for entering or editing text. It is a basic element with a variety of uses, including search entry, settings and preferences, or account configuration and setup. A text entry field can be prefilled with text, and can include additional buttons or icons.

General Guidelines
------------------

* Size text fields according to the likely size of the content they will contain. This gives a useful visual cue to the amount of input expected and prevents overflow.
* In an instant-apply dialog validate the contents of the entry field when it loses focus or when the window is closed, not after each keypress. Exception: if the field accepts only a fixed number of characters, such as a hexadecimal color code, validate and apply the change as soon as that number of characters have been entered.
* If you implement an entry field that only accepts certain characters, such as digits, play the system warning beep when the user tries to type an invalid character.
* Normally, pressing Tab in a single-line entry field should move focus to the next control, and in a multi-line entry field it should insert a tab character. Pressing Ctrl+tab in a multi-line entry field should move focus to the next control.
* If you need to provide a keyboard shortcut that inserts a tab character into a single line entry field, use Ctrl+Tab. You are unlikely to find many situations where this is useful, however.
  
Embedding information and controls
----------------------------------

A variety of additional information or controls can be inserted within a text entry field.

Icons or icon buttons can be placed inside a text field to provide status information or additional controls.

* An icon at the beginning of the entry can be used to indicate its purpose — replacing the need for the entry to be labelled. Search entry fields are the classic example of this, where a search icon is placed on the left side of the entry field.
* If the text to be entered is case sensitive, a warning icon can be shown inside the text field if caps lock is on. This is typically shown on the right side of the entry.
* If it is common for the text field to be cleared, a clear icon button can be placed inside the field, at the right side.
* If you place an icon in a text entry field (either as an indicator or a button), use its symbolic variant from the GNOME Symbolic Icon Theme.

When a user would benefit from additional information in order to use a text entry field, it can be prefilled with a hint text. As with any decision to display additional information, this should only be done when it is necessary.

API reference
-------------

* `GtkEntry <https://developer.gnome.org/gtk3/stable/GtkEntry.html>`_