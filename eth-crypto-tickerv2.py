#! /usr/bin/env python

import requests, json
from os.path import expanduser

home = expanduser('~')

def parse():
    ethereum = Ethereum()    
    file_write(ethereum)

def Ethereum():
    info = []
    price_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/price"
    r = requests.get(price_url)
    jsn_dict = r.json()
    price = jsn_dict['usd']
    volume_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/volume"
    t = requests.get(volume_url)
    jsn_dict2 = t.json()
    volume = jsn_dict2['usd']
    change_url = "http://coinmarketcap-nexuist.rhcloud.com/api/eth/change"
    e = requests.get(change_url)
    change = e.json()
    info.extend((price, volume, change))
    return info

def file_write(ethereum):    
    ethprice = ethereum[0]
    ethvolume = ethereum[1]
    ethchange = ethereum[2]
    file = open("%s/conky-ethereum-ticker-with-graph-chart-master/eth-price-percentage.txt" % home, 'w')    
    file.write("ETH:           $%.2f         %s%% \n" % (ethprice, ethchange))
    file.close

parse()
