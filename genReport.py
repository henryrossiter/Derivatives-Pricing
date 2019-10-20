import api.api as api
import api.auth as auth
import pricing.blackscholes as blackscholes
import utils.transforms as transforms

auth.login()
current_options = api.getOptionData(['MSFT'])
curr_price = api.getCurrentAskPrice('MSFT')

price_dict = transforms.convertToPricable(current_options, curr_price)

for item in price_dict:
  print(price_dict[item])