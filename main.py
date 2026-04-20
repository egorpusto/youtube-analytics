import argparse
import sys

from tabulate import tabulate

from reports import REPORTS
from services.csv_reader import read_csv_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="YouTube channel analytics CLI"
    )
    
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files with video metrics"
        )

    parser.add_argument(
        "--report",
        required=True,
        help=f"Report type. Available: {', '.join(REPORTS)}",
        )
    
    args = parser.parse_args()

    if args.report not in REPORTS:
        print(
            f"Unknown report: '{args.report}'. Available: {', '.join(REPORTS)}",
            file=sys.stderr,
        )
        sys.exit(1)

    return args


def main():
    
    try:
        args = parse_args()
        data = read_csv_files(args.files)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    report = REPORTS[args.report]()
    result = report.generate(data)

    table = [
        {"title": v.title, "ctr": v.ctr, "retention_rate": v.retention_rate}
        for v in result
    ]
 
    print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
