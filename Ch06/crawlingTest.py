from bs4 import BeautifulSoup

f = open('test.html', 'r', "utf-8")
html_test = f.read()
#print(html_test)
soup = BeautifulSoup(html_test, 'html.parser')
print(soup.prettify())
