import scraper_celeb_function as mps
# "https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1"
search_term='list_order,asc'
mode='detail'
url="https://www.imdb.com/list/ls068010962/?"
page=1
scrapped_products=[]
while True:
    starturl=f"{url}sort={search_term}&mode={mode}&page={page}"

    print('getting data from',starturl,'.........')
    soup=mps.get(starturl)
    if page==3:
        print('scrapper end')
        break
    else:
        output=mps.extract(soup)
        if len(output)==0:
            print('scrapper closed')
            break
        scrapped_products.extend(output)
        print('total size of collected data',len(scrapped_products))
        page=page+1
# save the stuff
mps.save(scrapped_products,'Celebrities_list.csv')
mps.pd.DataFrame(scrapped_products).head()