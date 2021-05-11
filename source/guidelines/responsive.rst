Scaling & Responsiveness
========================

GNOME  supports a variety of device types, including desktops, laptops, convertibles and phones. Just on the desktop, windows can also be used at a variety of sizes, and can sometimes be tiled alongside other windows. It is therefore important to ensure that app windows look and perform well at a range of sizes.

The :doc:`page on windows </containers/windows>` includes additional guidance that is relevant to this topic.

Small Size Handling
-------------------

The smallest recommended displays for GNOME is currently 1024×600px, and this size should be supported by all applications. Apps that are appropriate for a phone form factor should scale down to a width of 340px.

These size requirements should be doubled for high-resolution displays (those with greater than 96 PPI).

Large Size Handling
-------------------

Large window sizes can present a number of challenges, including:

* related controls becoming physically distant
* lines of text becoming uncomfortably long
* visual structure like grids being lost

To avoid these issues, place content within containers that have a maximum width. These can include both visible containers, like :doc:`lists </containers/lists>`, or invisible containers which act as a restraining frame.

:doc:`Flow boxes </containers/flow-boxes>` can be given a maximum number of columns, and will adjust their column width according to the overall grid width.

General Guidelines
------------------

* Remember to test your app design at a range of window sizes, both large and small. Consider portrait as well as landscape display orientation.
* Some design patterns have specific guidance for responsive handling, such as :doc:`view switchers </nav/view-switchers>` and :doc:`sidebars </nav/sidebars>`.
* Following the GNOME design conventions for app structure and progressive disclosure will help to ensure that your app works well at a range of sizes. Windows that are sub-divided it a numerous small panes or panels will struggle to be responsive.