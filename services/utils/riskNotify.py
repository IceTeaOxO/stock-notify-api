def calculate_stop_loss_and_take_profit(buy_price, stop_loss_percentage=0.95, take_profit_percentage=1.10):
    """
    根据买入价格计算建议的停损点和停利点。
    :param buy_price: 买入价格
    :param stop_loss_percentage: 停损点百分比，默认为买入价格的95%
    :param take_profit_percentage: 停利点百分比，默认为买入价格的110%
    :return: 停损点和停利点
    """
    stop_loss_price = buy_price * stop_loss_percentage
    take_profit_price = buy_price * take_profit_percentage
    
    return stop_loss_price, take_profit_price

# 示例使用
buy_price = 150  # 假设买入价格为150
stop_loss_price, take_profit_price = calculate_stop_loss_and_take_profit(buy_price)

print(f"建议买入价: {buy_price}")
print(f"停损点: {stop_loss_price}")
print(f"停利点: {take_profit_price}")
