Title: Matplotlib: Multiple Y-Axis Scales
date: 2019-02-13 06:00
updated: 2019-02-13 06:00
authors: Matthew Kudija
comments: true
slug: matplotlib-twin-axes
tags: python, matplotlib

<!-- PELICAN_BEGIN_SUMMARY -->
<!-- ![alt]({filename}/downloads/code/matplotlib-twin-axes/matplotlib-twin-axes.png) -->

<p style="text-align:center;"><img src="{filename}/downloads/code/matplotlib-twin-axes/matplotlib-twin-axes.png" width="75%" height="75%"></p>

Matplotlib's flexibility allows you to show a second scale on the y-axis. This example allows us to show monthly data with the corresponding annual total at those monthly rates. 

<!-- PELICAN_END_SUMMARY -->

The Matplotlib [`Axes.twinx`](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.twinx.html) method creates a new y-axis that shares the same x-axis. First we create an axis for the monthly and yearly scales:

```python
mm = ax.twinx()
yy = ax.twinx()
```

Let's label the monthly and yearly scales:
```python
mm.set_ylabel('Monthly Hours')
yy.set_ylabel('Yearly Hours')
```

Finally, we set the position of the yearly scale to the far right, and scale it based on the axis limits to be an annual total:

```python
yy.spines["right"].set_position(("axes", 1.2))
yy.set_ylim(mm.get_ylim()[0]*12, mm.get_ylim()[1]*12)
```

The full code to generate this plot is given in [`matplotlib-twin-axes.py`](https://github.com/mkudija/blog/tree/master/content/downloads/code/matplotlib-twin-axes/matplotlib-twin-axes.py):

<details>
	<summary>Click to expand...</summary>

```python
import pandas as pd


# --------------------------------------------------------------------------------------------------------
def plot(df, title):

    import matplotlib.pyplot as plt

    plt.style.use('mag')
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    mm = ax.twinx()
    yy = ax.twinx()
    for col in df.columns:
        mm.plot(df.index,df[[col]],label=col)
    mm.set_ylabel('Monthly Hours')
    yy.set_ylabel('Yearly Hours')
    yy.spines["right"].set_position(("axes", 1.2))
    yy.set_ylim(mm.get_ylim()[0]*12, mm.get_ylim()[1]*12)
    
    mm.tick_params(axis='y',labelsize=16) # set monthly labelsize (not global)

    # format
    ax.xaxis.grid(False)
    mm.yaxis.grid(False)
    yy.yaxis.grid(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.title(title, fontsize=16, x=.65, y=1.05)

    # format x-axis ticks as dates
    import matplotlib.dates as mdates
    years = mdates.YearLocator()    # every year
    months = mdates.MonthLocator()  # every month
    yearsFmt = mdates.DateFormatter('\n%Y')
    moFmt = mdates.DateFormatter('%m') # (%b for Jan, Feb Mar; %m for 01 02 03)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_minor_locator(months)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_formatter(moFmt)
    for label in ax.xaxis.get_minorticklabels()[::2]: # show every other minor label
        label.set_visible(False)
    
    # turn off x-axis
    x_axis = ax.axes.get_xaxis()
    x_label = x_axis.get_label()
    x_label.set_visible(False)

    # turn-off left y-axis
    ax.yaxis.set_visible(False)

    # adjust fontsize
    plt.tick_params(axis='both', which='major', labelsize=16)

    handles, labels = mm.get_legend_handles_labels()
    mm.legend(fontsize=14, loc=6)

    plt.savefig('matplotlib-twin-axes.png', bbox_inches='tight', dpi=150)


def main():

    df = pd.read_excel('data.xlsx').set_index('Date')
    plot(df, title='Multi Y-Axis Scales')


if __name__ == '__main__':
    main()
```

</details>

<p style="text-align:center;"><img src="{filename}/downloads/code/matplotlib-twin-axes/matplotlib-twin-axes.png" width="75%" height="75%"></p>



---

- *You can view the original [code and data](https://github.com/mkudija/blog/tree/master/content/downloads/code/matplotlib-twin-axes).*
- *Example:* [Plots with different scales](https://matplotlib.org/gallery/subplots_axes_and_figures/two_scales.html#sphx-glr-gallery-subplots-axes-and-figures-two-scales-py)
- *Example:* [multiple axis in matplotlib with different scales](https://stackoverflow.com/questions/9103166/multiple-axis-in-matplotlib-with-different-scales)




*Versions:*
```
Python      3.6.3
pandas      0.23.4
matplotlib  3.0.0
```