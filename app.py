# dictionary of stock portfolio, track daily performance, total g/l
from yahoo_finance import Share
# documentation for this module at https://pypi.python.org/pypi/yahoo-finance

portfolio = \
{
    'dsx': 300,
    'kr': 36
}


# can iterate over the keys in the portfolio dictionary this way, implicitly calls .keys() method
for company in portfolio:
    close = Share(company).get_price()
    print(company+":  "+close)