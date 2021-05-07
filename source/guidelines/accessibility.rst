Accessibility
=============

The guidelines included in the HIG incorporate relevant advice regarding accessibility and, in general, following the HIG will produce accessible designs. A number of them are particularly relevant to this topic, including the pages on :doc:`keyboard interaction <keyboard>`, :doc:`pointer interaction <pointer-touch>`, and :doc:`UI styling <ui-styling>`.

This page a few general principles, as well as a reference list on testing.

General Guidelines
------------------

Good design and accessibility are mutually reinforcing, and many of the :doc:`principles of good design </principles>` advocated by these guidelines enhance accessibility. Thinking carefully about how to follow those principles is one of the best ways to improve the accessibility of your application.

Additionly, there are a number of things to avoid in your app, in order to support accessibility, including:

* Using color as the only means to distinguish items of information. Instead, all information should be provided by at least one other method, such as shape, position or textual description.
* The use of flashing or blinking elements, as this may cause problems for people who are susceptible to visually-induced seizures.

Accessible Names
----------------

All interface elements should have descriptive, accessible names. These provide the text that is read aloud by screen readers.

GTK provides default accessible descriptions for many UI elements, but they may need to be added in some cases. Consider overriding the defaults with more helpful or application-specific descriptions where possible.

Accessible names should be short and descriptive.

Testing for Accessibility
-------------------------

There are a number of quick and easy ways to check whether your application is accessible, and these are described in the relevant pages of the HIG. The following list brings them together, as a reference. In each case, test to ensure that your application works correctly with accessibility features, including:

* High-contrast mode. This can be enabled from GTK Inspector or globally in the Accessibility settings. All parts of the UI should be correctly rendered in the high-contrast style.
* Large text mode. This can be enabled in the Accessibility settings. Does the UI look correct with it enabled? Can all labels be read?
* Keyboard navigation. Use the app using only the keyboard. Can every part of the application be navigated and interacted with? Does the UI follow the :ref:`keyboard navigation guidelines <keyboard-nav>`?
* Screen reader. This can be enabled from the Accessibility settings. Is each UI element read aloud? Are the accessible names accurate? Can you turn the display off and still use the app?
* On-screen keyboard: can your app be used while relying on the OSK for text input? Can every text entry be successfully used with it?