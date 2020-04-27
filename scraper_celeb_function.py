# libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
# data function
def get(url):
    #try:
        page=requests.get(url)
        if page.status_code==200:
            htmldata= page.text
            soup=BeautifulSoup(htmldata,'lxml')
            print('success')
            return soup
        else:
            print('error',page.status_code)
        '''except Execution as e:
        print(e)
        print('read this stuff carefully')'''
# extraction part
def extract(soup):
    page_products=[] # will hold the products from page
    #titles=soup.find_all('div',attrs={'class':'_3wU53n'})
    #prices= soup.find_all('div',attrs={'class':'_1vC4OE _2rQ-NK'})
    name=soup.find_all('img')
    link=soup.find_all('img')
    

    for n,l in zip(name,link):
        data={
            'name':n.get('alt'),
            'link':l.get('src'),
        }
        page_products.append(data)
    print('total product collected',len(page_products))
    return page_products
def save(dataset,filename='out.csv'):
    if len(dataset)>0:
        print('saving dataset')
        df=pd.DataFrame(dataset)
        df.to_csv(filename) # variable.to_fileformat(csv,excel)
        print ('saved file to', filename)
    else:
        print('could not save data')