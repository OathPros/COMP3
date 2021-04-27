UI Icons
========

This page provides general guidance on the types of icons in use in GNOME apps, how to access them, and how to create them.

Icon Styles
-----------

Symbolic icons are the primary icon style in GNOME UI. They are simple and monochrome, and are designed to work well at smaller sizes.

Symbolics are defined at 16×16px and can be used at sizes of 16×16px, 32×32px and 64×64px. All or part of the icon can be programmatically recolored.

The other style of icon found in GNOME is the full-color icon style, which is primarily used for app icons. In some cases, these can be used for where icons are displayed at large sizes and are intended to be the focus of attention. File and folder icons in a file manager are one example of this.

Finding & Using UI Icons
------------------------

Where possible, it is recommended to reuse existing symbolic icons, as opposed to creating your own. There are two primary sources of pre-existing symbolic icons:

# Icons which are already included as part of GTK, and are therefore automatically available
# The icon dev kit, which includes a collection of icons which can be copy/pasted into your app

Both sources of symbolic icons included in the Icon Library app. This allows all the icons to be browsed and searched, and provides instructions for how to make use of each one.

Icon Usage Guidelines
---------------------

Only use icons which will be recognized by your users. This includes:

* Icons whose meaning is commonly recognized. This set of icons is actually quite small, and is dictated by convention. It includes standard icons such as search, menu, forward, back and share. If you are in doubt, only use icons which are frequently used in other applications.
* Icons will be meaningful in the specific context of your application — users of specialist tools will often be familiar with domain-specific symbols.

If users will not recognize an icon, it might be better to use a text label instead.

Some icons are only meaningful alongside other icons of the same type. For example, a media icon for stop is simply a square, and may not be identified as a stop icon without other media controls (like play, pause, or skip) being visible close by. Likewise, the icon to remove an item from a list is a subtract symbol (i.e. a single line), and will not be recognizable without a corresponding “plus” add icon.

As a general rule, controls should be identified with either a label or an icon, not both. This helps to avoid information overload and icon-overuse. However, there are some controls where both is required for practical reasons.

Symbolic Icon Creation
----------------------

If you require an icon that doesn't already exist, new ones can be defined as ``16×16`` SVGs. 

* When looking for an appropriate metaphor for an icon, identify a single property to communicate. For example, when describing an action to be performed on an image, it isn’t necessary to repeat the idea of an image in every icon. Instead, focus on what is distinct about each action (for example: rotate, tag, align).
* Avoid using any perspective in symbolic icons and stick to a simple orthogonal view.
* When using unfilled strokes for an outline, try avoiding hairline (``1px``) and use at least a ``2px`` stroke for the main feature of the icon.
* Symbolic icons are recolored at runtime to match the context, very much like a piece of text. While there are ways to “shade” parts of an icon by using opacity or creating duotone/pattern dithering, try avoiding these as much as possible.
* Ensure that any icons you create have a similar visual weight to existing symbolics.
* When a metaphor relies on negative space, make sure it will work with the colors inverted. For example a camera lens spec/highlight will only work if lighter than the lens itself:

.. image:: ../img/icons/hig-symbolic-inversion.svg

The `Symbolic Preview app <https://flathub.org/apps/details/org.gnome.design.SymbolicPreview>`_ is available to view and test icons that you have created.