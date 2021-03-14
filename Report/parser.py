import glob
import json

import xmltodict


def format_xml_to_json(xml_files):
    results = list()
    for xml_file in xml_files:
        file = open(xml_file)
        xml_content = file.read()
        file.close()
        results.append(json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True))
    return results


if __name__ == '__main__':
    files = glob.glob("test_files/*.xml")
    scan_results = format_xml_to_json(files)
