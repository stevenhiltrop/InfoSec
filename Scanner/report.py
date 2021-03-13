def create(scan_results):
    mock_file = \
        {'45.33.32.156':
            {'hostnames':
                [
                    {'name': 'scanme.nmap.org', 'type': 'user'},
                    {'name': 'scanme.nmap.org', 'type': 'PTR'}
                ],
                'addresses': {
                    'ipv4': '45.33.32.156'
                },
                'vendor': {},
                'status': {'state': 'up', 'reason': 'syn-ack'},
                'tcp': {
                    22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': '', 'version': '',
                         'extrainfo': '',
                         'conf': '3', 'cpe': ''},
                    25: {'state': 'filtered', 'reason': 'no-response', 'name': 'smtp', 'product': '', 'version': '',
                         'extrainfo': '', 'conf': '3', 'cpe': ''},
                    80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '',
                         'extrainfo': '', 'conf': '3', 'cpe': ''}
                }
            }
        }

    print(scan_results)
