import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *


def amortize(principal, interest_rate, years, addl_principal=0, annual_payments=12, start_date=date.today()):
    """
    The below code, which may have been edited, was originally written by 
    Chris Moffitt of pbpython.com (used with permission):
    - Blog Post: http://pbpython.com/amortization-model-revised.html
    - Code: https://github.com/chris1610/pbpython/blob/63e810a42d30c8297b82f6da43e5e962b8a6f15a/notebooks/Amortization-Corrected-Final.ipynb
    - License: https://github.com/chris1610/pbpython/blob/63e810a42d30c8297b82f6da43e5e962b8a6f15a/LICENSE
    """

    pmt = -round(np.pmt(interest_rate/annual_payments, years*annual_payments, principal), 2)
    # initialize the variables to keep track of the periods and running balances
    p = 1
    beg_balance = principal
    end_balance = principal

    while end_balance > 0:

        # Recalculate the interest based on the current balance
        interest = round(((interest_rate/annual_payments) * beg_balance), 2)

        # Determine payment based on whether or not this period will pay off the loan
        pmt = min(pmt, beg_balance + interest)
        principal = pmt - interest

        # Ensure additional payment gets adjusted if the loan is being paid off
        addl_principal = min(addl_principal, beg_balance - principal)
        end_balance = beg_balance - (principal + addl_principal)

        yield OrderedDict([('Month',start_date),
                           ('Period', p),
                           ('BeginBalance', beg_balance),
                           ('Payment', pmt),
                           ('Principal', principal),
                           ('Interest', interest),
                           ('AddPayment', addl_principal),
                           ('EndBalance', end_balance)])

        # Increment the counter, balance and date
        p += 1
        start_date += relativedelta(months=1)
        beg_balance = end_balance


# --------------------------------------------------------------------------------------------------------    
import xlwings as xw
import datetime as dt

# --------------------------------------------------------------------------------------------------------
def main():
    # define sheet(s)
    sht = xw.Book.caller().sheets['Inputs']

    # clear sheet(s)
    sht.range('A17').expand().clear_contents()

    # read inputs
    principal       = sht.range('C5').value
    interest_rate   = sht.range('C6').value
    years           = sht.range('C7').value
    addl_principal  = sht.range('C8').value
    annual_payments = sht.range('C9').value
    start_date      = sht.range('C10').options(dates=dt.date).value

    # read DataFrames
    #df = sht.range('H5').expand().options(pd.DataFrame).value
    #df = df.convert_objects(convert_numeric=True)
    #xw.view(df)

    # perform calcs
    schedule = pd.DataFrame(amortize(principal, interest_rate, years, addl_principal, annual_payments, start_date))
    payoff_date = schedule['Month'].max()

    # write values to Excel
    sht.range('C15').value = payoff_date
    sht.range('A17').value = schedule


# this is for testing; run with: python mortgage.py
if __name__ == '__main__':
    # Expects the Excel file next to this source file, adjust accordingly.
    xw.Book('Mortgage.xlsm').set_mock_caller()
    main()