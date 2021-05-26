#this script download current list of stocks from GPW in format that is easily consumable by systemtrader (very useful for AEM strategy on GPW)
#data come from stooq.pl
#libraries required: selenium | in cmd: pip3 install selenium | pip3 install chromedriver-binary
#if chromedriver version does not match chrome version - find out the latest correspoding version from https://sites.google.com/chromium.org/driver/ and run pip3 install chromedriver-binary==proper_version
from selenium import webdriver
import chromedriver_binary # adds chromedriver binary to path
import pandas as pd

WIG20 = 'https://stooq.pl/t/?i=532'
mWIG40 = 'https://stooq.pl/t/?i=533'
sWIG80 = 'https://stooq.pl/t/?i=588'

output_csv = r'C:\Users\krzyc\Documents\gpw.txt'

a = []
b = []

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(WIG20)

#identify elements
tickers_WIG20 = driver.find_elements_by_xpath('//a[contains(@href, "q/?s=")]')
stocks_WIG20 = driver.find_elements_by_id('f10')
for ticker in tickers_WIG20:
    #eliminate all non tickers (tickers are only 3digits)
    if len(ticker.get_attribute('innerHTML')) == 3:
        a.append(ticker.get_attribute('innerHTML'))

for stock in stocks_WIG20:
    if stock.size == {'height': 21, 'width': 164}:
        b.append(stock.get_attribute('innerHTML'))

driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(mWIG40)

#identify elements
tickers_mWIG40 = driver.find_elements_by_xpath('//a[contains(@href, "q/?s=")]')
stocks_mWIG40 = driver.find_elements_by_id('f10')
for ticker in tickers_mWIG40:
    #eliminate all non tickers (tickers are only 3digits)
    if len(ticker.get_attribute('innerHTML')) == 3:
        a.append(ticker.get_attribute('innerHTML'))

for stock in stocks_mWIG40:
    if stock.size == {'height': 21, 'width': 177}:
        b.append(stock.get_attribute('innerHTML'))

driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(sWIG80)

#identify elements
tickers_sWIG80 = driver.find_elements_by_xpath('//a[contains(@href, "q/?s=")]')
stocks_sWIG80 = driver.find_elements_by_id('f10')
for ticker in tickers_sWIG80:
    #eliminate all non tickers (tickers are only 3digits)
    if len(ticker.get_attribute('innerHTML')) == 3:
        a.append(ticker.get_attribute('innerHTML'))

for stock in stocks_sWIG80:
    #get_attribute() to get all href

    if stock.size == {'height': 21, 'width': 164}:
        #print(stock.get_attribute('innerHTML'))
        b.append(stock.get_attribute('innerHTML'))

driver.quit()

df = pd.DataFrame({"Ticker": a, "Stock": b})
#concatenate values in to one column consumable
df['Systemtrader input'] = df[["Ticker","Stock"]].agg('|'.join, axis=1)
#print(df)
df['Systemtrader input'].to_csv(output_csv, index=None, header=None)
print('SUCCESS !')