from urllib.request import urlopen, Request
import re

url = Request("https://realpython.com/practice/dionysus.html", headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(url)
text = html.read().decode('utf-8')
print(text)

# regex to find "Name" and "Favorite Color"
match_name = re.search("Name:.*?<", text)
name = (re.sub(".*:", "", match_name.group()).strip()).strip('<')

match_color = re.search("Color:.*?[\n]<", text)
color = (re.sub(".*:", "", match_color.group()).strip('\n<')).strip()

print("Name is:", name.strip(), "with length", len(name))
print("Color is:", color, "with length", len(color))
