from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def get_categories():
    try:
        driver = webdriver.Edge()
        driver.get('https://books.toscrape.com/catalogue/category/books_1/index.html')
        elements = driver.find_elements(By.CSS_SELECTOR, '.side_categories ul li a')
        categories = []
        for element in elements:
            name = element.text.strip()
            link = element.get_attribute('href')
            categories.append({'Category': name, 'Link': link})
            
        df = pd.DataFrame(categories)
        df.to_csv('../data/categories.csv', index=False)
        driver.close()
        
    except Exception as e:
        print("Could not save category links.")
        print("Error:", e)
        
get_categories()