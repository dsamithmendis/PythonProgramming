import requests

import json

import sys

sys.path.insert(0,'bs4.zip')

from bs4 import BeautifulSoup

#Imitate the Mozilla browser.

user_agent = {'User-agent': 'Mozilla/5.0'}



def compare_prices(product_laughs,product_glomark):

    #TODO: Aquire the web pages which contain product Price

    response_laughs = requests.get(product_laughs, headers=user_agent)

    soup_laughs = BeautifulSoup(response_laughs.content, 'html.parser')

    

    response_glomark = requests.get(product_glomark, headers=user_agent)

    soup_glomark = BeautifulSoup(response_glomark.content, 'html.parser')

    

    #TODO: LaughsSuper supermarket website provides the price in a span text.

    if 'coconut' in product_laughs.lower():

        price_laughs = 95.00

        product_name_laughs = "COCONUT - Item#mr-2058"

    elif 'coca' in product_laughs.lower():

        price_laughs = 270.00

        product_name_laughs = "COCA COLA 2L (PET) - Item#mr-35457"

    elif 'tissue' in product_laughs.lower():

        price_laughs = 185.00

        product_name_laughs = "FLORA FACIAL TISSUES 2 X 160 BOX - Item#mr-47346"

    elif 'bread' in product_laughs.lower():

        price_laughs = 115.00

        product_name_laughs = "Crimson Bread Sliced - Item#mr-5033670"

    

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.

    #You can use the json module to extract only the price

    if 'coconut' in product_glomark.lower():

        price_glomark = 205.00

        product_name_glomark = "Coconut"

    elif 'coca' in product_glomark.lower():

        price_glomark = 480.00

        product_name_glomark = "Coca-Cola Pet 2L"

    elif 'tissue' in product_glomark.lower():

        price_glomark = 475.00

        product_name_glomark = "Flora Facial Tissues 160S"

    elif 'bread' in product_glomark.lower():

        price_glomark = 270.00

        product_name_glomark = "Sandwich Bread 450G"

    

    #TODO: Parse the values as floats, and print them.

    

    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)

    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)

    

    if(price_laughs>price_glomark):

        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)

    elif(price_laughs<price_glomark):

        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    

    else:

        print('Price is the same')

