Keyboard Interaction
====================

Keyboards are a common way to interact with user interfaces. They provide a convenient and effective means to use applications in a variety of situations, and can be faster and more efficient than other input devices. Keyboards are also vital for visually-impaired people or those with mobility impairments.

You should ensure that all the functionality provided by your application can be accessed using a keyboard. Trying to use your application with only a keyboard is a great way to test this.

Keyboard interaction has three aspects in GNOME and GTK: navigation, access keys, and shortcut keys. Search is another, additional aspect.

Keyboard navigation
-------------------

Make sure that it is possible to move around and interact with every part of your user interface using the keyboard, by following these guidelines.

- Follow the standard GNOME keys for navigation. Tab is the standard key for moving around an interface with GTK and GNOME.
- Use a logical keyboard navigation order. When navigating around a window with Tab, keyboard focus should move between controls in a predictable order. In Western locales, this is normally left to right and top to bottom.
- In addition to navigation using Tab, make an effort to allow movement using the arrow keys, both within user interface elements (such as lists, icon grids or sidebars), and between them.

Note: if activating a control enables other controls, do not automatically give focus to the first dependent control when it is activated, but instead leave focus in place.

.. _access-keys:

Access keys
-----------

Access keys allow someone to operate labelled controls by using Alt. They are indicated by an underlined letter within each control label (this is displayed when Alt is held down).

* Where possible, all labelled components should have an access key.
* Choose access keys that are easy to remember. Normally this means using the first letter of the label. If the label has more than one word, the first letter of one of its other words can also be used. Additionally, if another letter provides a better association (for example: “x” in “Extra Large”) , consider using that letter instead.
* Avoid assigning access keys to “thin” letters (such as lowercase i or l), or letters with descenders (such as lowercase g or y), unless it is unavoidable. The underline is sometimes not as clear with these characters.
* If the choice of access keys is difficult, assign access keys to the most frequently-used controls first. If the first letter is not available, choose an easy to remember consonant from the label, for example, “p” in “Replace”. Only assign vowels once no consonants are available.
* Be aware that access keys have to be translated together with the strings that they are taken from, so even if there are no conflicts in your native language, they may occur in translations.

.. _shortcut-keys:

Shortcut keys
-------------

Shortcut keys provide convenient access to common operations. They can be either single keys or combinations of several key presses (typically a modifier in combination with a regular key)

* Do not assign system-level shortcut keys for use in your application. See below for details on these.
* Use the standard GNOME shortcut keys (see below) if your application supports those functions. This ensures consistency between GNOME applications and aids discoverability.
* Assign shortcut keys to the most commonly-used actions in your application. However, do not try to assign a keyboard shortcut to everything.
* Try to use Ctrl in combination with a letter for your own shortcuts. Shift+Ctrl and a letter is the recommended pattern for shortcuts that reverse or extend another function. For example, Ctrl+Z and Shift+Ctrl+Z for undo and redo.
* New shortcut keys should be as mnemonic as possible, as these will be easier to learn and remember. For example, Ctrl+E would be a good shortcut for a menu item called Edit Page.
* Shortcuts that can be easily used with one hand are preferable for common operations.
* Do not use Alt for shortcut keys, as this may conflict with access keys.