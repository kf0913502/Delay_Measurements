
wifiOne=$1
wifiTwo=$2
wlan0Ip=`ifconfig $wifiOne | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1`
wlan1Ip=`ifconfig $wifiTwo | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1`
wlan0IpWithMask=`ip -o -f inet addr show | grep $wifiOne | awk '/scope global/ {print $4}'`
wlan1IpWithMask=`ip -o -f inet addr show | grep $wifiTwo | awk '/scope global/ {print $4}'`
wlan0NetworkWithMask=`ip route | grep link | grep kernel | grep $wifiOne | awk {'print $1'}`
wlan1NetworkWithMask=`ip route | grep link | grep kernel | grep $wifiTwo | awk {'print $1'}`
gatewayIp=`ip route | grep default | grep $wifiOne | awk '{print $3}'`

ip rule add from $wlan0Ip table 1
ip rule add from $wlan1Ip table 2
#ip route add $wlan0NetworkWithMask dev $wifiOne scope link table 1
#ip route add $wlan1NetworkWithMask dev $wifiTwo scope link table 2
ip route add default via $gatewayIp dev $wifiOne table 1
ip route add default via $gatewayIp dev $wifiTwo table 2

