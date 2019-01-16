from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
my_address = Request("https://realpython.com/practice/dionysus.html", headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(my_address)
html_text = html_page.read() # Py 3: decode
my_soup = BeautifulSoup(html_text, features="lxml")
text = my_soup.get_text()
print(text.strip())