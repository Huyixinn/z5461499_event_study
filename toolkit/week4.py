def qan_tic():            # (1)

    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()                 # (7)



# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)


i = 1
test = i == 1
print(test)

f = 0.2 + 0.2 + 0.2
print(f)


l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for i in l:
    print(i)


import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
 df = yfinance.download(tic, start, end, ignore_tz=True)
 print(df)
 tic_base = tic.lower().split('.')[0]
 df.to_csv(f'{tic_base}_stk_prc.csv')

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)


def qan_tic(): # (1)
 tic = "QAN.AX" # (2)

# Call the function
res = qan_tic() # (5b)
print(res)



def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
# Call the function
qan_tic() # (5)




def qan_tic(): # (1)

 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7




def mk_csv_name(tic): # (1)
 tic = tic.lower() # (2)
 tic_base = tic.split('.')[0] # (3)
 return f'{tic_base}_stk_prc.csv' # (4)
name = mk_csv_name('QAN.AX') # (5)
print(name) # (6)




# Start with a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# Create a set comprehension with the keys from `dic`
keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')


def add(a,b):
    ''' Returns the sum of two numbers '''
    return a + b
