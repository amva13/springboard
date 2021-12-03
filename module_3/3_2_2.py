from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=graphics+cards"

# download webpage unto a client
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# test
# print(page_soup.h1)

# what type of containers are we looking for ?
containers = page_soup.findAll("div",{"class":"item-container"})

# file
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    try:
        brand = container.div.div.a.img["title"].replace(",","|")
        title_container = container.findAll("a", {"class":"item-title"})[0]
        product_name = title_container.text.replace(",","|")
        shipping_container = container.findAll("li",{"class":"price-ship"})[0]
        shipping = shipping_container.text.strip().replace(",","|")
        f.write(brand+","+product_name+","+shipping+"\n")
    except:
        pass
