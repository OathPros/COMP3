Sidebars
========

A sidebar allows switching between different views. A sidebar example can be seen in the *Flap* demo in the Adwaita demo app.

When to Use
-----------

Sidebars can be used when it is necessary to expose a larger number of views than can be accommodated in a standard :doc:`view switcher </nav/view-switchers>`.

Sidebars are particularly appropriate when navigating between content which is dynamic and/or suited to a list format (messaging apps are a good example of this). The are also suited to contexts where frequent switching back and forth between specific locations is common.

Sidebars should be avoided for apps which provide rich or immersive content. In this situation, the sidebar would be a distraction from application content.

Guidelines
----------

* Order the list according to what is most useful for the users of your application. It is often best to place recently updated items at the top of the list.
* Header bar controls which affect the sidebar list should be placed within the list pane section of the header bar. Controls for search and selection should be found above the list.
* Each list row can include multiple lines of text, as well as images. However, be careful to ensure that the most important information is not lost, and work to ensure a clean and attractive appearance.

TODO: guidelines on how to handle narrow window widths (leaflet and flap are relevant here).

API Reference
-------------

* GtkStackSidebar: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.StackSidebar.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkStackSidebar.html>`_