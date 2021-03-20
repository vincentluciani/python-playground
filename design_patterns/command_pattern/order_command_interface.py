from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractOrderCommand(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

