import csv

def load_portfolio(portfolio_list_files):
    portLists = []
    with open(portfolio_list_files, mode='r') as portfile:
        for line in csv.reader(portfile):
            portLists.append(line[0].split(';'))
    return portLists[1:]

# Loading Portfolio
print('Loading Portfolio List!')
for link, cat, title in load_portfolio('static/portfolio/list.csv'):
    print(link)
print('Loading Portfolio Done!')