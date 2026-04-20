import csv
from typing import List
from models import Video


def read_csv_files(file_paths: List[str]) -> List[Video]:
    videos: List[Video] = []

    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    videos.append(
                        Video(
                            title=row["title"],
                            ctr=float(row["ctr"]),
                            retention_rate=float(row["retention_rate"]),
                        )
                    )
        except FileNotFoundError:
            raise ValueError(f"File not found: {path}")

    return videos