from bs4 import BeautifulSoup
import pandas as pd
import os 

book_dict = {'Category':[],
             'Book title':[],
             'Book price':[]
    }
for file in os.listdir('data/html'):
    category = file.removesuffix('.html')
    
    with open(f"data/html/{file}",'r', encoding='UTF-8') as file:
        html_text = file.read()
        soup = BeautifulSoup(html_text, 'html.parser')
        book = soup.find_all('article', class_ = 'product_pod')
        
        for b in book:
            book_title = b.h3.a['title']
            price = b.find('p',class_ = 'price_color').text.removeprefix('Â')
            book_dict['Category'].append(category)
            book_dict['Book title'].append(book_title)
            book_dict['Book price'].append(price)

df = pd.DataFrame(book_dict)
df.to_csv("data/category books.csv")