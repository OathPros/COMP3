Sliders
=======

A slider allows the user to quickly select a value from a range.

When to use
-----------

Sliders can be used to either change a value, or for navigation within a content item, such as video, audio or even documents. Common uses include seeking through audio or video, changing a zoom or volume level, or setting values in image editors.

Use a slider when:

* The range of values is fixed and ordered, and when adjusting the value relative to its current value is more important than choosing an absolute value.
* It is useful for the user to control the rate of change of the value in real time.

If the range of values does not have a fixed maximum and/or minimum, a :doc:`spin button </controls/spin-buttons>` can be used.

Guidelines
----------

* Ensure that real time feedback is provided, in order to enable the user to make live adjustments. Examples of this include sound from speakers, indicating volume changes, or live feedback in an image editor.
* Take care to ensure that the purpose of a slider is clearly identified.
* In cases where it is common to use a slider, follow placement conventions. For example, in video players, it is common to situate a horizontal seek bar along the bottom of the window. Simply placing a slider in this position is enough to identify it.
* In other cases, label the slider with a text label above it or to its left, using :ref:`sentence capitalization <sentence-capitalization>`. Provide an :ref:`access key <access-keys>` in the label that allows the user to give focus directly to the slider.
* Mark significant values along the length of the slider with text or tick marks. For example the left, right and center points on an audio balance control in Figure 6-7.
* For large ranges of integers (more than about 20), and for ranges of floating point numbers, consider providing a :doc:`text field <text-fields>` or :doc:`spin button <spin-buttons>` that is linked to the slider’s value. This allows the user to quickly set or fine-tune the setting more easily than they could with the slider control alone.

API reference
-------------

* `GtkHSCale <https://developer.gnome.org/gtk3/stable/GtkHScale.html>`_
* `GtkVSCale <https://developer.gnome.org/gtk3/stable/GtkHScale.html>`_