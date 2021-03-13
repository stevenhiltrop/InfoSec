import subprocess
import nmap
from urllib.parse import urlparse


def nmap(host):
    domain = urlparse(host).netloc
    scanner = nmap.PortScanner()
    scanner.scan(domain, arguments='-F')
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
    web = scan_web(host)
    return infra, web
