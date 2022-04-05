from rakuten_rss_prime import rss
import pandas as pd
from price_logger import LastNPerfTime
import datetime

if __name__ == '__main__':
    a = datetime.datetime.now()
    print(a)
    store = pd.HDFStore("topix-series.hdf5")
    while True:
        a = datetime.datetime.now()
        temp = rss("1306.T", "現在値")
        
        store.append("topix", pd.DataFrame({"value":[temp], "now": [a]}))
    