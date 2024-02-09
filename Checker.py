import requests

def check_binance_availability(coins):
    base_url = 'https://api.binance.com/api/v3/exchangeInfo'
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        symbols = [symbol['symbol'] for symbol in data['symbols']]
        
        available_coins = []
        unavailable_coins = []
        
        for coin in coins:
            if coin.upper() in symbols:
                available_coins.append(coin.upper())
            else:
                unavailable_coins.append(coin.upper())
        
        if available_coins:
            print("Available coins on Binance:", available_coins)
        if unavailable_coins:
            print("Unavailable coins on Binance:", unavailable_coins)
        
    else:
        print("Failed to retrieve data from Binance API")

# Define the lists of coins
list_1 = ["BNBUSDT", "BTCUSDT", "ETHUSDT", "YGGUSDT", "XRPUSDT", "REIUSDT", "STMXUSDT", "LTCUSDT", "SOLUSDT", "DOGEUSDT", "ZILUSDT", "WAVESUSDT", "VETUSDT"]
list_2 = ["AKROUSDT", "TRXUSDT", "ADAUSDT", "WLDUSDT", "OPUSDT", "MATICUSDT", "SHIBUSDT", "LINKUSDT", "XLMUSDT", "TOMOUSDT", "EOSUSDT", "NEOUSDT", "FETUSDT"]
list_3 = ["CELOUSDT", "ILVUSDT", "SCRTUSDT", "ASRUSDT", "UNIUSDT", "DOTUSDT", "WBTCUSDT", "ARBUSDT", "COMPUSDT", "CHZUSDT", "ETCUSDT", "GLMRUSDT"]
list_4 = ["BCHUSDT", "SNXUSDT", "SUIUSDT", "MKRUSDT", "FTMUSDT", "AVAXUSDT", "KNCUSDT", "INJUSDT", "APTUSDT", "LINAUSDT", "SXPUSDT", "DASHUSDT", "MOVRUSDT"]
list_5 = ["WINGUSDT", "GALAUSDT", "KAVAUSDT", "OGNUSDT", "LDOUSDT", "DYDXUSDT", "SANDUSDT", "NEARUSDT", "GMXUSDT", "MASKUSDT", "XTZUSDT", "ICXUSDT"]
list_6 = ["STXUSDT", "EGLDUSDT", "ATOMUSDT", "XMRUSDT", "APEUSDT", "ICPUSDT", "GRTUSDT", "AAVEUSDT", "AXSUSDT", "QNTUSDT", "ZECUSDT", "LSKUSDT"]

# Check availability for each list
for i, lst in enumerate([list_1, list_2, list_3, list_4, list_5, list_6], start=1):
    print(f"Checking List {i}:")
    check_binance_availability(lst)
    print()
