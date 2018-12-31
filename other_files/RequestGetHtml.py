import datetime
import requests

print("requests version: " + requests.__version__)

r = requests.get('https://finance.yahoo.com/quote/USDAUD=X/')

#filename has issues with spaces, colons and periods, replace all with compatible characters
now = str(datetime.datetime.now()).replace(" ", "_").replace(":", "-").replace(".", "-")


f = open("yahoo-" + now + ".html","w+")
f.write(r.text)
f.close()
