Title: xlwings as a Wrapper for a Python Function
date: 2018-03-21 06:00
comments: true
slug: xlwings-mortgage
tags: python, pandas, xlwings, excel
status: draft

![alt]({filename}/images/xlwings-mortgage.png)

<!-- PELICAN_BEGIN_SUMMARY -->

The Python [xlwings](https://www.xlwings.org/) library provides easy interaction between Python and a Microsoft Excel workbook. In this example, I demonstrate using xlwings and Excel as a wrapper around a Python function.

<!-- PELICAN_END_SUMMARY -->

Python and Excel have complementary strengths and it can be useful to use them together. Excel is great for lightweight data exploration where you need some interactivity, and as the default tool for data analysis in the corporate world an average user is probably much less intimidated by Excel than more advanced tools. Python provides heavy-duty analytics, access to many third-party libraries, and allows you to make your analysis more reproducable since it can be version-controlled and quickly re-run with new data. Using xlwings to link the two can bring the best of both worlds. Let's get started.



# Wrapping a Python Function
This example uses xlwings as a bridge between a Python function and an Excel front-end. The easiest way to get started with xlwings is to download and modify a working example. There are great examples on the [xlwings page](https://www.xlwings.org/examples), or you can download all the files used to create this example [here](). 

## Python Function
The Python function we will use as an example is a financial model built with pandas written by Chris Moffitt. We will take this function as a given, but please see Chris' [original post](http://pbpython.com/amortization-model-revised.html) for the details. This model builds a simple loan amortization table, such as you would need to evaluate a mortgage. Given the required inputs of loan principal, interest rate, term, etc. this Python function returns a pandas DataFrame giving the amortization table. 

```python
def amortize(principal, interest_rate, years, addl_principal=0, annual_payments=12, start_date=date.today()):
    """
    The below code, which may have been edited, was originally written by Chris Moffitt of pbpython.com:
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
```

Remember that while we are using this as an example, anything you can do in Python is fair game for extending the capabilities of Excel.


## Set up the workbook
First, let's set up the Excel workbook. Our user will set values for the required inputs, press the "Calculate" button, and see outputs written by xlwings. The chart is a native Excel chart constructed off the table in the outputs, but xlwings [can write image files](http://docs.xlwings.org/en/stable/matplotlib.html) to Excel so you could generate charts in matplotlib or another Python plotting library as well. This is a standard `.xlsm` macro-enabled Excel workbook, so you can apply formatting and add charts as you like.

![alt]({filename}/images/xlwings-mortgage-2.png)



## Set up Python with xlwings
Our Python script **`mortgage.py`** uses xlwigns to interface with Excel. First we include the `amortize()` function discussed previously. All the Excel interaction is in the `main()` function. We define the sheets to pull from.

  - if __main__ for testing (print)

**`mortgage.py`**:

```python
import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *


def amortize(principal, interest_rate, years, addl_principal=0, annual_payments=12, start_date=date.today()):
    """
    Function not copied...see above
    """


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
```

## Set up the macro

Finally, we can call `mortgage.py` using a simple macro which is assigned to the button.  

```vba
Sub Button_click()
    RunPython ("import mortgage; mortgage.main()")
End Sub
```


# How you use this
As you can see, xlwings is a powerful way to bring together the best of Excel and Python. 
- complex spreadsheed that you want to automate parts of: use python to add a bit of automation instead of VBA (Odin model)
- Python code you want to share with others: use Excel as your front end (BD Tool)
- 

