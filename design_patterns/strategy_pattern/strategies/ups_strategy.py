from design_patterns.strategy_pattern.strategy import Strategy


class UPSStrategy(Strategy):
    def calculate(self, order_price):
        return order_price * 0.45