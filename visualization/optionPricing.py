import numpy as np
import matplotlib.pyplot as plt

def optionPricingByStrike(price_dict):
  strike_prices = []
  calculated_prices = []
  actual_prices = []
  for option in price_dict:
    strike_prices.append(price_dict[option]['strike_price'])
    calculated_prices.append(price_dict[option]['calculated_price'])
    actual_prices.append(price_dict[option]['actual_price'])

  fig, ax = plt.subplots()

  ax.scatter(strike_prices, calculated_prices, label='Black Scholes Estimation')
  ax.scatter(strike_prices, actual_prices, label='Actual Price')

  ax.legend()
  plt.show()