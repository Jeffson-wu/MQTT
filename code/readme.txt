7688 setup
======================================================================

1>Install paho-mqtt package

#pip install paho-mqtt

2>Install packages for outputing audio

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


8>restart the board,the device will automatically subscribed when booting.
