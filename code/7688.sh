#!/bin/bash
ser = subscribe

if (( ps | grep $ser ) > 0 )
then
echo "$ser is running!!!"
else
/etc/init.d/iot start
fi
~

