from __future__ import annotations

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @property
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @property
    @abstractmethod
    def forward(self, **kwargs):
        pass