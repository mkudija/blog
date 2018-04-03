Title: Filter Table
date: 2018-04-02 06:00
updated: 2018-04-02 06:00
comments: true
slug: filter-table
tags: html, javascript, web
status: draft

<!-- PELICAN_BEGIN_SUMMARY -->
![alt]({filename}/images/filter-table-1.gif)

Recently I wanted to make a table of data available on GitHub Pages for quick reference. Since there were a lot of rows (over 1,000) I really needed a way to filter the table down. You could `CTRL + F` your way through the table, but this would be annoying and only all you to search on one column at a time.



<!-- PELICAN_END_SUMMARY -->


# Requirements
The data to share is in a spreadsheet on my computer, and the motivation for this in the first place was to make it accessible to others without needing to email the spreadsheet. The basic requirements, therefore, is the ability to filter on multiple columns as you can in a spreadsheet:

![alt]({filename}/images/filter-table-2.gif)


# Initial Looking
Some initial poking around showed that there some options that 

# The Process
After some searching, I came across [TableFilter](http://koalyptus.github.io/TableFilter/) library


# Example
Example code [here](https://github.com/mkudija/General-Examples/tree/master/Web/HTML_Table_Filter)


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



[Live example](http://matthewkudija.com/General-Examples/Web/HTML_Table_Filter/index.html)


# Closing Thoughts

- is this the best way to share this information? no, but it works
- show this example to demonstrate how you don't need to have an intimate understanding to make something work

> **Note:** All names in this dataset are fake. Any resemblance to real persons, living or dead, is purely coincidental.