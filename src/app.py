import requests
from bs4 import BeautifulSoup # from bs4 file import BeautifulSoup class

website = "https://www.flipkart.com/the-lean-startup/p/itmfc8qf72rxfhfa?pid=9780670921607&lid=LSTBOK97806709216070FHJIM&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=2e1ca8e0-78d8-41d3-8da2-67d67a76be7a.9780670921607.SEARCH&ppt=sp&ppn=sp&ssid=yimmnb60s00000001579715597727&qH=c19186675fec67bb"
# In the request variable the page information are going to store
request = requests.get(website)

# in content variable the html code of that website(here flipkart.com) is going to be stored
content = request.content

# soup variable
soup = BeautifulSoup(content, "html.parser")
# <div class="_1vC4OE _3qQ9m1">₹420</div> //  html element
element = soup.find("div", {"class" : "_1vC4OE _3qQ9m1"})

# item_price is going to store a string value like this "₹420"
item_price = element.text.strip()

# converted floating value is stored in price variable
price = float(item_price[1:])

# here is the comparision with our desired buying price and actual price
if price <= 400:
    print("Buy the book and the price of the book is {}".format(price))
else:
    print("No.. the price is {}, wait until the price goes down...".format(price))