Menus
=====

A menu is a list of actions and/or options which is revealed by pressing a heading or button. In the case of context menus, the menu is opened through a secondary action (such as secondary click with a mouse, or long press with a touch screen) on an item of content.

When to use
-----------

Menus can appear in various places, including primary and secondary menus, and context menus.

Size and structure
------------------

Menus should contain between three and 12 top-level items. If a menu contains more than 12 items, evaluate whether all the items are necessary and belong in the menu. If you are unable to reduce the size, submenus can be used. However, they should be avoided if at all possible, as they are physically difficult to use.

Submenus should contain between three and six items, and should never contain other submenus.

Organize similar menu items into groups using dividers — this will make them easier to understand and quicker to use. When creating groups:

* Order groups and group items logically, either by importance, task order, or expected frequency of use. Items at the top and bottom of the menu are more noticeable and easily targeted, so reserve these locations for particularly important or interesting functionality.
* Place single-item groups at the top or bottom of the menu, or group them together with other single items.
* Do not mix different types of menu item within each group — actions, check box and radio button items should be kept separate.

General guidelines
------------------

* Provide an access key (see :ref:`access-keys`) for every menu item. You may use the same access key on different menus in your application, but avoid duplicating access keys on the same menu. Note that unlike other controls, once a menu is displayed, its access keys may be used by just typing the letter; it is not necessary to press the Alt key at the same time.
* Label menu items with verbs for commands and adjectives for settings, using header capitalization (see :ref:`header-capitalization`).
* Use ellipses (see :ref:`ellipses`) when a menu item requires further input from the user to complete an action.
* Two linked actions can be combined into a single menu item, by changing the label when the item is selected. For example, a *Play* item may change to *Pause*. However, only use this type of item when actions are logical opposites which are obvious to users. Likewise, do not use this technique for settings — use check boxes or radio buttons instead.

Primary menus
-------------

Primary menus are a standard design pattern that is found in most applications. They are labelled with the menu icon (named <code>menu-open</code>) and contain the top-level menu items for the application. This can include standard items like *Preferences*, *Help* and *About Application*, as well as other application-specific items.

When to use
~~~~~~~~~~~

Most applications have primary menus, since they are the standard location for *About Application*, which every application is expected to have.

Guidance
~~~~~~~~

Primary menus are typically placed on the right side of the header bar. However, there are two variations on this rule:

* If the application incorporates in-window navigation, with a top-level location and sub-pages, the primary menu should only be placed on the top level: sub-pages can include a secondary menu, if a menu is required.
* When used in combination with a sidebar, the primary menu should be placed above the sidebar list on the right. If a menu is required for items shown in the content side of the window, a secondary menu can be used.

Other guidelines:

* Primary menus can contain items for both the current window or view, as well as the application as a whole. This differentiates them from secondary menus, which only contain menu items that relate to a specific view or item.

Standard menu items
~~~~~~~~~~~~~~~~~~~

The following are standard primary menu items, and should be placed in a group at the end of the menu:

.. list-table::
  :widths: 20 80
  :header-rows: 0

  * - Preferences
    - Opens the application's preferences dialog, if it has one.
  * - Keyboard Shortcuts
    - Opens the application's keyboard shortcuts window, if it has one.
  * - Help
    - Opens the application's user documentation in the Help application.
  * - About Application
    - Opens the application's about dialog. This item should include the application's name, such as About Photos or About Calculator. Every primary menu should include this item.

Primary menus shouldn’t include menu items for close or quit: windows can already be closed using the close button in the header bar, and it can be ambiguous as to what a close menu item refers to. Users don't readily differentiate between quit and close, and it can therefore be misleading.

Secondary menus
---------------

Secondary menus are located in the header bar and include menu items for the current view or content item. This differentiates them from primary menus, which include menu items that relate to an entire application (such as *Preferences* and *About "Name"*).

When to use
~~~~~~~~~~~

Secondary menus can be used to host controls that relate to a particular content item which is being displayed in the application window (such as a document, contact, conversation or photo). They are typically used in combination with in-window navigation or sidebars (see :doc:`/nav/sidebars`), since both these arrangements feature separate views or areas for content items to be shown.

Secondary menus are optional and only need to be used if there are enough controls to require a menu.

Guidance
~~~~~~~~

* Secondary menus generally shouldn't reproduce menu items that are included in primary menus, like *Preferences* and *About*. However, it can sometimes be useful to show *Help*.
* A secondary menu is contained within a popover. As such, a header bar menu can include a variety of controls, such as groups of buttons.
* Secondary menus shouldn’t include menu items for close or quit.

API reference
-------------

* `GtkMenu <https://developer.gnome.org/gtk3/stable/GtkMenu.html>`_
* `GtkPopoverMenu <https://developer.gnome.org/gtk3/stable/GtkPopoverMenu.html>`_