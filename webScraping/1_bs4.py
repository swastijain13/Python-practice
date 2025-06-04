from bs4 import BeautifulSoup

with open("file.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

print("Title tag: " , soup.title) #title tag

print("\n")

print("Title text : " , soup.title.text) #title name(only)

print("\n")

print("Parent tag of title : ", soup.title.parent.name)
print("\n")

print("First paragraph tag : ", soup.p)
print("\n")

# print("Class attribute of first paragraph class : ", soup.p['class'])
# print("\n")

print("First anchor tag : ", soup.a)
print("\n")

# print("All anchor tags : ", soup.find_all('a'))
# print("\n")

# print("Tag with id=link3 : ", soup.find(id="link3"))