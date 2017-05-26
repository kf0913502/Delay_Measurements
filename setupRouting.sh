
wlan0Ip=`ifconfig wlan0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1`
wlan1Ip=`ifconfig wlan1 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1`
wlan0IpWithMask=`ip -o -f inet addr show | grep wlan0 | awk '/scope global/ {print $4}'`
wlan1IpWithMask=`ip -o -f inet addr show | grep wlan1 | awk '/scope global/ {print $4}'`
wlan0NetworkWithMask=`ip route | grep link | grep kernel | grep wlan1 | awk {'print $1'}`
wlan1NetworkWithMask=`ip route | grep link | grep kernel | grep wlan1 | awk {'print $1'}`
gatewayIp=`ip route | grep default | grep wlan0 | awk '{print $3}'`

ip rule add from $wlan0Ip table 1
ip rule add from $wlan1Ip table 2
ip route add $wlan0NetworkWithMask dev wlan0 scope link table 1
ip route add $wlan1NetworkWithMask dev wlan1 scope link table 2
ip route add default via $gatewayIp dev wlan0 table 1
ip route add default via $gatewayIp dev wlan1 table 2

