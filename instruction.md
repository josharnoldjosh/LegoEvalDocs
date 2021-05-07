# Instruction Page

The instruction page is useful for displaying instructions, or a decent amount of text before the user contains on to a more functional-aspect of your task.

The instruction page is user easy to use.

Below is an example for creating a "start" page.

#### build.py

The `title` and `description` are pretty self-explanatory. The `button` sets the title of the button for advancing to the next page.

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


#### main_loop.py

The only `instruction` necesscary to implement is the `advance` instruction, which requests the backend to advance the state to the next page.

```python
# main_loop.py

# ...

def update(state, instruction):    
    
    # ...

    if instruction == 'advance':
        state.advance()

    return state 
```

---