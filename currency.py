import request
import json
import os

def get_rates():
    response = requests.get("http://api.currencylayer.com/live?access_key=ca0cdd8c332da1840ec1e46a16ece708&source=USD&currencies=RUB,TRY&format=1")
    usdrub = ((response.json())['quotes'])['USDRUB']
    usdtry = ((response.json())['quotes'])['USDRUB']
    text_file = open('rates.yaml', "w")
        n = text_file.write(f'usdrub: {usdrub}\n')
        n = text_file.write(f'usdtry: {usdtry}')
        text_file.close()
