Progress Bars
=============

.. image:: /img/screenshots/progress-bars.png

Progress bars indicate progress on a task. Unlike :doc:`spinners <spinners>`, they can indicate the proportion of the task that has been completed, as well as the time remaining.

Progress bars are most appropriate for indicating the progress of tasks that take a relatively long time (as a rule of thumb, tasks that take over 30 seconds). For tasks that have shorter periods, spinners are often a better choice.

Indicating Progress
-------------------

The bar of a progress bar should indicate progress in terms of the amount of time required for the task, as well as the amount of time remaining.

Ideally, the remaining time should be calculated accurately. However, if this is not possible, then the remaining time can be estimated. Here, overestimation can be handled by having progress pause at 100%, and showing explanatory text such as “Almost done”, and underestimation can be handled by having progress skip ahead as necessary.

If it is impossible to calculate remaining time, either accurately or estimated, then a progress bar can be set to activity mode, which causes it to move back and forth without indicating progress. Activity mode should be avoided wherever possible, particularly for long periods of time. However, it can sometimes be necessary for multi-stage tasks (see below).

Progress Text
-------------

Progress text should describe how much of the task has been completed. For shorter tasks, this can be expressed using units which are appropriate to the task. For example, “13 of 19 images rotated” or “12.1 of 30 MB downloaded”.

For long-running tasks, it can be desirable to show an estimate of the time remaining, either on its own, or with supplementary progress information. If the time remaining is an estimate, use the word “about“. For example, “About 3 minutes left”.

Task Stages
-----------

Some tasks can be made up of a series of stages, each of which has its own time estimation. In these situations, try to create a a single composite calculation of progress for the entire task. Only communicate the different stages in a task when they are relevant to a user.

In some cases, it is possible to calculate or estimate the time remaining for part of a task, but not another part. In this situation, a progress bar can enter activity mode for part of the task. However, it is best not to show activity mode for long periods of time, and the number of progress bar mode changes should be kept to an absolute minimum.

Subtasks
---------

Some tasks are comprised of multiple simultaneous subtasks (such as downloading several files at the same time). Here, it is generally advisable to show a single progress bar which indicates composite progress for the overall task.

In rare cases, it might be desirable to show a progress bar for each indvidual subtask. Only do this if it is genuinely useful for the user to know progress for each  subtask, or if it might be necessary to pause or stop a subtask.

Thin Progress Bars
------------------

For situations where task progress happens in the background, and accompanying text isn't as important, a thin progress bar can be used. These are smaller than regular progress bars, don't show accompanying status text, and are attached to the bottom of the header bar.

See the `style class documentation <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/style-classes.html#progress-bars>`_ for details.

General Guidelines
------------------

* If the operation is potentially destructive or resource intensive, consider adding pause and/or cancel buttons.
* Where possible, progress bars should be displayed inline, and should have a close visual relationship with the content items or controls which represent the ongoing task.
* In the past, progress windows were a popular way to present progress bars. These secondary windows would appear for the duration of a task, and would contain one or more progress bars. In general, progress windows are not recommended, since the consequence of closing the window can be unclear and they can obscure useful controls and content.

API Reference
-------------

* `GTK 4: GtkProgressBar <https://docs.gtk.org/gtk4/class.ProgressBar.html>`_
* `GTK 3: GtkProgressBar <https://docs.gtk.org/gtk3/class.ProgressBar.html>`_
