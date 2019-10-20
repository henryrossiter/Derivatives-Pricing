import robin_stocks as r


def getOptionData(stocks):
  optionData = r.find_options_for_list_of_stocks_by_expiration_date(stocks, optionType='call', expirationDate='2019-10-25')
  return optionData