import glob

import xmltodict

# TODO: Get the scan results from:
## Nmap
## Nikto
## Burp
## OpenVAS
## Nessus
## w3af
## Owasp Zap
## Masscan


def format_xml_to_dict(xml_files):
    results = list()
    for xml_file in xml_files:
        file = open(xml_file)
        xml_content = file.read()
        file.close()
        results.append(xmltodict.parse(xml_content))
    return results


if __name__ == '__main__':
    files = glob.glob("test_files/*.xml")
    scan_results = format_xml_to_dict(files)
    print('yup')