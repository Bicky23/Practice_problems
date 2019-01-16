from urllib.request import urlopen, Request
import re
# start_tag = "<title>"
# end_tag = "</title>"
# start_index = html_text.find(start_tag) + len(start_tag)
# end_index = html_text.find(end_tag)
# print(html_text[start_index:end_index])
url = Request("https://realpython.com/practice/dionysus.html", headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(url)
text = html.read().decode('utf-8')
print(text)
match_results = re.search("<title.*?>.*</title .*?>", text, re.IGNORECASE)
print(match_results.group())