# Creating a Python Wrapper for Your Custom Page

> This page is still under construction ⚠️

We want to provide you the steps to build a custom component, however, we plan to signficantly re-write this part of the documentation to provide in-depth details. For now, it is the absolute bare-minimum to get started.

In the directory, `app/components`, create a new Python file.

```python
from util.build_helper import Component


class Page:

    def __init__(self, title="I am a title.", description="I am a description.", button="Continue"):
        self.title = title
        self.description = description
        self.button = button

    @property
    def component(self):
        # Pass in any default arguments you want to suply to your react.js file as soon as its initialized
        return Component("Page", title=self.title, description=self.description, button_name=self.button)
```

Then, you can go ahead and use your component in the `build.py`, like so:


```python
# build.py
from components.page.page import Page

# ...

start = Page()
start.title = "Hello, world!"
start.description = "These are my instructions."
start.button = "Continue"
pipeline.append(start.component)
```

