Keyboard
========

Keyboard interaction covers a range of behaviors, including text entry, use of shortcuts, and search, through to the keyboard being used as the sole input device. The latter is vital for visually-impaired people or those with mobility impairments.

Every action that can be acheived with a pointing device should therefore also be possible with a keyboard. Trying to use your application with only a keyboard is a great way to test this.

The only exceptions to this are actions where fine motor control is an essential part of the task. For example, controlling movement in some types of action games, or freehand painting in an image-editing application.

Keyboard Navigation
-------------------

Make sure that it is possible to move around and interact with every part of your user interface using the keyboard:

* Tab should cycle keyboard focus through each UI element.
* Construct a logical keyboard navigation order for your UI. Keyboard focus should move between controls in a predictable order. In Western locales, this is normally left to right and top to bottom.
* In addition to Tab, where possible it should also be possible to move through a UI using the arrow keys, both within user interface elements (such as lists, icon grids or sidebars) and between them.

Note: if activating a control enables other controls, do not automatically give focus to the first dependent control when it is activated, but instead leave focus in place.

Standard Navigation Keys
------------------------

The following keys should automatically work for the majority of GNOME user interface elements. However, it is recommended to test to ensure that they do work correctly. Custom UI should support the standard navigation keys.

.. list-table::
  :widths: 10 90
  :header-rows: 1

  * - Keys
    - Function
  * - Tab
    - Move keyboard focus to the next control
  * - Shift+Tab
    - Move` keyboard focus to the previous control
  * - Ctrl+Tab
    - Move keyboard focus to the next control, when Tab has another function, or when controls are grouped
  * - Shift+Ctrl+Tab 
    - Move keyboard focus to the previous control, when Tab has another function, or when controls are grouped
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
  

.. _access-keys:

Access Keys
-----------

Access keys allow someone to operate labelled controls by holding Alt in combination with another key. These are indicated by an underlined letter within each control label (this is displayed when Alt is held down).

* Where possible, all labelled components should have an access key.
* Choose access keys that are easy to remember. Normally this means using the first letter of the label. If the label has more than one word, the first letter of one of its other words can also be used. Additionally, if another letter provides a better association (for example: “x” in “Extra Large”) , consider using that letter instead.
* Avoid assigning access keys to “thin” letters (such as lowercase i or l), or letters with descenders (such as lowercase g or y), unless it is unavoidable. The underline is sometimes not as clear with these characters.
* If the choice of access keys is difficult, assign access keys to the most frequently-used controls first. If the first letter is not available, choose an easy to remember consonant from the label, for example, “p” in “Replace”. Only assign vowels once no consonants are available.
* Be aware that access keys have to be translated together with the strings that they are taken from, so even if there are no conflicts in your native language, they may occur in translations.

.. _shortcut-keys:

Shortcut Keys
-------------

Use the :doc:`standard GNOME shortcut keys</reference/keyboard>` if your application supports those functions. This ensures consistency between GNOME applications and aids discoverability. Do not assign :doc:`system shortcut keys </reference/keyboard>` for use in your application.

When assigning shortcuts which are specific to your application:

* Assign shortcut keys to the most commonly-used actions in your application. However, do not try to assign a keyboard shortcut to everything.
* Try to use Ctrl in combination with a letter for your own shortcuts. Shift+Ctrl and a letter is the recommended pattern for shortcuts that reverse or extend another function. For example, Ctrl+Z and Shift+Ctrl+Z for undo and redo.
* Shortcuts should be as mnemonic as possible, as these will be easier to learn and remember. For example, Ctrl+E would be a good shortcut for a menu item called Edit Page.
* Shortcuts that can be easily used with one hand are preferable for common operations.
* Do not use Alt for shortcut keys, as this may conflict with access keys.

GNOME reserves the use of the Super key for use in system shortcuts. Super should therefore not be used by applications. Additional :ref:`legacy system shortcuts <legacy-shortcuts>` should also be avoided by apps.
