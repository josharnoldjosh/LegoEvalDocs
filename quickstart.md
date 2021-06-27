# Quickstart

Let's get up and running with LegoEval in as little **a few steps**.

## Install LEGOEval
LegoEval supports **Python 3.6+**. Windows is not supported currently.

### 1. Installing via pip
If you have installed **npm >= 7.7.6** and **Node.js >= 15.13.0**, you can install LegoEval via `pip`.

#### Clone the Repo
In your terminal app, paste the following command.
```bash
git clone https://github.com/yooli23/LEGOEval.git
```
#### Installing the libarary and dependencies
Installing the library and dependencies is simple using `pip`.
```bash
cd ./LEGOEval/app/
pip3 install -r requirements.txt
```

### 2. Installing via Docker
We also provide a dockerfile which makes it easy to distribute the environment.

Once you have installed [Docker](https://docs.docker.com/get-docker/), you can run the following commands to get the environment.

1. Build
```bash
sudo docker build https://github.com/yooli23/LEGOEval.git -t legoeval:1
```

2. Run docker
```bash
sudo docker run -it legoeval:1
```

3. Clone the code
```bash
git clone https://github.com/yooli23/LEGOEval.git
```

<!-- #### 2. Install requirements.txt
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
``` -->
---

## Next steps

Here are some next steps you can take:

- [Run your task in your local browser](/runlocal)
- [Launch a task on MTurk](/mturk)
- [Design your own Task](/taskbasics)

---