Tabs
====

Tabs allow a window to contain a mutable set of content items, such as pages, documents or images. They are primarily used as part of editor or browser applications.

An example of tabs can be seen in the *Tab View* demo in the LibHandy demo app.

Guidelines
----------

* Where possible, ensure that tab labels are short and concise, and that the most useful part of the label is displayed first. This ensures that the label continues to be useful even when ellipsized.
* If the content of a tab changes or requires attention, a visual hint can be displayed.
* Provide a context menu on each tab. This menu should only include actions for manipulating the tab itself, such as *Move Left*, *Move Right*, *Move to New Window*, and *Close*.
* The presence of the tab can vary according to the role of tabs in the application: the tab bar can always be shown, or it can be hidden until there is more than one tab.

Standard Keyboard Shortcuts
---------------------------

When using dynamic tabs, ensure that the standard keyboard shortcuts are supported.

.. list-table::
  :widths: 30 70
  :header-rows: 0

  * - Ctrl+T
    - Create a new tab
  * - Ctrl+W
    - Close the current tab
  * - Ctrl+Page Up
    - Switch to the next tab
  * - Ctrl+PageDown
    - Switch to the previous tab

API reference
-------------

* `HdyTabBar <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyTabBar.html>`_
* `HdyTabView <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyTabView.html>`_