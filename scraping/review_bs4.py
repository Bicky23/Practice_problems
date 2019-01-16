# import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# grab full HTML page
url = Request("https://realpython.com/practice/profiles.html", headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(url)
html_text = html_page.read() 
my_soup = BeautifulSoup(html_text, features="lxml")

# look for HTML tag "a" and retrieve "href" attribute
tags = my_soup.find_all("a")
print(tags)
hrefs = [tag["href"] for tag in tags]
print(hrefs)
print('-'*50)

# go to every link in "hrefs" and display its text(without HTML)
for link in hrefs:
    url = Request("https://realpython.com/practice/"+link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(url)
    text = html.read()
    soup = BeautifulSoup(text, features="lxml")
    print(soup.get_text())
    print('='*100)