""" zid_project1.py

"""
import json
import os

import toolkit_config
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join(cfg.PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """

    tickers_element = {}
    with open(pth, 'r') as file:
        for line in file:
            line = line.strip().lower()
            if line:
                element_ = line.split("=")
                if len(element_) == 2:
                    ticker = element_[1].strip().strip('"')
                    exchange = element_[0].strip().strip('"')
                    tickers_element[ticker] = exchange
    return tickers_element


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    # <COMPLETE THIS PART>
    dat_path = os.path.join(DATDIR, f"{tic}_prc.dat")
    with open(dat_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    # <COMPLETE THIS PART>
    file_dict = {}
    WIDTH = [value for value in COLWIDTHS.values()]
    start = 0
    for i in range(len(COLUMNS)):
        col = COLUMNS[i]
        width = WIDTH[i]
        value = line[start:(start + width)].strip()
        file_dict[col] = value
        start = start + width
    return file_dict



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    # <COMPLETE THIS PART>
    if tickers_lst is not None:
        if not tickers_lst:
            raise Exception

        for ticker in tickers_lst:
            if ticker not in tic_exchange_dic:
                raise Exception


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    # <COMPLETE THIS PART>
    if col_lst is not None:
        if not col_lst:
            raise Exception

        for col in col_lst:
            if col not in COLUMNS:
                raise Exception


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """
    # <COMPLETE THIS PART>
    data_dict = {}
    if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic.keys())
    else:
        verify_tickers(tic_exchange_dic, tickers_lst)

    for ticker in tickers_lst:
        tic_exchange = tic_exchange_dic[ticker]
        data = []
        for i in range(len(read_dat(ticker))):
            line_data = line_to_dict(read_dat(ticker)[i])
            if col_lst is None:
                col_lst = COLUMNS
            else:
                verify_cols(col_lst)
            line_data = {col: line_data[col] for col in col_lst}
            data.append(line_data)
        data_dict[ticker] = {'exchange': tic_exchange, 'data': data}
    return data_dict





# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    # <COMPLETE THIS PART>
    with open(pth, 'w') as json_file:
        json.dump(data_dict, json_file)

# ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------
    """<COMPLETE THIS PART>
Explain why to configure as in step 1:
----In the first step, I use os.path to set up a file and path of the file. 
In this way, which can let the code library more maintainable and more tidiness. 
This is very important because firstly it is more easy for us to maintain our code.
In my words, I think maintainability is that it is easy for us to change the path.
If we want to use other files, we only need to change the step1 instead of change 
all code. Secondly, it is more easy for us to add some new files to it. If we want 
to add new files, we just need to use 'os.path.join', which is very comfortable.
Thirdly, consistency. The file which we need to use is consistent with the bigger 
folder. In this way, it reduce the error risk of not consistent when we already 
write all the code. And we use the os can ensure that code can be work in any
different computers.

Evaluate both hypotheses:

Hypotheses1
----Assuming this hypothesis is true, when articles contain more negative words, it may 
reflect investors' negative evaluations of the company. This negative assessment 
could lead to a deterioration in investor sentiment, resulting in short-term declines
in stock prices. However, in the long run, if the company's fundamentals have not 
substantially changed, investors may reassess the situation and gradually push the 
stock price back to reasonable levels, thus no reversal occurs in the long term.

Hypotheses2
----Assuming this hypothesis is correct, the negative language in articles might reflect 
information beyond the company's fundamentals, such as industry trends, macroeconomic 
factors, or policy changes. These factors could influence stock prices in the short term. 
Since this information goes beyond the company's fundamentals, investors may need more 
time to reassess the situation and bring the stock price back to a reasonable level, 
potentially leading to no long-term reversal.

----
Considering the observed pattern of negative articles causing short-term stock price 
declines with no long-term reversal, I believe hypothesis 2 is more likely to be true. 
The sustained presence of negative sentiment and its impact on long-term stock prices 
suggests that the articles contain valuable information beyond just investor evaluations. 
If the articles were solely based on investor evaluations, we might expect short-term reversals 
as the market receives new information.
    

Evaluate the short-run predictability for the trading volume with reason(s)  
----
In the short term, trading volume may respond to both the expectations and content of articles. 
If negative articles lead to investor concerns and subsequently cause short-term declines in stock 
prices, trading volume may also increase.
    
    """


# ----------------------------------------------------------------------------
#   Test functions:
#   The purpose of these functions is to help you test the functions above as
#   you write them.
#   IMPORTANT:
#   - These functions are optional, you do not have to use them
#   - These functions do not count as part of your assessment (they will not
#     be marked)
#   - You can modify these functions as you wish, or delete them altogether.
# ----------------------------------------------------------------------------
def _test_get_tics():
    """ Test function for the `get_tics` function. Will print the tickers as
    returned by the `get_tics` function.
    """
    pth = TICPATH
    tics = get_tics(pth)
    print(tics)


def _test_read_dat():
    """ Test function for the `read_dat` function. Will read the lines of the
    first ticker in `TICPATH` and print the first line in the list.
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])


def _test_line_to_dict():
    """ Test function for the `read_dat` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Read the lines of the ".dat" file for the first ticker
    - Convert the first line of this file to a dictionary
    - Print this dictionary
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


def _test_create_data_dict():
    """ Test function for the `create_data_dict` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Call `create_data_dict` using
        - tickers_lst =  ['aapl', 'baba']
        - col_lst = ['Date', 'Close']
    - Print out the dictionary returned, but only the first 3 items of the data list for each ticker for brevity

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)


def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    _test_get_tics()
    _test_read_dat()
    _test_line_to_dict()
    _test_create_data_dict()
    _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass





