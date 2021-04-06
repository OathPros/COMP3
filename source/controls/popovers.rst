Popovers
========

A popover is a transient container that appears over its parent window in response to a user action. Popovers can contain a variety of UI elements, including buttons, lists or menus. They are often used as a part of button menus or context menus.

When to use
-----------

Popovers can be used to reveal additional controls that are not always needed by the user. They can can allow the user to take actions or they can contain settings and preferences. They are a very flexible interface element that lend themselves to creative design solutions.

A popover should always relate to a specific interface element which acts as the source of the popover. Typically, this is either a button or a content item. When they are triggered by a button, a popover can be used as a more flexible version of a button menu, allowing groups of controls to be accessed when needed. Examples of this include:

* Revealing a small toolbox of text formatting controls.
* A find interface, with a search entry box and a space for a list of results.
* A collection of view controls, such as zoom, list/grid and content ordering.

As a mechanism for disclosing additional controls or information, popovers are similar to dialog windows (see :doc:`/containers/dialogs`). Their main advantage over dialogs is that they are less disruptive and have a close relationship with a single element which the popover points to. However, you should still consider using a dialog if you want to display large amounts of information, or more complex arrangements of controls, or if the situation requires one of the common conventions for dialog usage, such as a confirmation dialog.

Popover content
---------------

* A popover is a generic container, and can include a wide variety of controls, such as buttons, sliders, lists, switches and text fields. However, don’t mix too many different types of control within the same popover, and try to group controls of the same type together.
* Popovers can function as a container for a menu, or for a menu in combination with a small number of supplementary controls.
* If the purpose of a popover’s controls is ambiguous, the popover can be given a heading.
* Close or Done buttons are not usually required in a popover.

General guidelines
------------------

* Popovers should always be small in size (as a rule of thumb, they should not cover more than a third of their parent window) and low in complexity. They should always appear as subordinates to their parent windows.
* A popover should only ever appear in response to a user action, and should never appear in a surprising or unintended manner.

API reference
-------------

* `GtkPopover <https://developer.gnome.org/gtk3/stable/GtkPopover.html>`_
* `GtkPopoverMenu <https://developer.gnome.org/gtk3/stable/GtkPopoverMenu.html>`_