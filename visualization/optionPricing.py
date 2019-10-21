import numpy as np
import matplotlib.pyplot as plt

def optionPricingByStrike(price_dict, stock_name=None):
  strike_prices = []
  calculated_prices = []
  actual_buy_prices = []
  actual_sell_prices = []
  for option in price_dict:
    strike_prices.append(price_dict[option]['strike_price'])
    calculated_prices.append(price_dict[option]['calculated_price'])
    actual_buy_prices.append(price_dict[option]['actual_buy_price'])
    actual_sell_prices.append(price_dict[option]['actual_sell_price'])

  fig, ax = plt.subplots()

  ax.scatter(strike_prices, calculated_prices, c='#000000', label='Black Scholes Estimation')
  ax.scatter(strike_prices, actual_buy_prices, c='#21CE99', label='Robinhood High Fill Buy')
  ax.scatter(strike_prices, actual_sell_prices, c='#F45532', label='Robinhood High Fill Sell')

  ax.set_xlabel('Strike Price')
  ax.set_ylabel('Option Contract Value')
  if stock_name != None:
    ax.set_title('{} Call Option Pricing (15 Months until Expiration)'.format(stock_name))

  ax.legend()
  plt.show()