# App Basics

These Human Interface Guidelines provide design guidance on the creation of GNOME applications. Given this focus on applications, this page provides a definition of applications from a user experience perspective. It also provides guidance on basic application behavior and characteristics.

The application model allows users to understand how software is distributed, installed and removed, as well as how that software behaves when in use. Ensuring that your software behaves according to this model will therefore help to ensure that it is predictable and conforms to user expectations. It will also ensure correct integration with system tools for installing and removing applications.

## What is an application?

The following list of characteristics provides a basic definition of an application. An application is a distinct piece of software which:

 * Can be individually installed and removed from the system.
 * Does not affect or interfere with the behavior of other applications.
 * Does not rely on other applications in order to run.
 * Provides at least one primary window (see [primary windows][]).
 * Has a unique name and icons (see [icon design][]).
 * Has an application launcher.

 key theme in this definition is that applications are intended to be independent of other applications. This ensures flexibility, predictability, and simplicity of use.

Of course, there are other characteristics that are expected of applications, including standard window behavior, system integration, and application metadata. Guidance on these aspects of applications can be found elsewhere.

## Naming your application

An application’s name is vital. It is what users will be first exposed to, and will help them decide whether they want to use an application or not. It is a major part of your application’s public face.

An application name plays a number of functions:

 * It must advertise your application to potential users.
 * It should serve to reinforce a positive identity, and have expressive qualities.
 * It needs to identify your application in the systems where it is installed and run.

Ensure that your application name is short — fewer than 15 characters. This will ensure that it is always displayed in full within a GNOME 3 environment.

<p>Additionally, choose an application name that is easy to understand and communicates your application’s functionality. Avoid references which will not be understood or be familiar to potential users, such as obscure cultural references, inside jokes and acronyms. Instead, pick a name that references what your application does, or the domain in which it operates.
