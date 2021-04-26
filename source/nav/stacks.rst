Stacks
======

A stack consists of a grid or list of items, each of which can be opened to show a dedicated view. A back button allows navigated from an individual item back to the stack.

An example of a stack might be to a grid of videos, where opening an item switches to a dedicated view of the video.

Guidelines
----------

* Avoid nesting stacks. They should generally only have one level of depth.
* As the view changes, update the :doc:`header bar </containers/header-bars>` to reflect what is being shown. This can include changing the controls, the heading, and switching between a primary and secondary menu (see :doc:`menus </controls/menus>`).
* If :doc:`search <search>` is provided, it should remain available irrespective of the view that is displayed.
* Support the :ref:`standard keyboard shortcuts for navigation <navigation-shortcuts>`.
* When in a sub-view, a back button should be shown at the start of the header bar (in left-to-right locales, on the far left).
* Stacks can be combined with other navigation patterns. For example, a top-level :doc:`view switcher <view-switchers>` can contain stacks for each view.