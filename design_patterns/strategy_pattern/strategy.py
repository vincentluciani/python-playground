from __future__ import annotations

from abc import ABC, abstractmethod

class Strategy(ABC):
    @property
    @abstractmethod
    def calculate(self, order_price):
        pass