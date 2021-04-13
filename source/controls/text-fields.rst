Text Fields
===========

Text fields have a variety of uses, including search, messaging input, preferences and forms.

General Guidelines
------------------

* Size text fields according to the likely size of the content they will contain. This gives a useful visual cue to the amount of input expected.
* In an instant-apply dialog validate the contents of the entry field when it loses focus or when the window is closed, not after each keypress. Exception: if the field accepts only a fixed number of characters, such as a hexadecimal color code, validate and apply the change as soon as that number of characters have been entered.
* If the text field only accepts certain characters, such as digits, play the system warning beep when someone types an invalid character.
* Keyboard navigation and tab entry:
   * Normally, pressing Tab in a single-line entry field should move focus to the next control, and in a multi-line entry field it should insert a tab character.
   * Pressing Ctrl+Tab in a multi-line entry field should move focus to the next control.
   * Ctrl+Tab can be used as a way to insert tab characters into single entry fields.
  
Embedding information and controls
----------------------------------

Icons and icon buttons can be placed inside a text field, either at the beginning or the end.

* Common conventions for embedding icons include a search icon at the beginning of the text field, and a clear icon at the end of the text field.
* Embedded icons should use symbolics only.
* TODO: standard design pattern for indicating caps lock and case sensitivity.
* TODO: standard design pattern for toggling field text visibility.

TODO: do we actually support hint texts? When a user would benefit from additional information in order to use a text entry field, it can be prefilled with a hint text. As with any decision to display additional information, this should only be done when it is necessary.

API reference
-------------

* GtkEntry: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.Entry.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkEntry.html>`_