import time
import I2C_LCD_driver
import requests
eth_address = "bitcoincash:qzs02v05l7qs5s24srqju498qu55dwuj0cx5ehjm2c"  # your ethereum address goes here
site = "https://rest.bitcoin.com/v2/address/details/"
mylcd = I2C_LCD_driver.lcd()

final_site = site + eth_address
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
res = requests.get(final_site,hdr)

jsondata = res.json()
h = 'BCH 4 LYF'
#print(jsondata)
print(jsondata['balance'])
#print(res.status_code)
x = 0
mylcd.lcd_display_string(h,2)
while 1==1:
	print(x)
	res = requests.get(final_site,hdr)
	jsondata = res.json()
	balance = str(jsondata['balance'])
	mylcd.lcd_display_string(balance, 1)

	time.sleep(5)
	x= x+1
