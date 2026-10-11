# Network Setup Instructions
This is meant to be paired with my instructional video's on setting everything up.

## Step 1: Creating the VM's 

1. Go to virtualbox to download the application for your OS.
```
https://www.virtualbox.org/wiki/Downloads
```
2. Download the Ubuntu Server IPO
```
https://ubuntu.com/download/server
```
3. Run the virtualbox application.
4. Create a new VM by pressing the new button.
    * Name your VM, since we start with the client VM, I recommend dp-client
    * Select the ubunto iso file for your ISO image
    * Set up you unattended guest OS installation with a username and password for your new VM
5. Let the Ubuntu server attempt set up. This will take several minutes.
6. Once the server is created, log in to your account to test it.
7. power off the VM, you can run the command:
    ```
    sudo poweroff
    ```
8. Click on the VM, and go to settings and then network

    -Select Adapter 2

    -Select the enable network adapter box

    -Attach to Host-Only Adapter

    -Click okay, and restart the VM


## Step 2: Configuring the VM
Unfortunately, you cannot paste in the VM until we remote in during step 3. You will have to type the code.

1.  Update the system: 
    ```
    sudo apt update && sudo apt upgrade -y
    ```
2. ADD SSH (I forget to do this in the video until later, but this is a good time to do it.)
    ```
      sudo apt install -y openssh-server
    ```
    ```
      sudo systemctl status ssh
    ```
3. Check that IP port 3 is visible and note the name. Should be enp0s8, if not change code in places where enp0s8 appears to what is actually states.
    ```
    ip a
    ```
4. Now we give it a fixed IP (by default it will change every time we set it up)
create a yaml file:
    ```
    sudo vi /etc/netplan/60-hostonly.yaml
    ```
    VI tips: press esc to switch modes, press i to enter insert mode, type code below, and then press escape and shift zz.

    Type this in the file (the tabs do matter): 
    ```
    network:
      version: 2
      ethernets:
        enp0s8:
          addresses: [192.168.56.10/24]
    ```
    Save with shift zz (p.s. yes press z twice) (p.p.s. DO NOT USE COMMAND z) 

  This line will give the file more permissions, needed to change IP.

  
    ```
    sudo chmod 600 /etc/netplan/60-hostonly.yaml
    ```

  Running this command will change the IP.

  
    ```
    sudo netplan apply
    ```

### Now we move to setting up the second VM for the website backend.
1. Shut down the first VM. Can do this by powering off through buttons or running:
    ```
    sudo poweroff
    ```
2. Go to your vm in the virtual box application, right click, and select clone.
      * Rename the clone vm to dp-server
      * sellect full clone clone type
      * select generate new MAC addresses for all network adapters
  
3. We need to make changes so that it is a completely unique VM
    * 1: Change the host name (So they don't look the same):
       ```
       sudo hostnamectl set-hostname dp-server
       ```
     
    * 2: Change the Machine ID (otherwise both VMs can ask DHCP for the same address, and some services get confused):
       ```
       sudo rm /etc/machine-id
       ```
       ```
       sudo systemd-machine-id-setup
       ```
     
    * 3: Change the Static IP (Change the address in the netplan file from .10 to .11):
       ```
       sudo vi /etc/netplan/60-hostonly.yaml
       ```
     Edit this file so that the IP is changed. See below:
   ```
        network:
          version: 2
          ethernets:
            enp0s8:
              addresses: [192.168.56.11/24]
   ```
   ```
       sudo netplan apply
   ```
     
    * 4: SSH host keys. (The clone shares the original’s SSH identity, which makes Windows complain about changed or duplicate fingerprints Regenerate them):
    
    If you made my mistake in the video you need this code:
    ```
      sudo apt update
      sudo apt install -y openssh-server
      sudo systemctl status ssh
    ```

    Else, you are a better person than I am and here is the code you can use:

     ```
     sudo rm /etc/ssh/ssh_host_*
     ```
     ```
     sudo dpkg-reconfigure openssh-server
     ```
     ```
     sudo systemctl restart ssh
     ```

     
## Step 3: Connecting the VM's and sending a test

### Remote in to continue set up
  At this point it will be easier to remote in so that you can copy code to your clipboard. 

  To do this:
  * Ensure your VM is running
  * open up your command line on your PC
  * Run the command ssh username@(vmip)
    * example: ssh name@192.168.56.10 (.11 for backend)
  * Log in to your vm
  
  Make sure to do this for both and to keep them seperate.

### Backend VM Server Code:
  ```
  sudo apt install python3-venv python3-pip
  ```
  ```
  mkdir ~/api && cd ~/api
  ```
  ```
  python3 -m venv venv
  ```
  ```
  source venv/bin/activate
  ```
  ```
  pip install flask gunicorn
  ```
  ```
  vi app.py
  ```

  File code:
  ```
  from flask import Flask, jsonify
  
  app = Flask(__name__)
  
  @app.route("/hello")
  def hello():
      return jsonify(message="Hello from the backend!")
  
  if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)
  ```

  ```
  python app.py
  ```


### Frontend VM Server Code:
1. Run frontend specific install.
   
      ```
      sudo apt install -y nginx
      ```

3. Create a HTML test file
   
      ```
      sudo vi /var/www/html/index.html
      ```
      Paste this into the file:

      ```
      <h1>Frontend works</h1>
      ```

4. Modify the server block to create a proxy pass for the http requests.
   
   ```
        sudo nano /etc/nginx/sites-available/default
   ```
  
    Then inside the server { ... } block, keep what’s there and add this above the existing location / block:

   ```
        location /api/ {
            proxy_pass http://192.168.56.11:5000/;
        }
   ```
    
    Test and reload:

   ```
          sudo nginx -t
   ```
   ```
          sudo systemctl reload nginx
   ```

### Test The Connection:
  1. Frontend VM: (VMs can see each other)
      ```
      ping -c 3 192.168.56.11
      ```
  2. Frontend VM: (backend answers)
      ```
      curl http://192.168.56.11:5000/hello
      ```
  3. Your Windows browser: (shows “Frontend works”)
      ```
      http://192.168.56.10
      ```
  4. Your Windows browser: (shows the backend’s message, passing through the frontend)
      ```
      http://192.168.56.10/api/hello
      ```

## Step 4: Setting up remote VS code access to your VM's
All of this is assuming you use vscode
1. Install the remote-SSH extension by microsoft 
2. click on the open a remote window button. (very very bottom left, has arrows > < as its icon)
3. click connect to host
4. add new SSH Host
5. SSH in using the same command as used in terminal: ssh name@192.168.56.10
6. Select the top config file to update
7. click connect, or now you can connect to host as an option in the connect to host menu
8. let it spend a long time setting up
9. open a folder and access the drive we saved the code in
     * Frontend: `/var/www/`
     * Backend: `/home/<username>/api`
10. press okay
11. Now you can write so much code!!!!!

