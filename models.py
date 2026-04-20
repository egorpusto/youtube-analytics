from dataclasses import dataclass


@dataclass
class Video:
    title: str
    ctr: float
    retention_rate: float