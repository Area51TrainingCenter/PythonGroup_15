import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

# object BeatifulSoup
print('Tipo: {}\nEstructura: {}'.format(type(soup), dir(soup)))

print('Título en html: {}\nNombre del título: {}\nContenido del título: {}'
      .format(soup.title, soup.title.name, soup.title.string))
print(type(soup.title))

print()
# object Tag
print(type(soup.h1))
print(soup.h1)
print(soup.h1.string)
print(soup.h1['class'])
print(soup.h1['id'])
print(soup.h1.attrs)


print()
soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']

print(soup.h1)

print()
for i, h2 in enumerate(soup.find_all('h2')):
    print(i, h2.text)
print()

print(soup.p.a)
print(soup.p.find_all('a'))
print()

print(soup.find_all('p')[1].a)
p = soup.find_all('p')[1]
print()

print(p.contents)
print(p.contents[6])

print(p.children)
for child in p.children:
    print(type(child), child, child.name, sep=' ')
print()
print(p.a.previous_sibling)
print(p.a)
print(p.a.next_sibling)
