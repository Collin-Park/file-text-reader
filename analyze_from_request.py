#import beautifulsoup and an html parser
import datetime
from bs4 import BeautifulSoup
try:
  from lxml import etree
#  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")
import requests

#if you want to look at the version, print("requests version: " + requests.__version__)

#I'll use this to look up the usd to aud conversion rates which is of interest to me.
print('USD to AUD conversion rates:')

#request the html, specify the encoding
r = requests.get('https://finance.yahoo.com/quote/USDAUD=X/')
#use .text to get the html from the get request
fp = r.text
soup = BeautifulSoup(fp, 'lxml')

#print out the data, alternatively we can import datetime, and create a daily csv of exchange rates,
print(soup.find('td', attrs={"data-reactid": "33"}).text +': '+ (soup.find('td', attrs={"data-reactid": "35"}).text))

print(soup.find('td', attrs={"data-reactid": "37"}).text +': '+ (soup.find('td', attrs={"data-reactid": "39"}).text))

# we are interested in if it's a good time to exchange usd to aud.
high52weekslist = (soup.find('td', attrs={"data-reactid": "35"}).text).split()
high52weeks = float(high52weekslist[-1])
low52weeks = float(high52weekslist[0])
currentprice = float(soup.find('td', attrs={"data-reactid": "39"}).text)

print("currently " + str(currentprice/high52weeks*100) + " of the value from all time highs")
now = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-").replace(".", "-")

newRow = now + ", " + str(low52weeks) + ", " + str(high52weeks) + ", " + str(currentprice) + "\n"
print(newRow)


f = open("USDAUD_exchange_rate.csv","a")
f.write(newRow)
