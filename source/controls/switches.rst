Switches
========

.. image:: ../img/screenshots/switches.png

Switches can be used for controlling features, settings or hardware that have a clear on/off logic.

When to Use
-----------

Switches are strongly analogous to real-world controls, and this real-world correspondence can be used as a guide as to when a switch should be used. Ask yourself: "does this seem like something you'd use an actual switch for?"

On the whole, switches are preferred to :doc:`check boxes <checkboxes>`, since they offer a larger click target, often fit modern UI layouts better, and are more action orientated. However, check boxes may still be used if a switch doesn't seem appropriate.

Only use a switch to control options that have a clear binary nature. If the switch label cannot adequately what both states of the control do, a :doc:`radio button <radio-buttons>` may be a better choice.

General Guidelines
------------------

* Label switches using nouns in :ref:`header capitalization <header-capitalization>`. For example, *Automatic Location* or *Notifications*.
*  Give the label an access key to allow users to focus the control using a keyboard.

Switch States
-------------

Switches indicate the user-specified state through the switch position and the actual state of the thing that they control through their background color. These two indications can be used independently, to communicate when a service or feature has been switched to on, but has not yet responded.

This technique can be particularly useful when there's a delay between the switch being toggled and it having an effect. However, if a feature has been disabled or is unavailable, it is better to make the switch insensitive, since this avoids the suggestion that the service ought to respond to user action.

API Reference
-------------

* GtkSwitch: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.Switch.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkSwitch.html>`_
