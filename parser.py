import re

REGEXP = (r'\[\s*([0-9]+)\]\s*([0-9\.]+)-([0-9\.]+)\s*sec\s*([0-9\.]+)\s*([A-Za-z]+)\s*([0-9\.]+)\s*([A-Za-z]+)?('
          r'bits/sec)\s*([0-9]+)?\s*([0-9\.]+)?\s*([A-Za-z]+)?(Bytes)')
KEYS = ('ID', 'Start', 'End', 'Transfer', 'Transfer_Unit', 'Bitrate', 'Bitrate_Unit', 'Retr', 'Cwnd')


def parse_iperf_output(output):
    match = re.search(REGEXP, output)
    if match:
        return {key: match.group(i) for i, key in enumerate(KEYS, 1)}
    else:
        return None
