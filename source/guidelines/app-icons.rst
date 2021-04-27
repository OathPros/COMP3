App Icons
=========

In addition to having a :doc:`great name <app-naming>`, every app also needs a great icon. This page provides guidance on how to create one.

Typically creating an app icon requires prexisting visual design skills, and these guidelines are intended for those who are already able to create graphics. However, GNOME app icons are deliberately simple in style, in order to make icon creation as accessible as possible.

Icon Size
---------

The nominal size of full-color icons is ``128×128px``. However, because application icons are sometimes presented at lower resolutions, they should only feature detail that is presentable at ``64×64px`` resolution: anything more detailed would get lost by filtering/scaling down.

.. image:: ../img/icons/hig-icon-sizes.svg

The `full-color icon template <https://gitlab.gnome.org/Community/Design/HIG-app-icons/blob/master/template.svg>`_ includes a 2px grid which should help you avoid adding detail that's finer than the desired threshold.

Perspective & Shape
-------------------

Full-color icons should be rendered with a simple orthogonal view and no real or isometric perspective. To provide depth a raised effect can be applied to mimic the Z-axis. Please keep the effect subtle though! Raising the object more than `2 detail units` (`4 nominal pixels`) is not recommended.

In order to aid recognition, each application icon should have a unique silhouette. However, to ensure visual balance with other application icons, the aspect ratio should not be extreme. Very narrow or very wide shapes should be avoided.

A `grid template <https://gitlab.gnome.org/Community/Design/HIG-app-icons/raw/master/template.svg>`_ is available to assist with placing your icon outline. Do not try to cover a maximum area of the canvas: the outside margin should be left empty. In some circumstances a small detail can be extended into this margin space.

Shadows
-------

Shadows can be drawn internally, within a full-color icon, with the light source pointing straight from above. However, shadows should not be drawn outside the main silhouette of the icon, as these are generated programmatically based on the context. When app icons are presented on a white background, for example, a strong drop shadow is rendered to help define the contours.

.. image:: ../img/icons/scr-app-icon-preview.png

It is highly recommended to use the `App Icon Preview <https://flathub.org/apps/details/org.gnome.design.AppIconPreview>`_ app as it provides you with a complete workflow designing the app icon. From the up-to-date template to previewing the proper sizing and color in the context of other app icons, with properly generated drop shadow, up to generating optimized versions of the stable and development variants of the icon.

Palette
-------

Below is the baseline GNOME app icon color palette.

.. image:: ../img/icons/hig-colors.svg

You are free to use different shades of these colors depending on the desired material effect. However, these primary colors are a good baseline to start from.

It is recommended to keep flat surfaces unshaded, but using gradients to signify bent surfaces is allowed.

How to access the palette:

* Use the `Palette app <https://flathub.org/apps/details/org.gnome.design.Palette>`_ to copy the hexadecimal color codes.
* Recent versions of GIMP and Inkscape include the palette by default. (Alternatively, `the palette can be downloaded <https://gitlab.gnome.org/Teams/Design/HIG-app-icons/raw/master/GNOME%20HIG.gpl?inline=false>`_ in GIMP/Inscape format.)