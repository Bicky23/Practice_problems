# import packages
import mechanicalsoup
import warnings
warnings.filterwarnings('ignore')

# set up browser
my_browser = mechanicalsoup.Browser()

# retrieve page
page = my_browser.get("https://realpython.com/practice/login.php")

# HTML content
html = page.soup
print(html)
print('='*100)
form = html.select("form")[0]
# print(form.select("input")[0])
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# submit form
profiles_page = my_browser.submit(form, page.url)
print(profiles_page.url) # make sure we were redirected
print('='*100)
print(profiles_page.soup) # show html 
print('='*100)

for link in profiles_page.soup.select("a"):
    print("Address:", link["href"])
    print("Text:", link.text)
    print('='*100)