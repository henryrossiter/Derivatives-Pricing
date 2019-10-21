import visualization.optionPricing as optionPricing
import api.api as api
import api.auth as auth
import utils.transforms as transforms

#STOCK = 'TSLA'
STOCKS = ['ACB', 'GE', 'F', 'FIT', 'GPRO', 'CRON', 'HEXO', 'PLUG', 'ZNGA', 'CHK', 'NIO', 'APHA', 'GRPN', 'S', 'SIRI', 'CRBP', 'VSLR']
EXPIRATION_DATES = ['2019-11-01', '2019-11-08', '2019-11-15', '2019-11-22', '2019-11-29', '2019-12-20', '2020-01-17']
auth.login()
for STOCK in STOCKS:
  for DATE in EXPIRATION_DATES:
    try:
      current_options = api.getOptionData([STOCK], DATE)
      curr_price = api.getCurrentAskPrice(STOCK)

      price_dict = transforms.convertToPricable(current_options, curr_price)
      optionPricing.optionPricingByStrike(price_dict, stock_name=STOCK)
    except:
      pass