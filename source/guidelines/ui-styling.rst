UI Styling
==========

The visual style used for UI elements in GNOME is called Adwaita.

In general, the visual styling of UI elements is provided by the platform, so there is little need for designers or developers to manually set it. Indeed, developers are discouraged from defining their own UI styles, since this leads to incompatibilities with both Adwaita and high-contrast mode.

Style Options
-------------

UI elements do not generally require their own styling. However, there are some cases where designers do need to make UI style decisions.

Optional Element Styles
~~~~~~~~~~~~~~~~~~~~~~~

Alternative visual styles are available for some UI elements. For example, the :ref:`suggested and destructive styles <button-styles>` make it possible to give buttons different colors depending on their function. In cases such as this, the HIG provides specific guidance for when and how to use the optional styles that are available.

Outside of these individual cases, it is not recommended to manually change the appearance of UI elements.

Dark UI Style
~~~~~~~~~~~~~

By default, GNOME apps have a light UI style. However, apps can choose to use a dark UI style instead. The dark style can be used in three ways:

#. Apps can specify to use it by default, without an option to switch to the light style. This is recommended for apps which display rich visual content like images or video.
#. Apps can include a user setting to select the light or dark style. This is typically used for apps whose content can also be restyled, like code editors.
#. Users can opt to use the dark style for all apps in the system.

Apps specify the dark style using the `prefer dark theme GTK property <https://docs.gtk.org/gtk4/property.Settings.gtk-application-prefer-dark-theme.html>`_. Since any app can be used with the dark style, it is important to check that your app works well with it, irrespective of whether it uses the dark style itself. `GTK Inspector <https://wiki.gnome.org/Projects/GTK/Inspector>`_ can be used to change the style of an app to dark, for testing.

Named Colors
~~~~~~~~~~~~

While the vast majority of UI elements have their own default styling which shouldn't be changed, in some cases it is necessary to select colors for backgrounds and borders. Here it is recommended to use named CSS colors from the Adwaita stylesheet, as opposed to specifying exact color values (this can interfere with accessibility features).

High-Contrast Mode
------------------

High-contrast mode is an accessibility feature which changes the UI style to have very high contrast. As part of testing your app, it is important to test it with high-contrast mode enabled, to ensure that it is correctly rendered with this style. This can be done by using the system high-contrast mode setting, or with `GTK Inspector <https://wiki.gnome.org/Projects/GTK/Inspector>`_.

Accessibility Considerations
----------------------------

When creating custom UI elements, there are a number of accessibility issues to avoid regarding visual styling:

* Using color as the only means to distinguish items of information. Instead, all information should be provided by at least one other method, such as shape, position or text description.
* The use of flashing or blinking elements, as this may cause problems for people who are susceptible to visually-induced seizures.
