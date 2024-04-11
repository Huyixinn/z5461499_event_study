f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
remove = []
for x in f_suburbs:
    if not x.startswith("F"):
        remove.append(x)
for x in remove:
    f_suburbs.remove(x)
print(f_suburbs)



count = 2

while True:

    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        break

    count = count + 1

print(count)



def fizz_buzz_sumz(i):
    sum = 0
    for n in range(0,i+1):
        if n % 3 == 0:
            if n % 5 == 0:
                continue
            else:
                sum = sum + 3*n
        elif n % 5 == 0:
            sum = sum + 5*n
        else:
            sum = sum + n
    print(sum)
    return sum
fizz_buzz_sumz(10)




prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression

sorted_keys = sorted(prc_dic.keys())
prc_dic['2000-01-15'] = prc_dic['3000-01-15']
del prc_dic['3000-01-15']
print(sorted_keys)


import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
 df = yfinance.download(tic, start, end, ignore_tz=True)
 print(df)
 tic_base = tic.lower().split('.')[0]
 df.to_csv(f'{tic_base}_stk_prc.csv')

 import yfinance  # (1)

 tic = "QAN.AX"  # (2)
