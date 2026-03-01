from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_csv('data/categories.csv')
df.drop(index=0, inplace=True)
cat_dict = dict(zip(df['Category'], df['Link']))
driver = webdriver.Edge()

for category, link in cat_dict.items():
    with open(f"data/html/{category}.html", 'w', encoding='UTF-8') as file:
        current_url = link  
        while True:
            driver.get(current_url)
            elements = driver.find_elements(By.CLASS_NAME, 'product_pod')
            
            for element in elements:
                file.write(element.get_attribute("outerHTML"))
            
            next_btn = driver.find_elements(By.CLASS_NAME, 'next')
            if not next_btn:
                break  
            next_url = next_btn[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
            # print(next_url)
            current_url = next_url
driver.close()
    
    

