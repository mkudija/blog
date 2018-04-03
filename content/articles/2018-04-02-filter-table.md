Title: Table Filtering in HTML and JavaScript
date: 2018-04-03 06:00
updated: 2018-04-03 06:00
authors: Matthew Kudija
comments: true
slug: filter-table
tags: html, javascript, web, TableFilter

<!-- PELICAN_BEGIN_SUMMARY -->
![alt]({filename}/images/filter-table-1.gif)

GitHub pages makes it easy to share information: just send the URL instead of emailing a file attachment. When I wanted to share the contents of an Excel file this was a natural platform, but with over 1,000 rows of data I needed a way to filter the table on the webpage.

With my knowledge at the time limited to some basic HTML and very little JavaScript, this is an exercise in hacking together a solution. Keep reading to see how I implemented a solution using the [TableFilter](http://koalyptus.github.io/TableFilter/) JavaScript library. 

<!-- PELICAN_END_SUMMARY -->

# Requirements & Research
With our data to share in a local spreadsheet, the basic requirement is the ability to filter a table on a website on multiple columns just as you can in a spreadsheet:

![alt]({filename}/images/filter-table-2.gif)

Being comfortable in Python my first instinct is to [filter](https://github.com/mkudija/General-Examples/blob/master/Pandas/filter.md) a Pandas DataFrame. But we are hosting this on GitHub pages as a static website and unable to run the filtering server-side. Therefore, we'll use JavaScript to filter the table client-side in the browser.

I was able to find a [number](https://www.w3schools.com/howto/howto_js_filter_table.asp) of [examples](https://stackoverflow.com/questions/9127498/how-to-perform-a-real-time-search-and-filter-on-a-html-table) that provide basic filtering capability with JavaScript, but these are limited to filtering on one column. Eventually I came across the [TableFilter](http://koalyptus.github.io/TableFilter/) JavaScript library, which has great [documentation](http://koalyptus.github.io/TableFilter/docs/) and plenty of [examples](http://koalyptus.github.io/TableFilter/examples.html). 

# Using TableFilter
To get started, I cloned TableFilter into my repository:

```console
git clone https://github.com/koalyptus/TableFilter.git
```

We will edit `index.html`, the HTML file that holds our table and uses `tablefilter.js` to perform the filtering.

```console
├── assets
├── index.html
└── tablefilter
    └── tablefilter.js
```

The strategy I used to get a working product is simple and applicable to more general technical challenges:

1. Start with a working example that does approximately what you need or more
2. Remove or modify features to better align with your use case
3. Repeat step 2 until you have what you want

The key here is maintaining a working example throughout and taking a step back if you break something. Iterating a few times on the `index.html` I borrowed from one of the basic examples, I was left with this: 

```html
<!DOCTYPE HTML>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Table Filter Example</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">

  <body>

    <!-- Header -->
    <section id="header">
      <header>
        <h2>Filter Table Example</h2>
      </header>

      <!-- TABLE CODE START -->
      <table id="demo" border="1" class="dataframe">
        <thead>
          <tr style="text-align: right;">
            <th>First</th>
            <th>Last</th>
            <th>Birthday</th>
            <th>Age</th>
            <th>Color</th>
            <th>Height</th>
            <th>Weight</th>
            <th>IQ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>ZOE</td>
            <td>DAVIS</td>
            <td>2012-03-12</td>
            <td>6</td>
            <td>Yellow</td>
            <td>67</td>
            <td>108</td>
            <td>81</td>
          </tr>
          
          ...

        </tbody>
      </table>
      <!-- TABLE CODE END -->

    </section>
  </body>
</head>

<script src="tablefilter/tablefilter.js"></script>

<script data-config="">
 var filtersConfig = {
  base_path: 'tablefilter/',
  auto_filter: {
                    delay: 110 //milliseconds
              },
              filters_row_index: 1,
              state: true,
              alternate_rows: true,
              rows_counter: true,
              btn_reset: true,
              status_bar: true,
              msg_filter: 'Filtering...'
            };
            var tf = new TableFilter('demo', filtersConfig);
            tf.init();
          </script>
```

*You can view the original [code](https://github.com/mkudija/General-Examples/tree/master/Web/HTML_Table_Filter) or a [live example](http://matthewkudija.com/General-Examples/Web/HTML_Table_Filter/index.html) of the final product.*

Customize this by including the HTML defining the table between `<!-- TABLE CODE START -->` and `<!-- TABLE CODE END -->` (easy to automate with Python if you need to update the data often). Just below the table definition, we call the `tablefilter.js` script and define the configuration items. 

This leaves us with an easy to filter table:

![alt]({filename}/images/filter-table-1.gif)

# Closing Thoughts
Is this the best way to share data? Certainly not. But it was a quick solution to a problem I had in a situation (work) where speed and ease are valued at a premium. Furthermore this solution utilizes existing GitHub pages infrastructure and a great [open source](https://github.com/koalyptus/TableFilter/blob/master/LICENSE) library. 

I hope this example either provides you with a quick solution to a problem I previously had or demonstrates how you may be able to hack together a solution by iterating on a similar working example you can find online.

---

- *All names in this dataset are fake. Any resemblance to real persons, living or dead, is purely coincidental...I made up some data since the data motivating this example is proprietary.*
- *You can view the original [code](https://github.com/mkudija/General-Examples/tree/master/Web/HTML_Table_Filter) or a [live example](http://matthewkudija.com/General-Examples/Web/HTML_Table_Filter/index.html) of the final product.*
- *While writing this up I discovered [Brython](https://github.com/brython-dev/brython), an implementation of Python 3 in the browser. This is worth checking out in the future.*
