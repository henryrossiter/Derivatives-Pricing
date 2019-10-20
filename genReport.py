import api.getOptions as getOptions
import api.auth as auth
import pricing.blackscholes as blackscholes
from datetime import datetime

auth.login()
current_options = getOptions.getOptionData(['fb'])
pricing_data_dict = {}
for option in current_options:
  pricing_data_dict[option['id']] = {
    'strike_price': option['strike_price'],
    'expiration_date': option['expiration_date'],
    'implied_volatility': option['implied_volatility'],
    'share_price': 185.85,
    'risk_free_interest_rate': .01,
    'high_fill_rate_buy_price': option['high_fill_rate_buy_price']
  }

price_dict = {}
for option in pricing_data_dict:
  try:
    share_price = float(pricing_data_dict[option]['share_price'])
    strike_price = float(pricing_data_dict[option]['strike_price'])
    implied_volatility = float(pricing_data_dict[option]['implied_volatility'])
    def days_between(d1):
      d1 = datetime.strptime(d1, "%Y-%m-%d")
      d2 = datetime.now()
      return (d1 - d2).days / 365
    years_until_expiry = days_between(pricing_data_dict[option]['expiration_date'])

    calculated_price = blackscholes.callPrice(share_price, strike_price, .015, implied_volatility, years_until_expiry)
    actual_price = float(pricing_data_dict[option]['high_fill_rate_buy_price'])
    price_dict[option] = {
      'calculated_price': calculated_price,
      'actual_price': actual_price
    }
  except:
    print('one option was not found')

for item in price_dict:
  print(price_dict[item])