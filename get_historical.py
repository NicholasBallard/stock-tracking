# get-historical.py
'''
Import this function into app.py
Use it to write the daily p/l for the portfolio by day \
for a date range.
'''

from yahoo_finance import Share
import datetime
import pandas as pd

def history( stock_portfolio , start_date , end_date ):
  date = start_date
  while date <= end_date:
    day_change = 0
    for company in portfolio:
      close = Share(company).get_price()
      previous = Share(company).get_prev_close()
      change = close - previous
      day_change += change
    # TODO: Write `day_change` to price-tracker.txt as `date  , day_change r'\n`
    # date.strftime("%m-%d-%Y") + "\t,\t" + day_change
    historical = pd.DataFrame(, columns=list('date', 'gain/loss'))
    date += 1