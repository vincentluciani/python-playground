from unittest.mock import Mock

from injectable import (
    injectable,
    autowired,
    Autowired,
    Injectable,
    load_injection_container,
)
from injectable.testing import clear_injectables, register_injectables


@injectable
class RealCar:
    @staticmethod
    def print():
        print("driving for real")


class InjectableMocking():
    def __init__(self):
        clear_injectables(RealCar)
        mocked_car = Mock(wraps=RealCar)
        mocked_car.print = Mock(side_effect=lambda: print("driving but not for real"))
        mocked_injectable = Injectable(lambda: mocked_car)
        register_injectables({mocked_injectable}, RealCar)

    @autowired
    def run(self, dep: Autowired(RealCar)):
        dep.print()
        # MockedDep
        dep.print.assert_called()


def run_example():
    load_injection_container()
    example = InjectableMocking()
    example.run()


if __name__ == "__main__":
    run_example()