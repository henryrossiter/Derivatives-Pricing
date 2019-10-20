import visualization.optionPricing as optionPricing
import api.api as api
import api.auth as auth
import utils.transforms as transforms

STOCK = 'MSFT'
auth.login()
current_options = api.getOptionData([STOCK])
curr_price = api.getCurrentAskPrice(STOCK)

price_dict = transforms.convertToPricable(current_options, curr_price)
optionPricing.optionPricingByStrike(price_dict)