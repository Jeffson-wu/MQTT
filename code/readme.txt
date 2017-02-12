7688 setup
======================================================================

1>Install paho-mqtt package

#pip install paho-mqtt

2>Install packages for outputing audio

------AK added
UPDATE opkg packages

#opkg update
-----
#opkg install kmod-usb-audio
#opkg install ffmpeg

3>put the "iot" script into /etc/init.d/ directory
#cp iot/code/iot /etc/init.d

4>Change "iot" script permmision

#chmod 755 iot/code/iot

5>put the subscribe.py into /usr/sbin/

#cp iot/code/subscribe.py /usr/sbin

6>Enable iot script in boot-up

#/etc/init.d/iot enable

7>make the cronjob to prevent the subscribing process dead

#cp iot/code/7688.sh /usr/sbin
#chmod +x /usr/sbin/7688.sh
#crontab -e (add "* * * * * /bin/sh /usr/sbin/7688.sh" to the new file)

8>run curl command in the remote machine
curl -s http://104.236.243.30/publish.py | python - mqtt://obbzesrv:ZFBjLQuS1h3A@m10.cloudmqtt.com:13198  http://www.thewavsite.com/Birthday/bday02.wav <eth0 mac address>

9>restart the board,the device will automatically subscribed when booting.
