7688 setup
=========================================================================
1>Install paho-mqtt package

#pip install paho-mqtt

2>Install packages for outputing audio

------AK added
UPDATE opkg packages

#opkg update
-----
#opkg install kmod-usb-audio
#opkg install ffmpeg

3>Put the "iot" script into /etc/init.d/ directory
#cp iot/code/iot /etc/init.d

4>Change "iot" script permmision

#chmod 755 iot/code/iot

5>Put the subscribe.py into /usr/sbin/

#cp iot/code/subscribe.py /usr/sbin

6>Enable iot script in boot-up

#/etc/init.d/iot enable

7>Make the cronjob to prevent the subscribing process dead

#cp iot/code/7688.sh /usr/sbin
#chmod +x /usr/sbin/7688.sh
#crontab -e (add "* * * * * /bin/sh /usr/sbin/7688.sh" to the new file)

8>Restart the board,the device will automatically subscribed when booting.


Create the user
=========================================================================
1>Broswer http://104.236.243.30/login.html

2>Enter your board credentials to create the user
note:the user name should be without numbers,the mac address should strip colon;

3>Click submit to create the user


Modify the code to adjust to your board
=========================================================================
1>Open subscribe.py

2>Modify this line

#url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://obbzesrv:ZFBjLQuS1h3A@m10.cloudmqtt.com:13198')
change "obbzesrv:ZFBjLQuS1h3A" to your own cloudmqtt credential(username:password).


Test the result
=========================================================================
1>curl command to send publishing request
curl -s http://104.236.243.30/publish.py | python - mqtt://obbzesrv:ZFBjLQuS1h3A@m10.cloudmqtt.com:13198  http://www.thewavsite.com/Birthday/bday02.wav <mac address>

note:
1>change "obbzesrv:ZFBjLQuS1h3A" to your username:password which is created using web interface.
2>replace <mac address> with  your board mac address which is with colon stripped.
