Windows users are on their own. Only linux supported! Do not create issues if you are on Windows or OSX

Installing Synapse X is quite complicated but there is simple documentation for linux users.

1. Install python
2. Install nvm
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash
```
Restart your terminal after above command is completed.
3. Install node using nvm
```
nvm install 20.18.0 && nvm use 20.18.0
```
Restart your terminal after above command is completed.

4. Clone this repo locally
5. cd into the repo

6. Setup cloud-server
```
git clone https://github.com/TurboWarp/cloud-server
cd cloud-server
npm install
```

7. Run ```npm start``` on the cloud server folder to start local server (do this every time you restart your computer before launching Synapse X).
8. Run ```python -m pip install -r requirements.txt```
9. Install tkinter - Varies depending on your distro
10. Run ```python synapse_x.py```
