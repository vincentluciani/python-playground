class CostCalculator():
    def __init__(self,strategy):
        self._strategy = strategy

    def get_cost(self,order_price):
        return self._strategy.calculate(order_price)