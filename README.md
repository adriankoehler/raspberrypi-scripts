# setup raspberry pi with raspbian installed

`sudo apt update`  
`sudo apt upgrade`  
`sudo apt-get dist-upgrade`  

### webserver
`sudo apt install apache2 -y`  
`sudo apt install php libapache2-mod-php -y`  

### wiringPi
`sudo apt-get install wiringpi`

### motd
https://indibit.de/raspberry-pi-ssh-login-nachricht-anpassen-motd/

### telegram
`sudo apt-get install python-pip`  
`sudo pip install telepot`  

### tradfri
`sudo apt-get install build-essential autoconf automake libtool`  
`git clone --recursive https://github.com/obgm/libcoap.git`  
`cd libcoap`  
`git checkout dtls`  
`git submodule update --init --recursive`  
`./autogen.sh`  
`./configure --disable-documentation --disable-shared`  
`make`  
`sudo make install`  

### zeromq(sockets)
`pip install pyzmq`  

### temphumid
`sudo apt-get install -y build-essential python-dev git`  
`mkdir -p /home/pi/downloads`  
`cd /home/pi/sources`  
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git  `  
`cd Adafruit_Python_DHT`  
`sudo python setup.py install`  

