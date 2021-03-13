import argparse
import sys

import report
import scan

# TODO: set_configuration for user input and help documenation


def set_configuration():
    msg = "Description message"
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument("-i", "--input", help="Show input")
    parser.add_argument("-o", "--output", help="Show output")
    args = parser.parse_args()


if __name__ == "__main__":
    # configuration = set_configuration()
    scan_results = scan.start(sys.argv[1])
    result = report.create(scan_results)
