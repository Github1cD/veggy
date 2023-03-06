
import requests
from requests_html import HTML
import pandas as pd
import pprint
import re

class market_price:
    url=''
    def __init__(self):
        r= requests.get('https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price')
        if r.status_code == 200:
            self.html_text = r.text
        else:
            self.html_text = None
#converts the given url to th html text 


    def price(self,product):
        product = product.capitalize()
        html_text=self.html_text
        if html_text == None:
            return False
        r_html = HTML(html=html_text)
        t_class = '.Table'
        r_table = r_html.find(t_class)
        table_data=[]
        header_names =[]
        
        if len(r_table) == 0:
            return False
        parsed_table = r_table[0]
        rows = parsed_table.find('.Row')
        header_row = parsed_table.find('.Heading')[0]
        header_cols = header_row.find('.Cellth')
        header_names = [ x.text for x in header_cols]
        for row in rows:
            cols = row.find('.Cell')
            row_data =[]
            for col in cols:
                row_data.append(col.text)
            table_data.append(row_data)
    
        result ={}
        for table in table_data:
            for i in range(len(table)):
                if i == 0:
                    result[table[i]]={}
                else:
                    result[table[0]][header_names[i]] = table[i]
        for pdt in result:
            x = re.search(product,pdt)
            if x:
                return result[x.string]
            
            
                    
        
        
 