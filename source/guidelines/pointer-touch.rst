Pointer & Touch
===============

A pointing device is any input device that allows the manipulation of a pointer — typically represented as an arrow, and often called a cursor — on screen. While mice and touchpads are the most common, there are a wide variety of such devices, including graphics tablets, track balls, track points and joysticks.

General Guidelines
------------------

Designs ought to consider the range of common pointing devices, and be usable with all of them. This primarily includes mice, touchpads and touchscreens.

Ensure that click targets are large enough to be comfortably used with this range of devices. Also be careful to consider the range of physical abilities that users might have. Not everyone has lazer-like precision with a pointer.

Because your design should aim to be input device agnostic, specific input devices or input device buttons should not be referenced in user interfaces.

Primary & Secondary Actions
---------------------------

Pointing devices typically have two main buttons. Since the order of these buttons is user-configurable, these are referred to as the primary and secondary buttons, as opposed to left and right. These primary and secondary buttons are mapped to the primary and secondary actions.

The primary action actives, opens or selects. The secondary button is used to display additional actions for whatever is being pointed at. This is typically done through a context menu.

Guidelines for secondary actions:

* The secondary action should generally not be used for additional alternative actions, such as delete or remove.
* Only provide a context menu if there is a set of relevant menu items to expose. The secondary button does not always need to have an effect.
*  It should be possible to raise context menus without using a pointing device (see equivalent actions below as well as in the :doc:`keyboard guidelines <keyboard>`).

Pointer & Touch Equivalent Actions
----------------------------------

The following device equivalent actions are expected to work as described in all contexts. This will usually happen automatically.

Note: touchpads vary in their capabilities. Some have physical primary and secondary buttons. Some have "push to click". Some have click areas. Without these, "tap to click" behavior is required, and that is what is described below.

.. list-table::
  :widths: 10 30 30 30
  :header-rows: 1

  * - Operation
    - Mouse 
    - Touchpad
    - Touchscreen
  * - Primary action
    - Primary button
    - Tap*
    - Tap 
  * - Secondary action
    - Secondary button
    - Two-finger tap*
    - Long-press
  * - Drag
    - Hold primary button and move
    - Tap, then drag*
    - Tap, then drag

Scrolling, Zooming & Panning
----------------------------

Scrolling and panning are subtly different and require different pointer input handling.

Scrolling refers moving the view along a single axis, typically vertical. Panning refers to moving a plane in two dimensions. Scrolling is typical for web pages and documents, whereas panning is typical for viewing images or maps.

In the standard scrolling model, the following behaviors are expected for scroll and zoom:

.. list-table::
  :widths: 10 30 30 30
  :header-rows: 1

  * - Operation
    - Mouse 
    - Touchpad
    - Touchscreen 
  * - Scroll
    - Scroll wheel
    - Two-finger drag†‡
    - Single-finger drag‡
  * - Zoom
    - Ctrl+scroll wheel
    - Pinch
    - Pinch

However, when an app is focused on panning rather than scrolling, the opposite should be used:

.. list-table::
  :widths: 10 30 30 30
  :header-rows: 1

  * - Operation
    - Mouse 
    - Touchpad
    - Touchscreen 
  * - Pan
    - Drag
    - Tap, then drag†
    - Single-finger drag
  * - Zoom
    - Scroll wheel
    - Pinch
    - Pinch 

\* Requires tap to click to be enabled.

† Requires two-finger scrolling to be enabled.
    
‡ Along the axis to be scrolled.

Additional Guidelines
---------------------

* Double-click should be avoided, since it is undiscoverable, and translates poorly to touch input. Chording (pressing multiple buttons simultaneously) should also not be used.
* Pressing *Esc* while a pointer operation is in progress should cancel it. For example, while dragging and dropping a file or drawing a shape.
* In GNOME, three and four finger gestures are reserved for use by the system, and these should be avoided by applications. This includes both touchpad and touchscreen gestures. Drags from the top and bottom screen edges are also reserved.
* Apps are free to use two finger gestures as well as drags from the left and right screen edge.