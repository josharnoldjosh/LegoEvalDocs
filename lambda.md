# Lambda Functions

If you want to return a different page based on some parameter at run-time, you can do so like so:

> This page is under construction ⚠️

#### build.py

```python

# 1. Create a function that will be called at runtime
f = def some_function(state_data):
    if state_data['xyz'] == True:
        return [SomePageA()]
    else:
        return [SomePageB()]

# 2. Add this function to the 'compute' dictionary
compute['my_key_here'] = f

# 3. Append a 'Compute' page which will execute the above function and return a page at runtime
pipeline.append(
    Compute('my_key_here')
)
```

---