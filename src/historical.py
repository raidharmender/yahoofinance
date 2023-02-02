from datetime import datetime
import time
from typing import Final
import pandas as pd

YAHOO_URL: Final = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_time}&period2={end_time}&interval={interval}&events=history"

class YahooFinance(object):
    def __init__(self, interval="1d"):
        self.base_url = YAHOO_URL
        self.interval = interval

    def __build_url(self, ticker: str, start_date: datetime, end_date: datetime):
        return self.base_url.format(ticker=ticker, start_time=start_date, end_time=end_date, interval=self.interval)

    def get_ticker_df(self, ticker: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        start_date = int(time.mktime(start_date.timetuple()))
        end_date = int(time.mktime(end_date.timetuple()))
        df = pd.read_csv(self.__build_url(ticker, start_date, end_date))

        return df

def main():
    dh = YahooFinance()
    start_date = datetime.strptime("01/01/2010", "%d/%m/%Y")
    end_date = datetime.strptime("31/12/2022", "%d/%m/%Y")
    for ticker in ["MSFT","BITO", "VOO"]:
        df = dh.get_ticker_df(ticker, start_date, end_date)
        df.drop(columns=["Volume","Open","High","Low", "Adj Close"], inplace=True)
        df.to_csv(f"../data/{ticker}.csv")

if __name__ == '__main__':
    main()
