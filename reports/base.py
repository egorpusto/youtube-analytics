from abc import ABC, abstractmethod
from typing import List

from models import Video


class BaseReport(ABC):

    @abstractmethod
    def generate(self, data: List[Video]) -> List[Video]:
        pass