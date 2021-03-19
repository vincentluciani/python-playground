from design_patterns.strategy_pattern.strategy import Strategy


class FedexStrategy(Strategy):
    def calculate(self, order_price):
        return order_price*1.2+5