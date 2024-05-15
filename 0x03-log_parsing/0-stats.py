#!/usr/bin/python3
"""read from standard input and print some stats"""

import sys


def parse_line(line):
    """
    Parses a log line and extracts relevant information.
    Returns a tuple: (status_code, file_size)
    """
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None


def main():
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f"File size: {total_file_size}")
                    for code in sorted(status_counts.keys()):
                        if status_counts[code] > 0:
                            print(f"{code}: {status_counts[code]}")
                    print()

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print(f"File size: {total_file_size}")
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    main()
