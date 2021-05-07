Keyboard
========

Keyboard interaction covers a range of behaviors, including text entry, shortcuts and basic keyboard activation of controls, right through to the keyboard being used as the sole input device. The latter is vital for visually-impaired people or those with mobility impairments.

While many aspects of keyboard interaction are relevant to accessibility, use of the keyboard can also be favored by certain users, and can have efficiency benefits.

General Guidelines
------------------

Follow the guidelines in this section on :ref:`shortcut keys <shortcut-keys>`, :ref:`access keys <access-keys>` and :ref:`keyboard navigation <keyboard-nav>`. In addition, follow the :doc:`design guidance for search </nav/search>`.

Every action that can be performed with a pointing device should also be possible with a keyboard. Trying to use your application with only a keyboard is a great way to test this. Most of the time, this is easy to acheive with the standard keyboard features described below. However, some operations  — like drag-and-drop — may require more thought.

Ensure that any text that can be selected with the mouse should also be selectable with the keyboard.

.. _shortcut-keys:

Shortcut Keys
-------------

The technical term for shortcut keys is *accelerators*. 

Use the :doc:`standard GNOME shortcut keys</reference/keyboard>` if your application supports those functions. This ensures consistency between GNOME applications and aids discoverability.

Shortcut keys should also be assigned to the most commonly-used actions in your application. However, don't assign shortcuts for everything.

When assigning non-standard shortcuts in your application:

* Try to use Ctrl in combination with a letter. Shift+Ctrl and a letter is the recommended pattern for shortcuts that reverse or extend another function. For example, Ctrl+Z is the shortcut for undo, and Shift+Ctrl+Z is the shortcut for redo.
* Shortcuts should be as mnemonic as possible, as this makes them easier to learn and remember. For example, Ctrl+E would be a good shortcut for an edit action.
* Do not use Alt for shortcut keys, as this may conflict with access keys.
* GNOME reserves the use of the Super key for use in system shortcuts. Super should therefore not be used by applications. Additional :ref:`legacy system shortcuts <legacy-shortcuts>` should also be avoided by apps.

.. _access-keys:

Access Keys
-----------

Access keys allow someone to operate labelled controls by holding Alt in combination with another key. These are indicated by an underlined letter within each control label (this is displayed when Alt is held down). As far as possible, all labelled components should have an access key.

The technical term for access keys is *mneumonics*.

Guidelines for selecting access keys:

* Choose access keys that are easy to remember. Normally this means using the first letter of the label. If the label has more than one word, the first letter of one of its other words can also be used. Additionally, if another letter provides a better association (for example: “x” in “Extra Large”) , consider using that letter instead.
* Avoid assigning access keys to “thin” letters (such as lowercase i or l), or letters with descenders (such as lowercase g or y), unless it is unavoidable. The underline is sometimes not as clear with these characters.
* If the choice of access keys is difficult, assign access keys to the most frequently-used controls first. If the first letter is not available, choose an easy to remember consonant from the label, for example, “p” in “Replace”. Only assign vowels once no consonants are available.
* Be aware that access keys have to be translated together with the strings that they are taken from, so even if there are no conflicts in your native language, they may occur in translations.
* Don't assign awkward reaches. Some people may only be able to use one hand on the keyboard, so shortcuts that can be easily used with one hand are preferable for common operations. (This guideline also applies to shortcuts.)

.. _keyboard-nav:

Keyboard Navigation
-------------------

It should be possible to move around and interact with every part of your user interface using the keyboard. 

This is primarily done with the tab key, which moves through each UI element in sequence. This keyboard focus sequence follows the internal widget tree, and therefore should generally be logical. However, you should test to make sure that the focus order is logical and traverses each UI element.

* When possible, play the alert sound when tab fails to move keyboard focus. For example, when the focus is on the first character in a text field and the user presses left arrow key, or the user tries to perform multiple selection in a single selection dialog. 
* Ensure that control labels immediately precede their control in the keyboard focus order. This will ensure that the access key you assign to the label will move focus to or activate the control.
* Where possible, arrow keys should allow moving around the UI in a directional fashion.

Standard Navigation Keys
~~~~~~~~~~~~~~~~~~~~~~~~

The following keys should automatically work for the majority of GNOME user interface elements. However, it is recommended to test to ensure that they do work correctly. Custom UI should support the standard navigation keys.

.. list-table::
  :widths: 10 90
  :header-rows: 1

  * - Keys
    - Function
  * - Tab
    - Move keyboard focus to the next control
  * - Shift+Tab
    - Move keyboard focus to the previous control
  * - Ctrl+Tab
    - Move keyboard focus to the next control, when Tab has another function (this is primarily relevant to text entries)
  * - Shift+Ctrl+Tab 
    - Move keyboard focus to the previous control, when Tab has another function
  * - Return
    - Activate the focused control or content item
  * - Space
    - Toggle the state of a control
  * - F10
    - Open primary or secondary menu 
  * - Menu / Shift+F10
    - Open context menu for focused location
  * - Esc
    - Close the current container, if it is transient (applies to menus, popovers and dialogs)