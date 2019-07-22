import ipaddress
import subprocess

alive = []
subnet = ipaddress.ip_network(
    input("What is the CIDR Notation of the IP's you want to ping? "), strict=False
)
for i in subnet.hosts():
    i = str(i)
    retval = subprocess.call(["ping", "-c1", "-n", "-i0.1", "-W1", i])
    if retval == 0:
        alive.append(i)
for ip in alive:
    print(ip + " is alive".upper())
