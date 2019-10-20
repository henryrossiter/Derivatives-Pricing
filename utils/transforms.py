from datetime import datetime
import pricing.blackscholes as blackscholes

def convertToPricable(options, curr_price):
  pricing_data_dict = {}
  for option in options:
    pricing_data_dict[option['id']] = {
      'strike_price': option['strike_price'],
      'expiration_date': option['expiration_date'],
      'implied_volatility': option['implied_volatility'],
      'share_price': curr_price,
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
      strike_price = float(pricing_data_dict[option]['strike_price'])
      price_dict[option] = {
        'strike_price': strike_price,
        'calculated_price': calculated_price,
        'actual_price': actual_price
      }
    except:
      print('option not found')
  return price_dict