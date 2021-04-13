Buttons
=======

Buttons are one of the most common and basic user interface elements.

General guidelines
------------------

- Typically, a button contains either an icon or a label. Buttons shouldn't contain both.
- Do not use more than one or two different widths of button in the same window, and ensure that buttons placed next to each other have the same width. This will give a better appearance.
- Do not assign actions to double-clicking or right-clicking a button. Users are unlikely to discover these actions, and if they do, it will distort their expectations of other buttons.
- Make invalid buttons insensitive, rather than showing an error message when the user clicks them.
- Button labels should follow the :doc:`writing style guidelines</guidelines/writing-style>`. In addition:
   - Button labels should use imperative verbs, using :ref:`header capitalization <header-capitalization>`. For example, *Save* or *Update*.
   - Button labels should be short, so they don't cause a button to use too much space. Consider how labels will change length when localized.

Toggle buttons
--------------

Toggle buttons switch between two states, set and unset, which is indicated by the button being either “pushed in” or “popped out” respectively.

Toggle buttons are an appropriate choice for modes or settings which have an obvious binary nature. They are generally used when space is limited.

Linked buttons
--------------

Groups of buttons with a similar function can be grouped. This helps to communicate their similarity. Linking is a common technique for sets of toggle buttons.

.. _button-styles:

Suggested and destructive actions
---------------------------------

The suggested and destructive styles are available to highlight buttons in some situations.

* ``suggested-action`` can be used when a button has an important affirmative role. The highlights the button in order to recommend and draw attention to it.
* ``destructive-action`` can be used to draw attention to the potentially damaging consequences of using a button. This style acts as a warning to the user.

Each view should only include a single suggested or destructive button.

API reference
-------------

* GtkButton: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.Button.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkButton.html>`_
* GtkToggleButton: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ToggleButton.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkToggleButton.html>`_