from design_patterns.strategy_pattern.cost_calculator import CostCalculator
from design_patterns.strategy_pattern.strategies.fedex_strategy import FedexStrategy
from design_patterns.strategy_pattern.strategies.ups_strategy import UPSStrategy

strategy = FedexStrategy()

cost_calculator = CostCalculator(strategy)

print(cost_calculator.get_cost(10))

strategy = UPSStrategy()

cost_calculator = CostCalculator(strategy)

print(cost_calculator.get_cost(10))





