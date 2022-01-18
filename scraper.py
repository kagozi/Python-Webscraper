from bs4 import BeautifulSoup
import requests

from collections import Counter

html_text = requests.get('https://www.amazon.com/s?k=blender&ref=nb_sb_noss').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_ = 'sg-col-inner')

brands = ['LYONS', 'NUNIX', 'RAMTONS', 'BRUHM', 'RASHNIK', 'SCARLETT']
i = 0  #The number of entries found
brand_count = 0
for product in products:
    print(product)
    # if product is not None:
    #     product = product.text
    #     print(product)
    #     i += 1
    #     product = product.upper()
    #     product.strip()
    #     # print(Counter(product))
    #     print(product)
    #     product_count = product.count('SCARLETT') 
    #     # for brand in brands:     
    #     #     product_count = product.count('SCARLETT') 

# for brand in brands:  
#     for product in products:   
#         brand_count += product.text.count(brand)   
#     print(f'{brand}: {brand_count}')

# print(product_count)
print(f"The number of blenders found is: {i} ")

"""
for product_name in enumerate(products):
    company = products.find('h3', class_ = 'joblist-comp-name')
    skills  = products.find('span', class_ = 'srp-skills')

    print(f"Company Name: {company.strip()}")
    print(f"Required Skills: {skills.strip()}")

    with open(f'posts/{index}.txt', 'w') as f:
        f.write(f"Company Name: {company.strip()} \n")
        f.write(f"Required Skills: {skills.strip()} \n")
    print(f'File saved: {index}')


        # print()
"""
""""
if __name__ == '__main__':
    while True:
        fun()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
"""
# with open('main.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     courses_tags = soup.find_all('h5')
#     for course in courses_tags:
#         print(course.text)