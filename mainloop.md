# main_loop.py

The `main_loop.py` is the intersection where data is passed between the front-end and back-end. It's where the developer, *you*, can define your custom logic for each `page` you've added in your `build.py` file!

#### Introduction

Inside the `main_loop.py` file, there's only a single function called `update`. 

`update` is called each time the front-end wants to communicate with the back-end. It is the back-end's opportunity to influence the front-end and handle any necesscary logic.

```python
def update(state, instruction):

    # ...

    # Advance to a new page
    if instruction == 'advance':
        state.advance() 

    # Submit MTurk if necesscary
    if instruction == 'mark_complete':
        SubmitMTurk.mark_task_complete(state)

    return state
```

#### State

You'll notice [state](/temp) is the first argument passed into the `update` function.

The [state](/temp) represents, well, the entire *state* of the application. It contains all the data associated with the task, etc. You can think of it as the tasks database. You can read more about state [here](/temp).

Thus, the [state](/temp) object can be used to *read* the data that's currently been saved/collected, for example, what information the crowd-worker has answered for a survey, or a crowd-workers dialog history. You can access all of this information that might be saved via `state.data`, which returns a python dictionary.

If you want to **save data**, i.e, persist data in the database, you simply need to store it in the `state.data` dictionary, by doing something like:

```python
state.data["my_key"] = my_object
```

What's awesome about [state](/temp) is that any data you persist will automatically be available for the front-end components. Thus, if you end up creating a custom `page` by writing your own react.js file, its really easy to pass data between the front and back-end.

#### Instructions

You'll notice the second argument is the `instruction` argument. The `instruction` is simply a string.

The `instruction` will tell you what the front-end `page` is expecting. For example, when a user clicks submit on their survey page, the survey page sends the `advance` instruction which basically says, "this page is complete, can we advance to the next page?"

Thus when the back-end recieves the `advance` instruction, we can call `advance()` on the state object to automatically pop to the next `page` in your `build.py`.

Different `pages` will have different needs. For example, a `chatbot` page will send an instruction when the crowd-worker has sent a message, and it needs to send back a response: the `chatbot` page will send the `request_message` instruction in this case and will expect the response from the backend to be appended to the `state.data["messages"]` list.

**You can find detailed information about all the different instructions for each page in the `Page Library` section of the docs.**


#### Steps

For each type of `page` you've implemented in your [build.py](/build), just make sure to implement every instruction that those pages demand. Simply look at the **Page Library** for each componenet to figure this out.

After you've implmented the [build.py](/build) and the update function in the `main_loop.py`, you're ready to:

1. Run your task [locally](/runlocal)
2. Launch your task on [MTurk](/mturk)

---