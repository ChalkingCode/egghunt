import bs4
import requests
from bs4 import BeautifulSoup as soup
import re

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
# choose your page number to scrape
page_number = input('Please, enter a page number:\n')
formated_page_number = page_number.replace(' ', '+')
print(f'Searching {page_number}. Wait, please...')
page_url = f"https://www.newegg.com/p/pl?d=graphic+cards&page={formated_page_number}"
print(page_url)
uClient = requests.get(page_url, verify=False)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.text, "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "item-container"})

# name the output file to write to local disk
file_name = input('Please, enter a name for csv file:\n')
formated_file_name = file_name.replace(' ', '+')
print(f'Searching {file_name}. Wait, please...')
out_filename = f"{formated_file_name}.csv"
print(out_filename)
# header of csv file to be written
headers = "brand,product_name,shipping \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
    # Finds all link tags "a" from within the first div.
    make_rating_sp = container.div.select("a")

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    try:
        brand = make_rating_sp[0].img["title"].title()
    except TypeError:
        continue

    

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = container.div.select("a")[2].text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    # prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    # writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()  # Close the file
