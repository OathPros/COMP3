UI Styling
==========

The visual style used for UI elements in GNOME is called Adwaita.

In general, visual styling is provided by the platform, so there is little need for designers or developers to manually set it. Indeed, developers are discouraged from defining their own UI styles, since this leads to incompatibilities with both Adwaita and high-contrast mode.

Style Options
-------------

Be default, UI elements in GNOME do not require their own styling. However, there are some limited cases where designers do need to make UI style decisions.

Optional Element Styles
~~~~~~~~~~~~~~~~~~~~~~~

In some individual cases, alternative visual styles are provided for specific elements. For example, the :ref:`suggested and destructive styles <button-styles>` make it possible to give buttons different colors depending on their function. In cases such as this, the HIG provides specific guidance for when and how to use the optional styles that are available.

Outside of these individual cases, it is not recommended to manually change the appearance of UI elements.

Dark UI Style
~~~~~~~~~~~~~

By default, GNOME apps have a light UI style. However, apps can choose to use a dark UI style instead. The dark style gets used in three ways:

#. Apps specify to use it by default, without an option to switch to the light style. This is recommended for apps which display rich visual content like images or video.
#. Apps provide a user setting to select the light or dark style. This is typically used for apps whose content can also be restyled, like code editors.
#. Users can opt to use the dark style for all apps in the system.

Apps specify the dark style using the `prefer dark theme GTK property <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/property.Settings.gtk-application-prefer-dark-theme.html>`_. Since any app can be used with the dark style, it is important to check that your app works well with it, irrespective of whether it uses the dark style itself. This can be done with `GTK Inspector <https://wiki.gnome.org/Projects/GTK/Inspector>`_.

Named Colors
~~~~~~~~~~~~

While the vast majority of UI elements have their own default styling which shouldn't be changed, in some cases it is necessary to select colors for backgrounds and borders. Here it is recommended to use named CSS colors from the Adwaita stylesheet, as opposed to specifying exact color values.

High-Contrast Mode
------------------

High-contrast mode is an accessibility feature which changes the UI style to have very high contrast. As part of testing your app, it is important to test it with high-contrast mode enabled, to ensure that it is correctly rendered with this style. This can be done by using the system high-contrast mode setting, or with `GTK Inspector <https://wiki.gnome.org/Projects/GTK/Inspector>`_.