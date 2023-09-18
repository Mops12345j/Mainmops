import netifaces as ni
from subprocess import check_output, CalledProcessError
def getWifiNetworks():
    try:
        iface = [i for i in ni.interfaces() if 'wlan'in str(ni.ifaddresses[i])][0] # Find the wifi interface
         return check_output(['iwlist', iface, 'scan']).decode('utf-8')  # Scan available networks on this interface and convert to string
    except IndexError:   raise Exception("No WiFi Interface Found") from None     return []
