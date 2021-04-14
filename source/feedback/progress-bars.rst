Progress Bars
=============

Progress bars indicate progress on a task. Unlike spinners, they can indicate the proportion of the task that has been completed, as well as the time remaining.

Progress bars are most appropriate for indicating progress on tasks that take a relatively long time (as a rule of thumb, tasks that take over 30 seconds). For tasks that have shorter periods, spinners are often a better choice.

Types
-----

There are three types of progress bar:

* **Time-remaining**: these indicate how much time remains in an operation.
* **Typical-time**: these indicate how much time remains, based on an estimate of the expected duration.
* **Indeterminate**: these only indicate that an operation is ongoing, not how long it will take.

Accuracy is preferable for progress bars: where possible, use a time-remaining progress bar, followed by typical-time. Try to avoid using indeterminate progress bars.

When using a typical-time progress bar, handle overestimation by showing explanatory progress text at the end of the oporation, such as “Almost done”. Handle underestimation by filling in the remaining portion of the progress bar.

Progress Text
-------------

Progress text should describe how much of the task has been completed. When deciding on progress text:

* Provide specific information rather than a unitless percentage. For example, “13 of 19 images rotated” or “12.1 of 30 MB downloaded” rather than “13% complete”.
* For long-running tasks, it can be desirable to show an estimate of the time remaining. If other relevant information isn't available, this can be shown on its own.
* If the time remaining is an estimate, use the word “about“. For example, “About 3 minutes left”.
* Use :doc:`typographic conventions </guidelines/typography>` to differentiate the most useful information.

Task Stages
-----------

Some tasks can be made up of a sequential series of stages, each of which has its own time estimation. In these situations, try to create a single composite typical-time progress bar. Only communicate the different stages in a task when they are relevant to a user.

Sometimes it might be possible to estimate the time remaining for part of a task, but not another part. In this situation, the progress bar can show indeterminate progress for part of the task. However, it is best not to show indeterminate progress bars for long periods of time, and the number of progress bar mode changes should be kept to an absolute minimum. Avoid indeterminate progress wherever possible.

Sub-Tasks
---------

Some tasks are comprised of multiple simultaneous sub-tasks (such as downloading several files at the same time). Here, it is generally advisable to show a single progress bar which indicates composite progress for the overall task.

In very rare cases, it might be desirable to show a progress bar for each indvidual sub-task. Only do this if it is genuinely useful for the user to know progress for each  sub-task, or if it might be necessary to pause or stop a sub-task.

General Guidelines
------------------

* If the operation is potentially destructive or resource intensive, consider adding pause and/or cancel buttons.
* Where possible, progress bars should be displayed inline, and should have a close visual relationship with the content items or controls which represent the ongoing task.
* In the past, progress windows were a popular way to present progress bars. These secondary windows would appear for the duration of a task, and would contain one or more progress bars. In general, progress windows are not recommended, since the consequence of closing the window can be unclear and they can obscure useful controls and content.

API Reference
-------------

* GtkProgressBar: `GTK 4 <https://gnome.pages.gitlab.gnome.org/gtk/gtk4/class.ProgressBar.html>`_, `GTK 3 <https://developer.gnome.org/gtk3/stable/GtkProgressBar.html>`_