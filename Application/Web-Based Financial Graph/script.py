from pandas_datareader import data
import datetime

start = datetime.datetime.now() - datetime.timedelta(days=10)
end   = datetime.datetime.now()

df = data.DataReader(name = "GOOG", data_source = "yahoo", start = start, end = end)
print(df)
