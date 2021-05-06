# Task Creation Overview

Let's talk about the basics.

#### Introduction 

When creating a task, there are two main components to tackle:

1. The front-end
2. The back-end

Typically, as a researcher or developer, the back-end stuff can be pretty straight forward—you likely already have code for your model, etc.

The front-end is typically where things get more difficult—especially passing data between the front-end and back-end, and vice-versa.

#### General Task Creation Steps

Let's outline how you can go about building your own task.

0. (Optionally) Create custom `pages` / UI-elements for your task by writing a single `react.js` file for each page.
1. Edit the `app/build.py` python file. Specifically, snap together pre-existing UI pages in a simple fashion.
2. Add in the required logic that each component might demand in the `app/main_loop.py`.


#### Next steps

We recommend reading the articles in the following order:

1. [Editing the build.py file](/build)
2. [Editing the main_loop.py file](/temp).
3. [Creating custom components](/temp).


---