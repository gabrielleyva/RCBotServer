# RCBotServer for iSPY


# iSPY Server
A simple flask server that controls a raspberry pi 3 to certain specifications

# Install
Clone the repository
```
$ git clone https://github.com/gabrielleyva/RCBotServer.git
```

# Set Up
Find your machine's or raspberry pi 3 ip address by running the command
Computer:
```
$ ifconfig
```
Raspberry Pi 3:
```
$ hostname -I
```
Then navigate into the RCBot folder and open the file app.py
Replace the current ip address with your ip address and save the file

# Run
To start the server navigate into the RCBotServer directory through terminal and run the command
```
$ python app.py
```

# Test
Run the routes on a web browser or postman 
url = http://ip:5000/
