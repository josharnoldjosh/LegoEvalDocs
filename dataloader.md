# Data Assigner

Here is an example of how to use the Data Assigner. 

The Data Assigner will ensure each item from the list your provide to the `data` argument will be assigned at least `count` times to different crowd workers.

> This page is still under construction ⚠️

#### main_loop.py

```python
from dataloader import DataLoader

# ...

dataloader = DataLoader(key="uniqueKeyHere", count=3, data=[
    # list of json serializable data here
])

def update(state, instruction):
    # ...

    if instruction == 'load_single_conversation':                 
        state.data["messages"] = dataloader.pop()        
```

---