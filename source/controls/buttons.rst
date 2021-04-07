Buttons
=======

Buttons are one of the most common and basic user interface elements. Buttons can be used to perform actions, toggle settings or views, activate tools, or to display dialogs, popovers, or other user interface elements.

General Guidelines
------------------

- A button can contain an icon, button, or — more unusually — an image. Follow the icons and artwork guidelines when deciding which to use.
- After pressing a button, the user should expect to see the result of their action within 1 second.
- Do not use more than one or two different widths of button in the same window, and make all of them the same height. This will help give a pleasing uniform visual appearance to your window that makes it easier to use.
- Do not assign actions to double-clicking or right-clicking a button. Users are unlikely to discover these actions, and if they do, it will distort their expectations of other buttons on the desktop.
- Make invalid buttons insensitive, rather than popping up an error message when the user clicks them.
- When several buttons are placed next to each other, ensure that they have the same width. This is particularly important for pairs of *Cancel* and *OK* buttons.
- In a dialog, one button may be made the default button, which is shown with a different border and is activated by pressing *Return*. Often this will be the OK or equivalent button. However, if pressing this button by mistake could cause a loss of data, do not set a default button for the window.

Text buttons
------------

- Label all buttons with imperative verbs, using header capitalization (see :ref:`header-capitalization`). For example, *Save*, *Sort* or *Update Now*.
- Use ellipses (see :ref:`ellipses`) when a button requires further input from the user to complete an action.
- Provide an access key (see :ref:`access-keys`) in the label that allows the user to directly activate the button from the keyboard.
- Keep labels short, so they don't cause a button to use too much space. It is also important to consider how labels will change length when localized.

Toggle buttons
--------------

Toggle buttons look the same as regular buttons, but are used to show or change a state rather than initiate an action. A toggle button’s two states, set and unset, are shown by its appearing “pushed in” or “popped out” respectively.

Linked buttons
--------------

Groups of buttons with a similar function can be grouped. This helps to communicate their similarity. Linking is a common technique for sets of toggle buttons.

.. _button-styles:

Suggested and destructive actions
---------------------------------

In cases where a button has a particularly important affirmative role, it can be given a suggested style. This highlights the button, and helps to distinguish it from other visible controls.

Buttons which have a destructive consequence, such as removing or deleting a content item, can be given a destructive style. This highlights the button by coloring it, and acts as a warning to the user.

Each view should only include a single suggested or destructive button.

API reference
-------------

- `GtkButton <https://developer.gnome.org/gtk3/stable/GtkButton.html>`_
- `GtkToggleButton <https://developer.gnome.org/gtk3/stable/GtkToggleButton.html>`_