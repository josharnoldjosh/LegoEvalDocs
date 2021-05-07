# Chatbot Page

The chatbot page displays an interactive chatbot to the user.

The chatbot can be optionally configured to start with a default message.

The chatbot page is still fairly elementary, however, we are hoping to extend its logic as soon as possible.

> Note: You can customize the logic of the chatbot by editing the react.js file in `app/react_app/src/chatbot/Chatbot.js`

#### build.py

Its super easy to add a chatbot.

```python
# build.py
from components.chatbot.chatbot import Chatbot

# ...

pipeline.append(Chatbot("MyUniqueIdentiferHere").component)
```


#### main_loop.py

Below is an example where, when the `request_message` instruction is called, we:

1. Get the last message, `last_message`, from the user
2. Use the `last_message` in the back-end's response to the user
3. Advance to the next page in the task by calling `state.advance()` after 8 messages have been acrued.

`request_message` essentially asks the back-end to add a message to the list `state.data["messages"]`, in the format:

```python
{
    'id': # <the message number>, 
    'senderId': # <the title of the sender>, 
    'text': # <the backend's response>
}
```

```python
# main_loop.py

def update(state, instruction):

    # ...

    if instruction == 'request_message':

        last_message = state.data["messages"][-1]["text"] # optionally get the last message

        state.data["messages"].append(
            {'id':len(state.data["messages"]), 
            'senderId':'Robot', 
            'text': f"I think {last_message} is great too!"}
        ) # append a new message...

        if len(state.data["messages"]) >= 8:
            state.advance() # call advance when satisfied...
```

---