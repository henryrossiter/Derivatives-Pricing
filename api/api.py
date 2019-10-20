import robin_stocks as r

def getCurrentAskPrice(stock):
  data = r.helper.request_get('https://api.robinhood.com/quotes/{}/'.format(stock), dataType='regular', payload=None, jsonify_data=True)
  try:
    ask_price = data['ask_price']
    return ask_price
  except:
    print('{} ask price not found'.format(stock))
    return
  
def getOptionData(stocks):
  optionData = r.find_options_for_list_of_stocks_by_expiration_date(stocks, optionType='call', expirationDate='2019-10-25')
  return optionData