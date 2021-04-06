Checkboxes
==========

Check boxes are used to show or change a setting. Its two states, set and unset, are shown by the presence or absence of a checkmark in the labeled box.

Guidelines
----------

* Clicking a check box should not affect the values of any other controls. It may sensitize, insensitize, hide or show other controls, however.
* If toggling a check box affects the sensitivity of other controls, place the check box immediately above or to the left of the controls that it affects. This helps to indicate that the controls are dependent on the state of the check box.
* Use sentence capitalization (see see :ref:`sentence-capitalization`) for check box labels, for example *Use custom font*.
* Label check boxes to clearly indicate the effects of both their checked and unchecked states, for example, *Show icons in menus*. If the two states of a check box cannot be clearly communicated, consider using two radio buttons instead so both states can be given labels.
* Avoid negative check box labels, as this can be confusing and hard to understand. *Play alert sound* is better than *Disable alert sound*, for example.
* Provide an access key (see :ref:`access-keys` in all check box labels that allows the user to set or unset the check box directly from the keyboard.</p></item>
* If the check box represents a setting in a multiple selection that is set for some objects in the selection and unset for others, show the check box in its mixed state. When a check box is in its mixed state:
  * Clicking the box once should check the box, applying that setting (when confirmed) to all the selected objects.
  * Clicking the box a second time should uncheck the box, removing that setting (when confirmed) to all the selected objects.
  * Clicking the box a third time should return the box to its mixed state, restoring each selected object’s original value for that setting (when confirmed).
* Label a group of check boxes with a descriptive heading above or to the left of the group.
* Do not place more than about eight check boxes under the same group heading. If you need more than eight, try to use blank space or heading labels to divide them into smaller groups. Otherwise, consider using a check box list instead— but you probably also need to think about how to simplify your user interface.
* Try to align groups of check boxes vertically rather than horizontally, as this makes them easier to scan visually. Use horizontal or rectangular alignments only if they greatly improve the layout of the window.

API reference
-------------

* `GtkCheckButton <https://developer.gnome.org/gtk3/stable/GtkCheckButton.html>`_