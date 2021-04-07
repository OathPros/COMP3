Radio Buttons
=============

Radio buttons are used in groups to select from a mutually exclusive set of options. Only one radio button within a group may be set at any one time. As with check boxes, do not use radio buttons to initiate actions.

Guidelines
----------

* Only use radio buttons in groups of at least two, never use a single radio button on its own. To represent a single setting, use a check box or two radio buttons, one for each state.
* Exactly one radio button should be set in the group at all times. The only exception is when the group is showing the properties of a multiple selection, when one or more of the buttons may be in their mixed state.
* Clicking a radio button should not affect the values of any other controls. It may sensitize, insensitize, hide or show other controls, however.
* If toggling a radio button affects the sensitivity of other controls, place the radio button immediately to the left of the controls that it affects. This helps to indicate that the controls are dependent on the state of the radio button.
* Use sentence capitalization (see :ref:`sentence-capitalization`) for radio button labels, for example *Switched movement*. Provide an access key (see :ref:`access-keys`) in the label that allows the user to set the radio button directly from the keyboard.
* If the radio button represents a setting in a multiple selection that is set for some objects in the selection and unset for others, show the radio button in its mixed state.
* Do not place more than about eight radio buttons under the same group heading. If you need more than eight, consider using a single-selection list instead— but you probably also need to think about how to simplify your user interface.
* Try to align groups of radio buttons vertically rather than horizontally, as this makes them easier to scan visually. Use horizontal or rectangular alignments only if they greatly improve the layout of the window.

API reference
-------------

* `GtkRadioButton <https://developer.gnome.org/gtk3/stable/GtkRadioButton.html>`_