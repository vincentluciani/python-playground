from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractCommand(ABC):
    @property
    @abstractmethod
    def execute(self):
        pass