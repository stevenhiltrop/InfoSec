import report
from scan import scan_ports, scan_infrastructure


def set_configuration():
    return 0


if __name__ == "__main__":
    configuration = set_configuration()
    scan_results = scan_ports(), scan_infrastructure()
    result = report.create()
