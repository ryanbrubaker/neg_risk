import json
import sys
import time
import urllib
import winsound

# Put any markets you want to ignore in this array
IGNORE_MARKETS = []

USE_BEEP = False
if len(sys.argv) == 2 and sys.argv[1] == 'sound':
    USE_BEEP = True

while True:
    link = 'https://www.predictit.org/api/marketdata/all/'
    connection = urllib.urlopen(link)
    data = connection.read()
    marketData = json.loads(data)

    markets = marketData['markets']
    for market in markets:
        market_name = market['name']
        market_url = market['url']
    
        neg_potential = 0.0
        contracts = market['contracts']
        for contract in contracts:
            if None != contract['bestBuyNoCost']:
                neg_potential += (1 - contract['bestBuyNoCost'])

        if neg_potential >= 1.11 and market_url not in IGNORE_MARKETS:
            if USE_BEEP:
                winsound.Beep(450, 1000)
            print('\n\n\n\t\t' + market_name)
            print('\t\t' + market_url)
            print('\t\t{0}'.format(neg_potential))
            print('\n\n\n')

    sys.stdout.write('.')
    time.sleep(60)
