Switches
========

A switch is a simple interface element which has an on and off state.

When to use
-----------

Switches should be used for controlling services or hardware that have a clear on/off logic. They are particularly appropriate when those services or hardware do not activate immediately (i.e. there is a delay between the switch being operated and it having an effect), or when they affect the operation of the application in a significant way.

When the control does not turn a function on or off, or when a function does not clearly have an on/off nature, a :doc:`check box <check-boxes>` is a more appropriate option. For example, an alarm might be controlled using a switch, since it can be turned on or off. However, a check box is a better choice for an option to repeat that alarm on a daily basis, since alarm repetition is a configuration option, rather than starting or stopping a particular piece of functionality.

When in doubt, use switches for important configuration options, and check boxes for minor sub-options.

Switch labels
-------------

Switch labels should be written using :ref:`header capitalization <header-capitalization>`. The name of the function affected by the switch should be used as the label. *Automatic Location* or *Notifications* are examples of good switch labels.

API reference
-------------

* `GtkSwitch <https://developer.gnome.org/gtk3/stable/GtkSwitch.html>`_