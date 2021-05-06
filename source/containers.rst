.. image:: img/hig-containers.svg

Containers
==========

Containers are the main building blocks of any UI, and act as the main areas of an app's UI.

Explicit Apply Containers
-------------------------

By default, controls which affect settings or properties should have an immediate effect. However, in cases where changes need to be applied simultaneously to have the desired effect, changes in the state of multiple controls can be applied in a single action. This is called explicit apply.

Explicit apply is used in the context of a single container, such as a :ref:`secondary window <secondary-windows>`, :doc:`popover </popovers>`, or :doc:`utility pane </utility-panes>`. Changes to individual controls inside the container are not applied immediately, and are instead applied as a set when changes are confirmed.

To do this, place “Cancel” and “Done” buttons in the header bar if there is one, or alternatively at the top of the container, following the :ref:`dialog button guidelines <dialog-buttons>`. Both buttons should close the container. “Cancel” resets all values in the container to the state before it was opened, and “Done” applies all changes.

Contents
--------

.. toctree::
   :maxdepth: 1

   containers/windows
   containers/header-bars
   containers/lists
   containers/flow-boxes
   containers/model-based
   containers/popovers
   containers/utility-panes