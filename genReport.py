import visualization.optionPricing as optionPricing
import api.api as api
import api.auth as auth
import utils.transforms as transforms
import xlwt 
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1') 
STOCKS = ['ACB', 'GE', 'F', 'FIT', 'GPRO'] #, 'CRON', 'HEXO', 'PLUG', 'ZNGA', 'CHK', 'NIO', 'APHA', 'GRPN', 'S', 'SIRI', 'CRBP', 'VSLR']
EXPIRATION_DATES = ['2019-11-01', '2019-11-08', '2019-11-15'] #, '2019-11-22', '2019-11-29', '2019-12-20', '2020-01-17']
auth.login()
i = 0
for STOCK in STOCKS:
  for DATE in EXPIRATION_DATES:
    try:
      current_options = api.getOptionData([STOCK], DATE)
      curr_price = api.getCurrentAskPrice(STOCK)

      price_dict = transforms.convertToPricable(current_options, curr_price)
      print(price_dict)
      for option in price_dict:
        sheet1.write(i, 0, STOCK) 
        sheet1.write(i, 1, DATE) 
        sheet1.write(i, 2, price_dict[option]['calculated_price']) 
        sheet1.write(i, 3, price_dict[option]['actual_buy_price']) 
        sheet1.write(i, 4, price_dict[option]['actual_sell_price']) 
        i+=1
      
    except:
      pass

wb.save('example.xls') 