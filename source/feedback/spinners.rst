Spinners
========

Progress spinners are a common user interface element for indicating progress in a task. In contrast to progress bars, they only indicate that progress is taking place, and do not display the proportion of the task that has been completed.

When to use
-----------

A progress indication is generally needed whenever an operation takes more than around three seconds, and is necessary to indicate that an operation is really taking place. Otherwise, a user will be left in doubt whether an error has occurred.

At the same time, progress indications are a potential source of distraction, especially when displayed for short periods of time. If an operation takes less that 3 seconds, it is better to avoid using a progress spinner, since animated elements that are shown for a very short amount of time can detract from the overall user experience.

Spinners do not graphically show the degree of progress through a task, and are often better-suited for shorter operations. If the task is likely to take more than a minute, a :doc:`progress bar </feedback/progress-bars>` might be a better choice.

The shape of progress spinners also affects their appropriateness for different situations. Since they are effective at small sizes, spinners can be easily embedded in small user interface elements, like lists or header bars. Likewise, their shape means that they can be effective when embedded within square or rectangular containers. On the other hand, if vertical space is limited, a progress bar can be a better fit.

General guidelines
------------------

* If an operation can vary in how long it takes, use a timeout to only show a progress spinner after three seconds have elapsed. A progress indication is not needed for lengths of time below this.
* Place progress spinners close to or within the user interface elements they relate to. If a button triggers a long-running operation, the spinner can be placed next to that button, for example. When loading content, the spinner should be placed within the area where that content will appear.
* Generally, only one progress spinner should be displayed at once. Avoid showing a large number of spinners simultaneously — this will often be visually overwhelming.
* A label can be shown next to a spinner if it is helpful to clarify the task which a spinner relates to.
* If a spinner is displayed for a long time, a label can indicate both the identity of the task and progress through it. This can take the form of a percentage, an indication of the time remaining, or progress through sub-components of the task (e.g. modules downloaded, or pages exported).

API reference
-------------

* `GtkSpinner <https://developer.gnome.org/gtk3/stable/GtkSpinner.html>`_