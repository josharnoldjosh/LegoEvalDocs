# Running a Task Locally

#### Install NPM Modules
From the `app/react_app/` folder, execute the following commands.
```bash
npm install
npm run build
```
They might take a while! Once you've run this command, you **don't** need to run it again **unless**:

1. You modify any `.js` file
2. You delete either the `react_app/build/` folder or `react_app/node_modules/` folder

#### Comment Out MTurk lines in `build.py`
Make sure these lines are commented out, like so.
```python

# ...

# pipeline.append(
#     LoadMTurk(
#         title=TASK_TITLE,
#         description=TASK_INSTRUCTION,
#     ).component
# )

# ...

# pipeline.append(
#     SubmitMTurk().component
# )
```

#### Run the `server.py` Command
**Make sure** you're in the `app/` directory, run the following command and jump to [localhost](http://127.0.0.1:2988/helloworld).
```bash
python3 server.py
```
---