import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
import time
import random


def beer(start, stop):
    link_dfs = [] 
    for i in range(start,stop+1):
        ua = UserAgent()
        user_agent = {'User-agent': ua.random}
        if i == 1:
            page_num = ""
        else:
            page_num = f"page/{i}"
        url_links = f'https://www.brewersfriend.com/homebrew-recipes/{page_num}'
        response_url = requests.get(url_links, headers = user_agent)
        page_url = response_url.text
        soup_url = BeautifulSoup(page_url, 'lxml')
    
        link_dict = {}
        titles = []
        values = []
        for r_title in soup_url.find_all(class_='recipetitle'):
            r_title = r_title.text
            titles.append(r_title)
        for a in soup_url.find_all('a', class_='recipetitle', href=True):
            value = a['href']
            values.append(value)
            #link_dict[r_title] = a['href']
        link_dict = dict(zip(titles, values))
        
        link_df = pd.DataFrame(link_dict, index = ['beer']).T
        link_dfs.append(link_df)
    
    all_links = pd.concat(link_dfs)

    #ua = UserAgent()
    #user_agent = {'User-agent': ua.random}
    dicts = []
    dfs = []
    for row in range(len(all_links)):
        #ua = UserAgent()
        #user_agent = {'User-agent': ua.random}
        #print(user_agent)
        time.sleep(.4+2.2*random.random())
        req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        url = f'https://www.brewersfriend.com{all_links.beer[row]}'
        response = requests.get(url, headers = req_headers)
        if response.status_code != 200:
            #raise ValueError("Website unresponsive")
            print(f'#{row} unresponsive')
            continue
        page = response.text 
        soup = BeautifulSoup(page, 'lxml')
        
        beer_dict= {}
        recipe = []
        for item in soup.find_all('div', class_='forminput'):
            recipe.append(item)
        split_r = str(recipe).split('\r\n')
        recl = str(recipe)
        try:
            #title
            title = recl[recl.index('Title:') +7 : recl.index("Author:")-4]
        except:
            pass
        try:
            #style
            style = recl[recl.index('Style Name:') +12 : recl.index('Boil Time:') -2]
        except:
            pass
        try:
            # stats
            stats = recl[recl.index('STATS:') +8  : recl.index('FERMENTABLES')-4]
            stats = stats.replace('\r\n', ',').split(',')
            def list_to_dict(stats):
                return dict(map(lambda s : s.split(':'), stats))
            stats_dict = list_to_dict(stats)
        except:
            pass
        
        try:
            #ferms 
            ferms = recl[recl.index('FERMENTABLES:') +15: recl.index('HOPS')-4]
            ferms = ferms.replace('\r\n', ',').split(',')
        except:
            pass
        try:
            #hops
            hops = recl[recl.index('HOPS:') + 7: recl.index('MASH GUIDELINES:')-4]
            hops = hops.replace('\r\n', ',').split(',')
        except:
            pass
        try:
            # others
            others = recl[recl.index('OTHER INGREDIENTS:') + 20: recl.index('YEAST:')-4]
            others = others.replace('\r\n', ',').split(',')
        except:
            pass
        
        try:
            #yeast
            yeast = recl[recl.index('YEAST:') + 8: recl.index('PRIMING:')-4]
            yeast = yeast.replace('\r\n', ',').split(',')
        except:
            pass
        
        try:
            #co2
            co2 = recl[recl.index('CO2 Level') : recl.index('TARGET WATER')-4]
        except:
            pass
        
        try:
            #water 
            water = recl[recl.index('TARGET WATER PROFILE') + 23: recl.index('NOTES:')-4]
            water = water.replace('\r\n', ',').split(',')
        except:
            pass
        try:
            #notes
            notes = recl[recl.index('NOTES:') + 8: recl.index('This recipe has been')-4]
            notes.replace('\r\n', ',').split(',')
        except:
            pass
        
        #put it all together
        try:
            beer_dict['title'] = title
        except:
            pass
        try:
            beer_dict['style'] = style
        except:
            pass
        try:
            beer_dict.update(stats_dict)
        except:
            pass
            beer_dict['ferms'] = ferms
        try:
            beer_dict['hops'] = hops
        except:
            pass
        try:
            beer_dict['yeast'] = yeast
        except:
            pass
        try:
            beer_dict['others'] = others
        except:
            pass
        try:
            beer_dict['co2'] = co2
        except:
            pass
        try:
            beer_dict['water'] = water
        except:
            pass
        try:
            beer_dict['notes'] = notes
        except:
            pass
        
        print(f'getting row {row}')
        #df = pd.DataFrame(beer_dict, index = ["beer"])
        dicts.append(beer_dict)

    concat_dfs = pd.DataFrame(dicts)


    return concat_dfs 