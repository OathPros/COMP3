Scaling & Responsiveness
========================

GNOME  supports a variety of device types, including desktops, laptops, convertibles and phones. Windows can also be used at a variety of sizes, and can sometimes be tiled alongside other windows.

The following guidelines should be followed to ensure that your app performs well in these varied conditions.

The size requirements stated on this page should be doubled for high-resolution displays (those with greater than 96 PPI).

Small Size Handling
-------------------

The smallest recommended displays for GNOME is currently 1024×600px, and this size should be supported by all applications. Apps that are appropriate for a phone form factor should scale down to a width of 340px.

In addition to physically fitting on small displays, app windows should be fully usable, and content should be fully visible and accessible.

Default and Large Size Handling
-------------------------------

The default size of app windows should be appropriate to their content. Windows that display large content like documents or videos should be suitably large to provide a good experience without the need to resize the window. On the other hand, windows with a limited amount of UI can and should default to a smaller size.

At large window sizes, avoid:

* related controls becoming physically distant
* lines of text becoming uncomfortably long
* visual structure like grids being lost.

The primary means to acheive this is by placing content within containers that have a maximum width. These can include both visible containers, like :doc:`lists </containers/lists>`, or invisible containers which act as a restraining frame.

:doc:`Flow boxes </containers/flow-boxes>` can be given a maximum number of columns, and will adjust their column width according to the overall grid width.

General Guidelines
------------------

* Remember to test your app design at a range of window sizes, both large and small. Consider portrait as well as landscape display orientation.
* All primary windows should be resizable.
* Some design patterns have specific guidance for responsive handling, such as :doc:`view switchers </nav/view-switchers>` and :doc:`sidebars </nav/sidebars>`.
* Following the GNOME design conventions for app structure and progressive disclosure will help to ensure that you app works well at a range of sizes. Windows that are sub-divided it a numerous small panes or panels will struggle to be responsive.