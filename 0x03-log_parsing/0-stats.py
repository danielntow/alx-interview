#!/usr/bin/python3
"""read from standard input and print some stats"""

#!/usr/bin/python3
import sys
import signal


def print_stats(total_size, status_counts):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_stats(total_size, status_counts)
    sys.exit(0)


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                if len(parts) != 10:
                    continue
                ip, dash, date, get, path, http, status, size, *rest = parts

                if get != '"GET' or path != '/projects/260' or http != 'HTTP/1.1"':
                    continue

                status = int(status)
                size = int(size)

                total_size += size

                if status in valid_codes:
                    if status not in status_counts:
                        status_counts[status] = 0
                    status_counts[status] += 1

                line_count += 1
                if line_count == 10:
                    print_stats(total_size, status_counts)
                    line_count = 0

            except ValueError:
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

    # Print any remaining stats if the script finishes naturally
    print_stats(total_size, status_counts)
