from typing import List

from models import Video
from reports.base import BaseReport

CTR_THRESHOLD = 15.0
RETENTION_THRESHOLD = 40.0


class ClickbaitReport(BaseReport):

    def generate(self, data: List[Video]) -> List[Video]:
        filtered = [
            video
            for video in data
            if video.ctr > CTR_THRESHOLD
            and video.retention_rate < RETENTION_THRESHOLD
        ]

        return sorted(filtered, key=lambda v: v.ctr, reverse=True)