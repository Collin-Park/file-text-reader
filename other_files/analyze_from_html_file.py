#import beautifulsoup and an html parser
from bs4 import BeautifulSoup
try:
  from lxml import etree
  print("running with lxml.etree")
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

#open the file, specify the encoding
with open("index.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'lxml')

# this should spit out the S&P500 index level
print(soup.find(class_='IsqQVc NprOob ijJhl_1D__vU-zJFzKq8ukm8').text)
