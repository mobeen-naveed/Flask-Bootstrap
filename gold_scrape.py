from bs4 import BeautifulSoup
import requests


def getGoldRates():
    
    url = "https://hamariweb.com/finance/gold_rate/"

    responseData = requests.get(url)
    soup = BeautifulSoup(responseData.text, 'html.parser')

    goldRateTableRows = soup.find('div', {'id':'main-content'}).find('table')
    return str(goldRateTableRows).replace('(Source:Karachi Saraf)', '')

    
if __name__ == "__main__":
    getGoldRates()





