Spin Buttons
============

A spin button is a text field that accepts a range of values. It incorporates two buttons that allow the user to increase or decrease the value by a fixed amount.

When to use
-----------

Use spin boxes to allow users to select numeric values, but only when those values are meaningful or useful for users to know. If they aren't, a :doc:`slider </controls/sliders>` might be a better choice.

Use spin boxes for numerical input only. For non-numeric sets of options, a list can be used instead.

Sliders
-------

In some cases, it is appropriate to link a spin button with a slider. This combination allows both approximate control and the entry of specific values. However, it is only useful if you want to cater to people who may know a specific value that they want to use. Use a slider when:

* Immediate feedback for changes in the spin box’s value is possible (such as in the case of image editing).
* It is useful for the user to control the rate of change of the value in real time. For example, to monitor the effects of a color change in a live preview window as they drag the RGB sliders.

General guidelines
------------------

* Label the spin box with a text label above it or to its left, using sentence capitalization. Provide an access key in the label that allows the user to give focus directly to the spin box.
* Right-justify the contents of spin boxes, unless the convention in the user’s locale demands otherwise. This is useful in windows where the user might want to compare two numerical values in the same column of controls. In this case, ensure the right edges of the relevant controls are also aligned.

API reference
-------------

- `GtkSpinButton <https://developer.gnome.org/gtk3/stable/GtkSpinButton.html>`_