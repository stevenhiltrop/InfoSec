import subprocess
from urllib.parse import urlparse

import nmap


def get_ports(data):
    for item in data['scan']:
        print(item)
        if item == 'tcp':
            print(data[item])
        else:
            get_ports(data[item])


def nmap(host):
    domain = urlparse(host).netloc
    scanner = nmap.PortScanner()
    result = scanner.scan(domain, arguments='-n -F')
    ports = get_ports(data=result)
    return scanner['scan']


def nikto(host):
    return subprocess.check_output(['nikto', '-host', host])


def scan_infrastructure(host):
    nmap_result = nmap(host)
    return nmap_result


def scan_web(host):
    nikto_result = nikto(host)
    return nikto_result


def start(host):
    infra = scan_infrastructure(host)
    # web = scan_web(host)
    return infra
