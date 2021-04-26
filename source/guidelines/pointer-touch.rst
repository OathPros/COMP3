Pointer & Touch
===============

A pointing device is any input device that allows the manipulation of a pointer — typically represented as an arrow, and often called a cursor — on screen. While mice and touchpads are the most common, there are a wide variety of such devices, including graphics tablets, track balls, track points and joysticks.

While there is no visible pointer with a touchscreen, it fulfills the same role as other pointing devices.

General Guidelines
------------------

User interface designs should generally aim to accommodate the full range of common pointing devices, and be usable with all of them. This primarily includes mice, touchpads and touchscreens. They should also be suited to the range of physical abilities that users might have. Not everyone has lazer-like precision with a pointer.

* Click targets should be large enough to be comfortably used with different pointing devices and physical abilities.
* Buttons and controls which are only available on some pointing devices should not be exclusively relied upon for particular actions.
* Actions which are physically challenging to accomplish, such as double-clicking or chording (pressing multiple buttons simultaneously), should be avoided.
* All actions which can be accomplished with a pointing device should also be possible with a :doc:`keyboard <keyboard>`.
* Because designs should generally be input device agnostic, specific input devices or input device buttons should not be referenced in user interfaces. For example, text should not instruct users to "move the mouse" or "tap".

Some types of apps have specialist input devices associated with them, and therefore may need to ignore some or all of these general guidelines. For example, games might provide features that are specific to games controllers, or graphics apps might target graphics tablets. If an app requires a specific type of device in order to be used, this expectation should be clearly communicated to the user.

Primary & Secondary Actions
---------------------------

Mice and many touchpads have a primary and a secondary button. While the default order of the buttons is to have the primary button on the left, this order is user-configurable. Hence, the terms primary and secondary buttons are used.

While not all pointer and touch devices have primary and secondary buttons, they do have equivalents. The primary action activates, opens or selects. The secondary action should display additional actions for whatever is being pointed at, typically through a context menu.

Secondary actions should:

* not be used for additional alternative actions, such as delete or remove
* only provide a context menu if there is a set of relevant menu items to expose
*  be possible without using a pointing device: see equivalent actions for :doc:`keyboard <keyboard>`.

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

Scrolling, Panning & Zooming
----------------------------

Scrolling moves a view along a single (typically vertical) axis, whereas panning can move the view along two axes. For example, scrolling is typical for web pages and documents, whereas panning is typical for viewing images or maps.

Input handling conventions for scolling, panning and zooming vary according to whether the view is focused on scrolling or panning, as determined by the content type. For scrolling, the following behaviors are expected for scroll and zoom:

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

However, when an app is focused on panning rather than scrolling, the following should be used:

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

* Pressing *Esc* while a pointer operation is in progress should cancel it. For example, while dragging and dropping a file or drawing a shape.
* In GNOME, three and four finger gestures are reserved for use by the system, and these should be avoided by applications. This includes both touchpad and touchscreen gestures. Drags from the top and bottom screen edges are also reserved.
* Apps are free to use two finger gestures as well as drags from the left and right screen edge.