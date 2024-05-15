#!/usr/bin/python3
"""read from standard input and print some stats"""

import sys
import signal

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def handle_sigint(signum, frame):
    """Signal handler for keyboard interruption."""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, handle_sigint)

for line in sys.stdin:
    line_count += 1
    parts = line.split()

    # Validate line format
    if len(parts) < 7:
        continue

    # Extract the required parts from the line
    ip, _, _, date, request, status_code, file_size = parts[
        0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]

    # Validate the request format
    if not request.startswith('"GET /projects/260 HTTP/1.1"'):
        continue

    # Validate the status code and file size
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    # Accumulate the metrics
    total_size += file_size
    if status_code in status_codes:
        status_codes[status_code] += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final statistics if the script ends without interruption
print_stats()
