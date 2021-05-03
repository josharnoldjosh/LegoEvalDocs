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

## Demo A Task Locally
**Make sure** you're in the `app/` directory, run the following command and jump to [localhost](http://127.0.0.1:2988/helloworld).
```bash
cd ..
python3 server.py
```

---

## Launch on MTurk Sandbox
#### 1. Enable Sandbox Mode
**Make sure** that in `app/mturk/settings.py`, `is_sandbox = True` in the `mturk` dictionary:
```python
mturk = {
    # If this is False, real money will be deducted
    'is_sandbox': True,
    # ...
}
```
#### 2. Disable Local Debug Mode
**Make sure** that in `app/settings.py`, `debug = True` in the `server` dictionary:
```python
server = {
    # If this is False, real money will be deducted
    'debug': False,
    # ...
}
```

#### 3. Delete our build!
Currently, for launching on MTurk, you're going to need to delete the following folders:

1. `app/react_app/build/`
2. `app/react_app/node_modules/`

We're working hard to remove steps like this (to make your life easier), but for now, please delete the above folders before proceeding to the next step.

> Note: If you want to run your task locally again, make sure to run `npm install` and `npm run build` inside of `react_app` again.


#### 4. Run the MTurk Command
Whilst still in the `app/` folder, lets go ahead and run the following command:
```
python3 launch_hits.py --task_name demo
```

> Note: After running the above command, you might be asked for some AWS and Heroku information. It should be pretty self explanatory how to provide this information. 

And voilà! After about **5 minutes** (unforuntely there is some setup time required for launching a web server on Heroku), you should get some links below:
```bash
31KPKEKW4AD78QC0RLKFD4B4PAT0BV https://workersandbox.mturk.com/mturk/preview?groupId=3PN7FLVWM454R7NYSKRT54250KKSYM
33NOQL7T9OZL8DKJS3DXS1OPZBR8ZW https://workersandbox.mturk.com/mturk/preview?groupId=3PN7FLVWM454R7NYSKRT54250KKSYM
34KYK9TV2R879ZWC0N3ZNAHNK2CBST https://workersandbox.mturk.com/mturk/preview?groupId=3PN7FLVWM454R7NYSKRT54250KKSYM
389A2A304OIQIV465LGAOOHM7VT0C2 https://workersandbox.mturk.com/mturk/preview?groupId=3PN7FLVWM454R7NYSKRT54250KKSYM
3UQVX1UPFSHDKDC48SR4CB80V4G20V https://workersandbox.mturk.com/mturk/preview?groupId=3PN7FLVWM454R7NYSKRT54250KKSYM
...
```

---

## Viewing your Data

Coming soon.

---

## Customizing Your Task
We'll have more details coming describing how you can launch your own, customized tasks in as little as a few steps! But for now, please check out these two files:

1. `app/build.py`
2. `app/main_loop.py`

More content coming soon!
