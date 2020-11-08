# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(pf['shares'] for pf in portfolio)
min_shares2 = min(portfolio, key=lambda s: s['shares'])

print(min_shares2['shares'])
