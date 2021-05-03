# Quickstart

Let's get up and running with LegoEval in as little **a few steps**.

## Install LEGOEval

#### 1. Clone the Repo
In your terminal app, paste the following command.
```bash
git clone https://github.com/yooli23/LEGOEval.git
```

#### 2. Install requirements.txt
Jump into the `app` folder of the `LEGOEval/` directory.
```bash
cd LEGOEval/app/
```
Next, install any requirements.
```bash
pip3 install -r requirements.txt
```

#### 3. Install NPM Modules
From the `app/` folder, execute the following command.
```bash
cd react_app
```
Next, run the following commands:
```bash
npm install
npm run build
```
They might take a while! You only need to run these commands once for installing, and once after you change any `React.js` files.

#### 4. Enable Local Debug Mode
**Make sure** that in `app/settings.py`, `debug = True` in the `server` dictionary:
```python
server = {
    # If this is False, real money will be deducted
    'debug': True,
    # ...
}
```

---

## Next steps

Here are some next steps you can take:

- [Run your task in your local browser](/runlocal)
- [Launch a task on MTurk](/mturk)
- [View your collected data](/viewdata)
- [Build a Custom Task](task/customize)

---