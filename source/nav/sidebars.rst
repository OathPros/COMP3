Sidebars
========

A sidebar list allows switching between different views. In GNOME, the sidebar divides the window in two, with content being shown on the opposite pane to the sidebar.

A sidebar example can be seen in the *Flap* demo in the LibAdwaita demo app.

When to Use
-----------

Use a sidebar list when it is necessary to expose a larger number of views than can be accommodated in a standard :doc:`view switcher </nav/view-switchers>`. Sidebar lists also provide a possible alternative to browser-style navigation.

Sidebars are particularly appropriate when navigating between content which is both dynamic and is suited to a list format. Messaging apps are a good example of this.

The are also suited to contexts where frequent switching back and forth between specific locations is common.

Sidebars should be avoided for apps which provide rich or immersive content. In this situation, the sidebar would be a distraction from application content.

Guidelines
----------

* Order the list according to what is most useful for the users of your application. It is often best to place recently updated items at the top of the list.
* Header bar controls which affect the sidebar list should be placed within the list pane section of the header bar. Controls for search and selection should be found above the list.
* Each list row can include multiple lines of text, as well as images. However, be careful to ensure that the most important information is not lost, and work to ensure a clean and attractive appearance.

API Reference
-------------

* `AdwFlap <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/AdwFlap.html>`_
* `HdyFlap <https://gnome.pages.gitlab.gnome.org/libhandy/doc/1-latest/HdyFlap.html>`_
* GtkStackSidebar: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.StackSidebar.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkStackSidebar.html>`_