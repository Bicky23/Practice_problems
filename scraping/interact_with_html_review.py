# import packages
import mechanicalsoup
import warnings
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')

# set up browser
my_browser = mechanicalsoup.Browser()

# retrieve page
page = my_browser.get("https://realpython.com/practice/login.php")

# HTML content
html = page.soup
print('='*100)
form = html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# submit form
profiles_page = my_browser.submit(form, page.url)

# get title
print("Title is:", profiles_page.soup.title.text) # make sure we were redirected
print('='*100)

# navigate back to login page and show title
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_title = login_page.soup.title
print("Title: ", login_title.text)

