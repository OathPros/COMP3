Menus
=====

Standard menus in GNOME include primary, secondary and context menus.

Primary menus
-------------

Primary menus are a standard design pattern. Most applications have primary menus, since they are the standard location for the about dialog, which every application is expected to have.

Primary menus are labelled with the menu icon (named ``menu-open``).

Primary menus are typically placed on the right side of the header bar. However, there are two variations on this rule:

* If the application incorporates in-window navigation, with a top-level location and sub-pages, the primary menu should only be placed on the top level: sub-pages can include a secondary menu, if a menu is required.
* When used in combination with a sidebar, the primary menu should be placed above the sidebar list on the right. If a menu is required for items shown in the content side of the window, a secondary menu can be used.

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

Secondary menus are located in the header bar and include menu items for the current view or content item (such as a document, contact, conversation or photo). This differentiates them from primary menus, which include menu items that relate to an entire application (such as *Preferences* and *About*).

Secondary menus:

* Are typically used in combination with in-window navigation or sidebars (see :doc:`/nav/sidebars`), since both these arrangements feature separate views or areas for content items to be shown.
* Are optional and only need to be used if there are enough controls to require a menu.
* Generally shouldn't reproduce menu items that are included in primary menus, like *Preferences* and *About*.

General guidelines
------------------

The following guidelines apply to all menus.

Menu items
~~~~~~~~~~

* Label menu items with verbs for commands and adjectives for settings, using :ref:`header capitalization <header-capitalization>`.
* Two linked actions can be combined into a single menu item, by changing the label when the item is selected. For example, a *Play* item may change to *Pause*. However, only use this type of item when actions are logical opposites which are obvious to users. Likewise, do not use this technique for settings — use check boxes or radio buttons instead.
* Provide an :ref:`access key <access-keys>` for every menu item. You may use the same access key on different menus in your application, but avoid duplicating access keys on the same menu.

Menu size and structure
~~~~~~~~~~~~~~~~~~~~~~~

* Menus should contain between three and 12 top-level items, and submenus should contain between three and six items.
* Don't nest submenus, since nesting can be difficult to use ergonomically, as well as being hard to navigate.
* Organize similar menu items into groups using dividers — this will make them easier to understand and quicker to use. When creating groups:
   * Order groups and group items logically, either by importance, task order, or expected frequency of use. Items at the top and bottom of the menu are more noticeable and easily targeted, so reserve these locations for particularly important or interesting functionality.
   * Place single-item groups at the top or bottom of the menu, or group them together with other single items.
   * Do not mix different types of menu item within each group — actions, check box and radio button items should be kept separate.

API reference
-------------

* GtkPopoverMenu:  `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.PopoverMenu.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkPopoverMenu.html>`_