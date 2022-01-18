from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.jumia.co.ke/catalog/?q=blender').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_ = 'info')

def scraper():
    #creation of a dictionary holding values of the brands we want to count:
    brands = {'LYONS':0, 'NUNIX':0, 'RAMTONS':0, 'BRUHM':0, 'RASHNIK':0, 'SCARLETT':0, 'MIKA':0}
    lst = []
    #we iterate through the products list from the GET call and assign variables to each desired attribute:
    for product in products:
        # print(product.text)
        name = product.find('h3', class_ = 'name')
        # print(name.text)
        price = product.find('div', class_ = 'prc')
        # print(price.text)
        rating = product.find('div', class_ = 'stars _s')
        if rating is not None:
            rating = rating.text
        item = {'Product Name': name.text.upper(), 'Product Price': price.text, 'Product Rating': rating}
        lst.append(item)

    # print(lst)
    #print the list of dictionaries and count every instance a brand is found in the list:
    for item in lst:
        print(item, sep="\n")
        for brand in brands:
            if brand in item.get('Product Name'):
                brands[brand] += 1

    print(f'Total number of blenders found: {len(lst)}')

    branded = 0
    # print the list of all brands and the number of times they occur in the list
    for brand in brands:
        print(f"{brand}: {brands[brand]}")
        branded += brands[brand]

    # determine the number of unbranded/generic products in the list:
    generic = len(lst) - branded
    print(f'The sum of generic blenders: {generic}')


if __name__ == "__main__":
    scraper()