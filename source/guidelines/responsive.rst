Scaling & Responsiveness
========================

TODO: this page needs to be rewritten.

Display Compatibility
---------------------

GNOME  supports a variety of device types, including desktops, laptops and convertibles. This requires that applications be compatible with displays that have different sizes and orientations.

The size requirements stated on this page should be doubled for high-resolution displays (those with greater than 96 PPI).

General Guidelines
~~~~~~~~~~~~~~~~~~

* It should be possible for all application windows to fit on the smallest recommended displays for GNOME. Currently, this is 1024×600 pixels.
* Ensure that your application works well in portrait orientation. The minimum recommended width for portrait mode is 768 pixels.
* All primary windows should be resizable. This ensures that transitions between landscape and portrait mode can be automatically handled by the window manager.
* Test to make sure that your interface works well on large displays. Where possible, scale content to make the best use of available space, or use fixed width layouts to ensure that interface elements maintain effective grouping and alignment.

Half-Screen Snap
----------------

GNOME allows windows to be snapped to occupy half the width of the display, allowing two windows to be used alongside each other. Half-screen snap is impractical on very small displays. As a rule of thumb, it should be supported on screens that are 1280 pixels or wider, meaning that windows should have a minimum width of no less than 640 pixels.

Since half-screen snap is only useful when windows are used in parallel, applications that are used in isolation do not need to support half-screen snap (a music player is a good example of this).