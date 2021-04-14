Pointer & Touch Input
=====================

A pointing device is any input device that allows the manipulation of a pointer — typically represented as an arrow, and often called a cursor — on screen. While mice and touchpads are the most common, there are a wide variety of such devices, including graphics tablets, track balls, track points and joysticks.

Touch input primarily refers to touchscreens.

Pointer Input
-------------

Primary & Secondary Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mice and touchpads often have two main buttons. One of these acts as the primary button, and the other acts as the secondary button. Typically, the left button is used as the primary button and the right button is used as the secondary button. However, this order is user-configurable. These guidelines therefore refer to primary and secondary action, rather than left and right.

The primary button is used for selecting items and activating controls. The secondary button is for additional options, typically through a context menu.

Do not depend on input from secondary or other additional buttons. As well as being physically more difficult to click, some pointing devices and many assistive technology devices only support or emulate the primary button.

Press and hold should be used to simulate the secondary button on single button pointing devices. Therefore, do not use press and hold for other purposes.

General Guidelines
~~~~~~~~~~~~~~~~~~

* Double click should not be used, since it is undiscoverable, and translates poorly to touch input.
* Do not require the use of chording (pressing multiple mouse buttons simultaneously) for any operations.
* Do not require the use of multiple (triple- or quadruple-) clicking actions for any operations, unless you also provide an accessible alternative method of performing the same action.
* Allow all mouse operations to be cancelled before their completion. Pressing *Esc* should cancel any mouse operation in progress, such as dragging and dropping a file in a file manager, or drawing a shape in a drawing application.
* Do not refer to particular mouse buttons in your interface unless absolutely necessary. Not everybody will be using a conventional mouse with left, middle and right buttons, so any text or diagrams that refer to those may be confusing.

Touch Input
-----------

The following touchscreen conventions are recommended, where relevant.

.. list-table::
  :widths: 20 40 40
  :header-rows: 1

  * - Input
    - Description
    - Action
  * - Tap
    - Tap on an item.
    - Primary action. Item opens — photo is shown full size, application launches, song starts playing.
  * - Press and hold
    - Press and hold for a second or two.
    - Secondary action. Select the item and list actions that can be performed.
  * - Drag
    - Slide finger touching the surface.
    - Scrolls area on screen.
  * - Pinch or stretch
    - Touch surface with two fingers while bringing them closer or further apart.
    - Changes the zoom level of the view (e.g. Maps, Photos).
  * - Double tap
    - Tap twice in quick succession.
    - Stepped zoom in.
  * - Flick
    - Very quick drag, losing contact with the surface without slowing movement.
    - Removes an item.

System Touch Conventions
~~~~~~~~~~~~~~~~~~~~~~~~

In GNOME, a number of touch gestures are reserved for use by the system. These should be avoided by applications.

.. list-table::
  :widths: 20 40 40
  :header-rows: 1

  * - Input
    - Description
    - Action
  * - Edge drag, top-left
    - Slide finger starting from a screen edge.
    - Top-left edge opens the application menu.
  * - Edge drag, top-right
    - Top-right edge opens the system status menu.
    - Left edge opens the Activities Overview with the application view visible.
  * - Three finger pinch
    - Bring three or more fingers closer together while touching the surface.
    - Opens the Activities Overview.
  * - Four finger drag
    - Drag up or down with four fingers touching the surface.
    - Switches workspace.
  * - Three finger hold and tap
    - Hold three fingers on the surface while tapping with the fourth.
    - Switches application.