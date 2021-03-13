import subprocess


def nmap(host):
    return subprocess.check_output(['nmap', '-A -sCV -T4 -Pn', host])


def nikto(host):
    return subprocess.check_output(['nikto', '-host', host])


def scan_ports(configuration):
    host = configuration.host
    nmap_result = nmap(host)
    return nmap_result


def scan_infrastructure(configuration):
    host = configuration.host
    nikto_result = nikto(host)
    return nikto_result
