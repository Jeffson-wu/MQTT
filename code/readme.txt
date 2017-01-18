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

7>restart the board,the device will automatically subscribed when booting.
