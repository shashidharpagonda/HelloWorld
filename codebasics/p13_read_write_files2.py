'''
stocks.csv contains stock price, earnings per share and book value.

You are writing a stock market application that will process this file and
create a new file with financial metrics such as pe ratio and price to book ratio.
These are calculated as,
    pe ratio = price / earnings per share
    price to book ratio = price / book value
'''

'''
Your input format (stocks.csv) is,

Company Name	Price	Earnings Per Share	Book Value
Reliance	1467	66	653
Tata Steel	391	89	572

Output.csv should look like this,

Company Name	PE Ratio	PB Ratio
Reliance	22.23	2.25
Tata Steel	4.39	0.68
'''

stocknames=[]
prices=[]
earningsPerShare=[]
bookValue=[]

headers=['Company Name','PE Ratio','PB Ratio']

with open('codebasics_files\\stocks.csv','r') as f, open('codebasics_files\\stocks_output.csv','w') as f_out:
    f_out.write('Company Name,PE Ratio,PB Ratio\n')
    next(f)  #It will skip 1st line from stocks.csv
    for line in f:
        tokens=line.split(',')
        stockname=tokens[0]
        price=float(tokens[1])
        eps=float(tokens[2])
        bv=float(tokens[3])
        pe_ratio=round(price/eps)
        bv_ratio=round(price/bv)
        f_out.write(f'{stockname},{pe_ratio},{bv_ratio}\n')
