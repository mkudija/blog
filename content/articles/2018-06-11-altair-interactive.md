title: Altair: Interactive Plots in Jupyter and on a Webpage
date: 2018-06-11 06:00
authors: Matthew Kudija
comments: true
slug: altair-interactive
tags: python, altair, vega
include: vega
status: draft

<!-- PELICAN_BEGIN_SUMMARY -->

![alt]({filename}/images/altair-interactive.png)

Adding interactivity to data visualizations can be extremely helpful, espcially with large, multi-dimensional datasets. Sharing them online extends the benefits to others. In this article I will show some examples of using the Altair library to create and share some simple interactive visualizations. The examples below are largely derived from examples in the excellent Altiar gallery. I claim no original work on these but enjoyed working with them to learn the mechanics of interactive visualization in Altair. 

<!-- PELICAN_END_SUMMARY -->

# Intro to Altair
[Altair](https://altair-viz.github.io) is a visualization library for Python notable for the fact that is takes a *declarative* approach and is based on [Vega](https://vega.github.io/vega/) and [Vega-Lite](https://vega.github.io/vega-lite/).

Every Altair chart is made up of **Data**, **Marks**, and **Encodings**, which can be modified with **Binning and Aggregation**. With a dataset of columns of x, y, and color, we can define a barebones Altair chart like this:

```python
alt.Chart(data).mark_point().encode(
    x='x:Q',
    y='mean(y)',
    color='color:O'
)
```

A quick summary of the properties available is given in the table below, with links to the Altair documentation of the corresponding section:

| [\| Marks \|](https://altair-viz.github.io/user_guide/marks.html) | [\| Encodings \|](https://altair-viz.github.io/user_guide/encoding.html) | [\| Data Types \|](https://altair-viz.github.io/user_guide/encoding.html#data-types) | [\| Binning & Aggregation \|](https://altair-viz.github.io/user_guide/encoding.html#binning-and-aggregation) | 
| :---: | :---: | :---: | :---: | 
| `mark_area`  | `x`: x-axis value | `:Q` Quantitative | `average` | 
| `mark_bar` | `y`: y-axis value| `:N` Nominal| `average`|
| `mark_circle` | `color`| `:O` Ordinal| `sum`|
| `mark_geoshape` | `opacity`| `:T` Temporal| `count`|
| `mark_line` | `shape`| | `distinct`|
| `mark_point` | `size`| | `max`|
| `mark_rect` | `row`| | `q1`/`q3`|
| `mark_rule` | `column`| | `ci0`/`ci1`|
| `mark_square` | `tooltip`| | etc...|
| `mark_text` | etc...| | |
| `mark_tick` | | | |
| `mark_trail` | | | |






# Building Interactive Altair Charts

## Cars Example

Start with a basic chart:

```python
import altair as alt
from vega_datasets import data

cars = data.cars.url

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)
```

<div id="vis00"></div>
<script type="text/javascript">
var spec00 = {"config":{"view":{"width":400,"height":300}},"data":{"url":"https://vega.github.io/vega-datasets/data/cars.json","format":{"type":"json"}},"mark":"point","encoding":{"color":{"type":"nominal","field":"Origin"},"x":{"type":"quantitative","field":"Horsepower"},"y":{"type":"quantitative","field":"Miles_per_Gallon"}},"$schema":"https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt00 = {"mode": "vega-lite"};

function showError(el00, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el00 = document.getElementById('vis00');
vegaEmbed("#vis00", spec00, embed_opt00)
.catch(error => showError(el00, error));
</script>



Then we add in some interactivity, including tooltips and a selectable legend:
```python
import altair as alt
from vega_datasets import data

cars = data.cars.url

# define selection
click = alt.selection_multi(encodings=['color'])

# scatter plots of points
scatter = alt.Chart(cars).mark_circle().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    size=alt.Size('Cylinders:O',
        scale=alt.Scale(range=(20,100))
    ),
    color=alt.Color('Origin:N', legend=None),
    tooltip=['Name:N','Horsepower:Q','Miles_per_Gallon:Q',
             'Cylinders:O','Origin:N'],
).transform_filter(
    click
).interactive()

# legend
legend = alt.Chart(cars).mark_rect().encode(
    y=alt.Y('Origin:N', axis=alt.Axis(title='Select Origin')),
    color=alt.condition(click, 'Origin:N', 
                        alt.value('lightgray'), legend=None),
    size=alt.value(250)
).properties(
    selection=click
)

chart = (scatter | legend)
chart.save('cars-clickable-legend.html')
```

<div id="vis0"></div>
<script type="text/javascript">
var spec0 = {"config": {"view": {"width": 400, "height": 300}}, "hconcat": [{"data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"}, "mark": "circle", "encoding": {"color": {"type": "nominal", "field": "Origin", "legend": null}, "size": {"type": "ordinal", "field": "Cylinders", "scale": {"range": [20, 100]}}, "tooltip": [{"type": "nominal", "field": "Name"}, {"type": "quantitative", "field": "Horsepower"}, {"type": "quantitative", "field": "Miles_per_Gallon"}, {"type": "ordinal", "field": "Cylinders"}, {"type": "nominal", "field": "Origin"}], "x": {"type": "quantitative", "field": "Horsepower"}, "y": {"type": "quantitative", "field": "Miles_per_Gallon"}}, "selection": {"selector005": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "transform": [{"filter": {"selection": "selector004"}}]}, {"data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"}, "mark": "rect", "encoding": {"color": {"condition": {"type": "nominal", "field": "Origin", "legend": null, "selection": "selector004"}, "value": "lightgray"}, "size": {"value": 250}, "y": {"type": "nominal", "axis": {"title": "Select Origin"}, "field": "Origin"}}, "selection": {"selector004": {"type": "multi", "encodings": ["color"]}}}], "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt0 = {"mode": "vega-lite"};

function showError(el0, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el0 = document.getElementById('vis0');
vegaEmbed("#vis0", spec0, embed_opt0)
.catch(error => showError(el0, error));
</script>


## Stocks Example

```python
# multi series line chart: https://altair-viz.github.io/gallery/multi_series_line.html
# multi-line tooltip: https://altair-viz.github.io/gallery/multiline_tooltip.html

import altair as alt
from vega_datasets import data

stocks = data.stocks()

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['date'], empty='none')

# The basic line
line = alt.Chart().mark_line(interpolate='basis').encode(
    alt.X('date:T', axis=alt.Axis(title='')),
    alt.Y('price:Q', axis=alt.Axis(title='',format='$f')),
    color='symbol:N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart().mark_point().encode(
    x='date:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'price:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart().mark_rule(color='gray').encode(
    x='date:T',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
stockChart = alt.layer(line, selectors, points, rules, text,
          data=stocks, width=600, height=300,title='Stock History')
stockChart.save('stocks.html')
```

<div id="vis1"></div>
<script type="text/javascript">
var spec = {"config": {"view": {"width": 400, "height": 300}}, "layer": [{"mark": {"type": "line", "interpolate": "basis"}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}, {"mark": "point", "encoding": {"opacity": {"value": 0}, "x": {"type": "temporal", "field": "date"}}, "selection": {"selector001": {"type": "single", "nearest": true, "on": "mouseover", "fields": ["date"], "empty": "none"}}}, {"mark": "point", "encoding": {"color": {"type": "nominal", "field": "symbol"}, "opacity": {"condition": {"value": 1, "selection": "selector001"}, "value": 0}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}, {"mark": {"type": "rule", "color": "gray"}, "encoding": {"x": {"type": "temporal", "field": "date"}}, "transform": [{"filter": {"selection": "selector001"}}]}, {"mark": {"type": "text", "align": "left", "dx": 5, "dy": -5}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "text": {"condition": {"type": "quantitative", "field": "price", "selection": "selector001"}, "value": " "}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}], "data": {"values": [{"symbol": "MSFT", "date": "2000-01-01", "price": 39.81}, {"symbol": "MSFT", "date": "2000-02-01", "price": 36.35}, {"symbol": "MSFT", "date": "2000-03-01", "price": 43.22}, {"symbol": "MSFT", "date": "2000-04-01", "price": 28.37}, {"symbol": "MSFT", "date": "2000-05-01", "price": 25.45}, {"symbol": "MSFT", "date": "2000-06-01", "price": 32.54}, {"symbol": "MSFT", "date": "2000-07-01", "price": 28.4}, {"symbol": "MSFT", "date": "2000-08-01", "price": 28.4}, {"symbol": "MSFT", "date": "2000-09-01", "price": 24.53}, {"symbol": "MSFT", "date": "2000-10-01", "price": 28.02}, {"symbol": "MSFT", "date": "2000-11-01", "price": 23.34}, {"symbol": "MSFT", "date": "2000-12-01", "price": 17.65}, {"symbol": "MSFT", "date": "2001-01-01", "price": 24.84}, {"symbol": "MSFT", "date": "2001-02-01", "price": 24.0}, {"symbol": "MSFT", "date": "2001-03-01", "price": 22.25}, {"symbol": "MSFT", "date": "2001-04-01", "price": 27.56}, {"symbol": "MSFT", "date": "2001-05-01", "price": 28.14}, {"symbol": "MSFT", "date": "2001-06-01", "price": 29.7}, {"symbol": "MSFT", "date": "2001-07-01", "price": 26.93}, {"symbol": "MSFT", "date": "2001-08-01", "price": 23.21}, {"symbol": "MSFT", "date": "2001-09-01", "price": 20.82}, {"symbol": "MSFT", "date": "2001-10-01", "price": 23.65}, {"symbol": "MSFT", "date": "2001-11-01", "price": 26.12}, {"symbol": "MSFT", "date": "2001-12-01", "price": 26.95}, {"symbol": "MSFT", "date": "2002-01-01", "price": 25.92}, {"symbol": "MSFT", "date": "2002-02-01", "price": 23.73}, {"symbol": "MSFT", "date": "2002-03-01", "price": 24.53}, {"symbol": "MSFT", "date": "2002-04-01", "price": 21.26}, {"symbol": "MSFT", "date": "2002-05-01", "price": 20.71}, {"symbol": "MSFT", "date": "2002-06-01", "price": 22.25}, {"symbol": "MSFT", "date": "2002-07-01", "price": 19.52}, {"symbol": "MSFT", "date": "2002-08-01", "price": 19.97}, {"symbol": "MSFT", "date": "2002-09-01", "price": 17.79}, {"symbol": "MSFT", "date": "2002-10-01", "price": 21.75}, {"symbol": "MSFT", "date": "2002-11-01", "price": 23.46}, {"symbol": "MSFT", "date": "2002-12-01", "price": 21.03}, {"symbol": "MSFT", "date": "2003-01-01", "price": 19.31}, {"symbol": "MSFT", "date": "2003-02-01", "price": 19.34}, {"symbol": "MSFT", "date": "2003-03-01", "price": 19.76}, {"symbol": "MSFT", "date": "2003-04-01", "price": 20.87}, {"symbol": "MSFT", "date": "2003-05-01", "price": 20.09}, {"symbol": "MSFT", "date": "2003-06-01", "price": 20.93}, {"symbol": "MSFT", "date": "2003-07-01", "price": 21.56}, {"symbol": "MSFT", "date": "2003-08-01", "price": 21.65}, {"symbol": "MSFT", "date": "2003-09-01", "price": 22.69}, {"symbol": "MSFT", "date": "2003-10-01", "price": 21.45}, {"symbol": "MSFT", "date": "2003-11-01", "price": 21.1}, {"symbol": "MSFT", "date": "2003-12-01", "price": 22.46}, {"symbol": "MSFT", "date": "2004-01-01", "price": 22.69}, {"symbol": "MSFT", "date": "2004-02-01", "price": 21.77}, {"symbol": "MSFT", "date": "2004-03-01", "price": 20.46}, {"symbol": "MSFT", "date": "2004-04-01", "price": 21.45}, {"symbol": "MSFT", "date": "2004-05-01", "price": 21.53}, {"symbol": "MSFT", "date": "2004-06-01", "price": 23.44}, {"symbol": "MSFT", "date": "2004-07-01", "price": 23.38}, {"symbol": "MSFT", "date": "2004-08-01", "price": 22.47}, {"symbol": "MSFT", "date": "2004-09-01", "price": 22.76}, {"symbol": "MSFT", "date": "2004-10-01", "price": 23.02}, {"symbol": "MSFT", "date": "2004-11-01", "price": 24.6}, {"symbol": "MSFT", "date": "2004-12-01", "price": 24.52}, {"symbol": "MSFT", "date": "2005-01-01", "price": 24.11}, {"symbol": "MSFT", "date": "2005-02-01", "price": 23.15}, {"symbol": "MSFT", "date": "2005-03-01", "price": 22.24}, {"symbol": "MSFT", "date": "2005-04-01", "price": 23.28}, {"symbol": "MSFT", "date": "2005-05-01", "price": 23.82}, {"symbol": "MSFT", "date": "2005-06-01", "price": 22.93}, {"symbol": "MSFT", "date": "2005-07-01", "price": 23.64}, {"symbol": "MSFT", "date": "2005-08-01", "price": 25.35}, {"symbol": "MSFT", "date": "2005-09-01", "price": 23.83}, {"symbol": "MSFT", "date": "2005-10-01", "price": 23.8}, {"symbol": "MSFT", "date": "2005-11-01", "price": 25.71}, {"symbol": "MSFT", "date": "2005-12-01", "price": 24.29}, {"symbol": "MSFT", "date": "2006-01-01", "price": 26.14}, {"symbol": "MSFT", "date": "2006-02-01", "price": 25.04}, {"symbol": "MSFT", "date": "2006-03-01", "price": 25.36}, {"symbol": "MSFT", "date": "2006-04-01", "price": 22.5}, {"symbol": "MSFT", "date": "2006-05-01", "price": 21.19}, {"symbol": "MSFT", "date": "2006-06-01", "price": 21.8}, {"symbol": "MSFT", "date": "2006-07-01", "price": 22.51}, {"symbol": "MSFT", "date": "2006-08-01", "price": 24.13}, {"symbol": "MSFT", "date": "2006-09-01", "price": 25.68}, {"symbol": "MSFT", "date": "2006-10-01", "price": 26.96}, {"symbol": "MSFT", "date": "2006-11-01", "price": 27.66}, {"symbol": "MSFT", "date": "2006-12-01", "price": 28.13}, {"symbol": "MSFT", "date": "2007-01-01", "price": 29.07}, {"symbol": "MSFT", "date": "2007-02-01", "price": 26.63}, {"symbol": "MSFT", "date": "2007-03-01", "price": 26.35}, {"symbol": "MSFT", "date": "2007-04-01", "price": 28.3}, {"symbol": "MSFT", "date": "2007-05-01", "price": 29.11}, {"symbol": "MSFT", "date": "2007-06-01", "price": 27.95}, {"symbol": "MSFT", "date": "2007-07-01", "price": 27.5}, {"symbol": "MSFT", "date": "2007-08-01", "price": 27.34}, {"symbol": "MSFT", "date": "2007-09-01", "price": 28.04}, {"symbol": "MSFT", "date": "2007-10-01", "price": 35.03}, {"symbol": "MSFT", "date": "2007-11-01", "price": 32.09}, {"symbol": "MSFT", "date": "2007-12-01", "price": 34.0}, {"symbol": "MSFT", "date": "2008-01-01", "price": 31.13}, {"symbol": "MSFT", "date": "2008-02-01", "price": 26.07}, {"symbol": "MSFT", "date": "2008-03-01", "price": 27.21}, {"symbol": "MSFT", "date": "2008-04-01", "price": 27.34}, {"symbol": "MSFT", "date": "2008-05-01", "price": 27.25}, {"symbol": "MSFT", "date": "2008-06-01", "price": 26.47}, {"symbol": "MSFT", "date": "2008-07-01", "price": 24.75}, {"symbol": "MSFT", "date": "2008-08-01", "price": 26.36}, {"symbol": "MSFT", "date": "2008-09-01", "price": 25.78}, {"symbol": "MSFT", "date": "2008-10-01", "price": 21.57}, {"symbol": "MSFT", "date": "2008-11-01", "price": 19.66}, {"symbol": "MSFT", "date": "2008-12-01", "price": 18.91}, {"symbol": "MSFT", "date": "2009-01-01", "price": 16.63}, {"symbol": "MSFT", "date": "2009-02-01", "price": 15.81}, {"symbol": "MSFT", "date": "2009-03-01", "price": 17.99}, {"symbol": "MSFT", "date": "2009-04-01", "price": 19.84}, {"symbol": "MSFT", "date": "2009-05-01", "price": 20.59}, {"symbol": "MSFT", "date": "2009-06-01", "price": 23.42}, {"symbol": "MSFT", "date": "2009-07-01", "price": 23.18}, {"symbol": "MSFT", "date": "2009-08-01", "price": 24.43}, {"symbol": "MSFT", "date": "2009-09-01", "price": 25.49}, {"symbol": "MSFT", "date": "2009-10-01", "price": 27.48}, {"symbol": "MSFT", "date": "2009-11-01", "price": 29.27}, {"symbol": "MSFT", "date": "2009-12-01", "price": 30.34}, {"symbol": "MSFT", "date": "2010-01-01", "price": 28.05}, {"symbol": "MSFT", "date": "2010-02-01", "price": 28.67}, {"symbol": "MSFT", "date": "2010-03-01", "price": 28.8}, {"symbol": "AMZN", "date": "2000-01-01", "price": 64.56}, {"symbol": "AMZN", "date": "2000-02-01", "price": 68.87}, {"symbol": "AMZN", "date": "2000-03-01", "price": 67.0}, {"symbol": "AMZN", "date": "2000-04-01", "price": 55.19}, {"symbol": "AMZN", "date": "2000-05-01", "price": 48.31}, {"symbol": "AMZN", "date": "2000-06-01", "price": 36.31}, {"symbol": "AMZN", "date": "2000-07-01", "price": 30.12}, {"symbol": "AMZN", "date": "2000-08-01", "price": 41.5}, {"symbol": "AMZN", "date": "2000-09-01", "price": 38.44}, {"symbol": "AMZN", "date": "2000-10-01", "price": 36.62}, {"symbol": "AMZN", "date": "2000-11-01", "price": 24.69}, {"symbol": "AMZN", "date": "2000-12-01", "price": 15.56}, {"symbol": "AMZN", "date": "2001-01-01", "price": 17.31}, {"symbol": "AMZN", "date": "2001-02-01", "price": 10.19}, {"symbol": "AMZN", "date": "2001-03-01", "price": 10.23}, {"symbol": "AMZN", "date": "2001-04-01", "price": 15.78}, {"symbol": "AMZN", "date": "2001-05-01", "price": 16.69}, {"symbol": "AMZN", "date": "2001-06-01", "price": 14.15}, {"symbol": "AMZN", "date": "2001-07-01", "price": 12.49}, {"symbol": "AMZN", "date": "2001-08-01", "price": 8.94}, {"symbol": "AMZN", "date": "2001-09-01", "price": 5.97}, {"symbol": "AMZN", "date": "2001-10-01", "price": 6.98}, {"symbol": "AMZN", "date": "2001-11-01", "price": 11.32}, {"symbol": "AMZN", "date": "2001-12-01", "price": 10.82}, {"symbol": "AMZN", "date": "2002-01-01", "price": 14.19}, {"symbol": "AMZN", "date": "2002-02-01", "price": 14.1}, {"symbol": "AMZN", "date": "2002-03-01", "price": 14.3}, {"symbol": "AMZN", "date": "2002-04-01", "price": 16.69}, {"symbol": "AMZN", "date": "2002-05-01", "price": 18.23}, {"symbol": "AMZN", "date": "2002-06-01", "price": 16.25}, {"symbol": "AMZN", "date": "2002-07-01", "price": 14.45}, {"symbol": "AMZN", "date": "2002-08-01", "price": 14.94}, {"symbol": "AMZN", "date": "2002-09-01", "price": 15.93}, {"symbol": "AMZN", "date": "2002-10-01", "price": 19.36}, {"symbol": "AMZN", "date": "2002-11-01", "price": 23.35}, {"symbol": "AMZN", "date": "2002-12-01", "price": 18.89}, {"symbol": "AMZN", "date": "2003-01-01", "price": 21.85}, {"symbol": "AMZN", "date": "2003-02-01", "price": 22.01}, {"symbol": "AMZN", "date": "2003-03-01", "price": 26.03}, {"symbol": "AMZN", "date": "2003-04-01", "price": 28.69}, {"symbol": "AMZN", "date": "2003-05-01", "price": 35.89}, {"symbol": "AMZN", "date": "2003-06-01", "price": 36.32}, {"symbol": "AMZN", "date": "2003-07-01", "price": 41.64}, {"symbol": "AMZN", "date": "2003-08-01", "price": 46.32}, {"symbol": "AMZN", "date": "2003-09-01", "price": 48.43}, {"symbol": "AMZN", "date": "2003-10-01", "price": 54.43}, {"symbol": "AMZN", "date": "2003-11-01", "price": 53.97}, {"symbol": "AMZN", "date": "2003-12-01", "price": 52.62}, {"symbol": "AMZN", "date": "2004-01-01", "price": 50.4}, {"symbol": "AMZN", "date": "2004-02-01", "price": 43.01}, {"symbol": "AMZN", "date": "2004-03-01", "price": 43.28}, {"symbol": "AMZN", "date": "2004-04-01", "price": 43.6}, {"symbol": "AMZN", "date": "2004-05-01", "price": 48.5}, {"symbol": "AMZN", "date": "2004-06-01", "price": 54.4}, {"symbol": "AMZN", "date": "2004-07-01", "price": 38.92}, {"symbol": "AMZN", "date": "2004-08-01", "price": 38.14}, {"symbol": "AMZN", "date": "2004-09-01", "price": 40.86}, {"symbol": "AMZN", "date": "2004-10-01", "price": 34.13}, {"symbol": "AMZN", "date": "2004-11-01", "price": 39.68}, {"symbol": "AMZN", "date": "2004-12-01", "price": 44.29}, {"symbol": "AMZN", "date": "2005-01-01", "price": 43.22}, {"symbol": "AMZN", "date": "2005-02-01", "price": 35.18}, {"symbol": "AMZN", "date": "2005-03-01", "price": 34.27}, {"symbol": "AMZN", "date": "2005-04-01", "price": 32.36}, {"symbol": "AMZN", "date": "2005-05-01", "price": 35.51}, {"symbol": "AMZN", "date": "2005-06-01", "price": 33.09}, {"symbol": "AMZN", "date": "2005-07-01", "price": 45.15}, {"symbol": "AMZN", "date": "2005-08-01", "price": 42.7}, {"symbol": "AMZN", "date": "2005-09-01", "price": 45.3}, {"symbol": "AMZN", "date": "2005-10-01", "price": 39.86}, {"symbol": "AMZN", "date": "2005-11-01", "price": 48.46}, {"symbol": "AMZN", "date": "2005-12-01", "price": 47.15}, {"symbol": "AMZN", "date": "2006-01-01", "price": 44.82}, {"symbol": "AMZN", "date": "2006-02-01", "price": 37.44}, {"symbol": "AMZN", "date": "2006-03-01", "price": 36.53}, {"symbol": "AMZN", "date": "2006-04-01", "price": 35.21}, {"symbol": "AMZN", "date": "2006-05-01", "price": 34.61}, {"symbol": "AMZN", "date": "2006-06-01", "price": 38.68}, {"symbol": "AMZN", "date": "2006-07-01", "price": 26.89}, {"symbol": "AMZN", "date": "2006-08-01", "price": 30.83}, {"symbol": "AMZN", "date": "2006-09-01", "price": 32.12}, {"symbol": "AMZN", "date": "2006-10-01", "price": 38.09}, {"symbol": "AMZN", "date": "2006-11-01", "price": 40.34}, {"symbol": "AMZN", "date": "2006-12-01", "price": 39.46}, {"symbol": "AMZN", "date": "2007-01-01", "price": 37.67}, {"symbol": "AMZN", "date": "2007-02-01", "price": 39.14}, {"symbol": "AMZN", "date": "2007-03-01", "price": 39.79}, {"symbol": "AMZN", "date": "2007-04-01", "price": 61.33}, {"symbol": "AMZN", "date": "2007-05-01", "price": 69.14}, {"symbol": "AMZN", "date": "2007-06-01", "price": 68.41}, {"symbol": "AMZN", "date": "2007-07-01", "price": 78.54}, {"symbol": "AMZN", "date": "2007-08-01", "price": 79.91}, {"symbol": "AMZN", "date": "2007-09-01", "price": 93.15}, {"symbol": "AMZN", "date": "2007-10-01", "price": 89.15}, {"symbol": "AMZN", "date": "2007-11-01", "price": 90.56}, {"symbol": "AMZN", "date": "2007-12-01", "price": 92.64}, {"symbol": "AMZN", "date": "2008-01-01", "price": 77.7}, {"symbol": "AMZN", "date": "2008-02-01", "price": 64.47}, {"symbol": "AMZN", "date": "2008-03-01", "price": 71.3}, {"symbol": "AMZN", "date": "2008-04-01", "price": 78.63}, {"symbol": "AMZN", "date": "2008-05-01", "price": 81.62}, {"symbol": "AMZN", "date": "2008-06-01", "price": 73.33}, {"symbol": "AMZN", "date": "2008-07-01", "price": 76.34}, {"symbol": "AMZN", "date": "2008-08-01", "price": 80.81}, {"symbol": "AMZN", "date": "2008-09-01", "price": 72.76}, {"symbol": "AMZN", "date": "2008-10-01", "price": 57.24}, {"symbol": "AMZN", "date": "2008-11-01", "price": 42.7}, {"symbol": "AMZN", "date": "2008-12-01", "price": 51.28}, {"symbol": "AMZN", "date": "2009-01-01", "price": 58.82}, {"symbol": "AMZN", "date": "2009-02-01", "price": 64.79}, {"symbol": "AMZN", "date": "2009-03-01", "price": 73.44}, {"symbol": "AMZN", "date": "2009-04-01", "price": 80.52}, {"symbol": "AMZN", "date": "2009-05-01", "price": 77.99}, {"symbol": "AMZN", "date": "2009-06-01", "price": 83.66}, {"symbol": "AMZN", "date": "2009-07-01", "price": 85.76}, {"symbol": "AMZN", "date": "2009-08-01", "price": 81.19}, {"symbol": "AMZN", "date": "2009-09-01", "price": 93.36}, {"symbol": "AMZN", "date": "2009-10-01", "price": 118.81}, {"symbol": "AMZN", "date": "2009-11-01", "price": 135.91}, {"symbol": "AMZN", "date": "2009-12-01", "price": 134.52}, {"symbol": "AMZN", "date": "2010-01-01", "price": 125.41}, {"symbol": "AMZN", "date": "2010-02-01", "price": 118.4}, {"symbol": "AMZN", "date": "2010-03-01", "price": 128.82}, {"symbol": "IBM", "date": "2000-01-01", "price": 100.52}, {"symbol": "IBM", "date": "2000-02-01", "price": 92.11}, {"symbol": "IBM", "date": "2000-03-01", "price": 106.11}, {"symbol": "IBM", "date": "2000-04-01", "price": 99.95}, {"symbol": "IBM", "date": "2000-05-01", "price": 96.31}, {"symbol": "IBM", "date": "2000-06-01", "price": 98.33}, {"symbol": "IBM", "date": "2000-07-01", "price": 100.74}, {"symbol": "IBM", "date": "2000-08-01", "price": 118.62}, {"symbol": "IBM", "date": "2000-09-01", "price": 101.19}, {"symbol": "IBM", "date": "2000-10-01", "price": 88.5}, {"symbol": "IBM", "date": "2000-11-01", "price": 84.12}, {"symbol": "IBM", "date": "2000-12-01", "price": 76.47}, {"symbol": "IBM", "date": "2001-01-01", "price": 100.76}, {"symbol": "IBM", "date": "2001-02-01", "price": 89.98}, {"symbol": "IBM", "date": "2001-03-01", "price": 86.63}, {"symbol": "IBM", "date": "2001-04-01", "price": 103.7}, {"symbol": "IBM", "date": "2001-05-01", "price": 100.82}, {"symbol": "IBM", "date": "2001-06-01", "price": 102.35}, {"symbol": "IBM", "date": "2001-07-01", "price": 94.87}, {"symbol": "IBM", "date": "2001-08-01", "price": 90.25}, {"symbol": "IBM", "date": "2001-09-01", "price": 82.82}, {"symbol": "IBM", "date": "2001-10-01", "price": 97.58}, {"symbol": "IBM", "date": "2001-11-01", "price": 104.5}, {"symbol": "IBM", "date": "2001-12-01", "price": 109.36}, {"symbol": "IBM", "date": "2002-01-01", "price": 97.54}, {"symbol": "IBM", "date": "2002-02-01", "price": 88.82}, {"symbol": "IBM", "date": "2002-03-01", "price": 94.15}, {"symbol": "IBM", "date": "2002-04-01", "price": 75.82}, {"symbol": "IBM", "date": "2002-05-01", "price": 72.97}, {"symbol": "IBM", "date": "2002-06-01", "price": 65.31}, {"symbol": "IBM", "date": "2002-07-01", "price": 63.86}, {"symbol": "IBM", "date": "2002-08-01", "price": 68.52}, {"symbol": "IBM", "date": "2002-09-01", "price": 53.01}, {"symbol": "IBM", "date": "2002-10-01", "price": 71.76}, {"symbol": "IBM", "date": "2002-11-01", "price": 79.16}, {"symbol": "IBM", "date": "2002-12-01", "price": 70.58}, {"symbol": "IBM", "date": "2003-01-01", "price": 71.22}, {"symbol": "IBM", "date": "2003-02-01", "price": 71.13}, {"symbol": "IBM", "date": "2003-03-01", "price": 71.57}, {"symbol": "IBM", "date": "2003-04-01", "price": 77.47}, {"symbol": "IBM", "date": "2003-05-01", "price": 80.48}, {"symbol": "IBM", "date": "2003-06-01", "price": 75.42}, {"symbol": "IBM", "date": "2003-07-01", "price": 74.28}, {"symbol": "IBM", "date": "2003-08-01", "price": 75.12}, {"symbol": "IBM", "date": "2003-09-01", "price": 80.91}, {"symbol": "IBM", "date": "2003-10-01", "price": 81.96}, {"symbol": "IBM", "date": "2003-11-01", "price": 83.08}, {"symbol": "IBM", "date": "2003-12-01", "price": 85.05}, {"symbol": "IBM", "date": "2004-01-01", "price": 91.06}, {"symbol": "IBM", "date": "2004-02-01", "price": 88.7}, {"symbol": "IBM", "date": "2004-03-01", "price": 84.41}, {"symbol": "IBM", "date": "2004-04-01", "price": 81.04}, {"symbol": "IBM", "date": "2004-05-01", "price": 81.59}, {"symbol": "IBM", "date": "2004-06-01", "price": 81.19}, {"symbol": "IBM", "date": "2004-07-01", "price": 80.19}, {"symbol": "IBM", "date": "2004-08-01", "price": 78.17}, {"symbol": "IBM", "date": "2004-09-01", "price": 79.13}, {"symbol": "IBM", "date": "2004-10-01", "price": 82.84}, {"symbol": "IBM", "date": "2004-11-01", "price": 87.15}, {"symbol": "IBM", "date": "2004-12-01", "price": 91.16}, {"symbol": "IBM", "date": "2005-01-01", "price": 86.39}, {"symbol": "IBM", "date": "2005-02-01", "price": 85.78}, {"symbol": "IBM", "date": "2005-03-01", "price": 84.66}, {"symbol": "IBM", "date": "2005-04-01", "price": 70.77}, {"symbol": "IBM", "date": "2005-05-01", "price": 70.18}, {"symbol": "IBM", "date": "2005-06-01", "price": 68.93}, {"symbol": "IBM", "date": "2005-07-01", "price": 77.53}, {"symbol": "IBM", "date": "2005-08-01", "price": 75.07}, {"symbol": "IBM", "date": "2005-09-01", "price": 74.7}, {"symbol": "IBM", "date": "2005-10-01", "price": 76.25}, {"symbol": "IBM", "date": "2005-11-01", "price": 82.98}, {"symbol": "IBM", "date": "2005-12-01", "price": 76.73}, {"symbol": "IBM", "date": "2006-01-01", "price": 75.89}, {"symbol": "IBM", "date": "2006-02-01", "price": 75.09}, {"symbol": "IBM", "date": "2006-03-01", "price": 77.17}, {"symbol": "IBM", "date": "2006-04-01", "price": 77.05}, {"symbol": "IBM", "date": "2006-05-01", "price": 75.04}, {"symbol": "IBM", "date": "2006-06-01", "price": 72.15}, {"symbol": "IBM", "date": "2006-07-01", "price": 72.7}, {"symbol": "IBM", "date": "2006-08-01", "price": 76.35}, {"symbol": "IBM", "date": "2006-09-01", "price": 77.26}, {"symbol": "IBM", "date": "2006-10-01", "price": 87.06}, {"symbol": "IBM", "date": "2006-11-01", "price": 86.95}, {"symbol": "IBM", "date": "2006-12-01", "price": 91.9}, {"symbol": "IBM", "date": "2007-01-01", "price": 93.79}, {"symbol": "IBM", "date": "2007-02-01", "price": 88.18}, {"symbol": "IBM", "date": "2007-03-01", "price": 89.44}, {"symbol": "IBM", "date": "2007-04-01", "price": 96.98}, {"symbol": "IBM", "date": "2007-05-01", "price": 101.54}, {"symbol": "IBM", "date": "2007-06-01", "price": 100.25}, {"symbol": "IBM", "date": "2007-07-01", "price": 105.4}, {"symbol": "IBM", "date": "2007-08-01", "price": 111.54}, {"symbol": "IBM", "date": "2007-09-01", "price": 112.6}, {"symbol": "IBM", "date": "2007-10-01", "price": 111.0}, {"symbol": "IBM", "date": "2007-11-01", "price": 100.9}, {"symbol": "IBM", "date": "2007-12-01", "price": 103.7}, {"symbol": "IBM", "date": "2008-01-01", "price": 102.75}, {"symbol": "IBM", "date": "2008-02-01", "price": 109.64}, {"symbol": "IBM", "date": "2008-03-01", "price": 110.87}, {"symbol": "IBM", "date": "2008-04-01", "price": 116.23}, {"symbol": "IBM", "date": "2008-05-01", "price": 125.14}, {"symbol": "IBM", "date": "2008-06-01", "price": 114.6}, {"symbol": "IBM", "date": "2008-07-01", "price": 123.74}, {"symbol": "IBM", "date": "2008-08-01", "price": 118.16}, {"symbol": "IBM", "date": "2008-09-01", "price": 113.53}, {"symbol": "IBM", "date": "2008-10-01", "price": 90.24}, {"symbol": "IBM", "date": "2008-11-01", "price": 79.65}, {"symbol": "IBM", "date": "2008-12-01", "price": 82.15}, {"symbol": "IBM", "date": "2009-01-01", "price": 89.46}, {"symbol": "IBM", "date": "2009-02-01", "price": 90.32}, {"symbol": "IBM", "date": "2009-03-01", "price": 95.09}, {"symbol": "IBM", "date": "2009-04-01", "price": 101.29}, {"symbol": "IBM", "date": "2009-05-01", "price": 104.85}, {"symbol": "IBM", "date": "2009-06-01", "price": 103.01}, {"symbol": "IBM", "date": "2009-07-01", "price": 116.34}, {"symbol": "IBM", "date": "2009-08-01", "price": 117.0}, {"symbol": "IBM", "date": "2009-09-01", "price": 118.55}, {"symbol": "IBM", "date": "2009-10-01", "price": 119.54}, {"symbol": "IBM", "date": "2009-11-01", "price": 125.79}, {"symbol": "IBM", "date": "2009-12-01", "price": 130.32}, {"symbol": "IBM", "date": "2010-01-01", "price": 121.85}, {"symbol": "IBM", "date": "2010-02-01", "price": 127.16}, {"symbol": "IBM", "date": "2010-03-01", "price": 125.55}, {"symbol": "GOOG", "date": "2004-08-01", "price": 102.37}, {"symbol": "GOOG", "date": "2004-09-01", "price": 129.6}, {"symbol": "GOOG", "date": "2004-10-01", "price": 190.64}, {"symbol": "GOOG", "date": "2004-11-01", "price": 181.98}, {"symbol": "GOOG", "date": "2004-12-01", "price": 192.79}, {"symbol": "GOOG", "date": "2005-01-01", "price": 195.62}, {"symbol": "GOOG", "date": "2005-02-01", "price": 187.99}, {"symbol": "GOOG", "date": "2005-03-01", "price": 180.51}, {"symbol": "GOOG", "date": "2005-04-01", "price": 220.0}, {"symbol": "GOOG", "date": "2005-05-01", "price": 277.27}, {"symbol": "GOOG", "date": "2005-06-01", "price": 294.15}, {"symbol": "GOOG", "date": "2005-07-01", "price": 287.76}, {"symbol": "GOOG", "date": "2005-08-01", "price": 286.0}, {"symbol": "GOOG", "date": "2005-09-01", "price": 316.46}, {"symbol": "GOOG", "date": "2005-10-01", "price": 372.14}, {"symbol": "GOOG", "date": "2005-11-01", "price": 404.91}, {"symbol": "GOOG", "date": "2005-12-01", "price": 414.86}, {"symbol": "GOOG", "date": "2006-01-01", "price": 432.66}, {"symbol": "GOOG", "date": "2006-02-01", "price": 362.62}, {"symbol": "GOOG", "date": "2006-03-01", "price": 390.0}, {"symbol": "GOOG", "date": "2006-04-01", "price": 417.94}, {"symbol": "GOOG", "date": "2006-05-01", "price": 371.82}, {"symbol": "GOOG", "date": "2006-06-01", "price": 419.33}, {"symbol": "GOOG", "date": "2006-07-01", "price": 386.6}, {"symbol": "GOOG", "date": "2006-08-01", "price": 378.53}, {"symbol": "GOOG", "date": "2006-09-01", "price": 401.9}, {"symbol": "GOOG", "date": "2006-10-01", "price": 476.39}, {"symbol": "GOOG", "date": "2006-11-01", "price": 484.81}, {"symbol": "GOOG", "date": "2006-12-01", "price": 460.48}, {"symbol": "GOOG", "date": "2007-01-01", "price": 501.5}, {"symbol": "GOOG", "date": "2007-02-01", "price": 449.45}, {"symbol": "GOOG", "date": "2007-03-01", "price": 458.16}, {"symbol": "GOOG", "date": "2007-04-01", "price": 471.38}, {"symbol": "GOOG", "date": "2007-05-01", "price": 497.91}, {"symbol": "GOOG", "date": "2007-06-01", "price": 522.7}, {"symbol": "GOOG", "date": "2007-07-01", "price": 510.0}, {"symbol": "GOOG", "date": "2007-08-01", "price": 515.25}, {"symbol": "GOOG", "date": "2007-09-01", "price": 567.27}, {"symbol": "GOOG", "date": "2007-10-01", "price": 707.0}, {"symbol": "GOOG", "date": "2007-11-01", "price": 693.0}, {"symbol": "GOOG", "date": "2007-12-01", "price": 691.48}, {"symbol": "GOOG", "date": "2008-01-01", "price": 564.3}, {"symbol": "GOOG", "date": "2008-02-01", "price": 471.18}, {"symbol": "GOOG", "date": "2008-03-01", "price": 440.47}, {"symbol": "GOOG", "date": "2008-04-01", "price": 574.29}, {"symbol": "GOOG", "date": "2008-05-01", "price": 585.8}, {"symbol": "GOOG", "date": "2008-06-01", "price": 526.42}, {"symbol": "GOOG", "date": "2008-07-01", "price": 473.75}, {"symbol": "GOOG", "date": "2008-08-01", "price": 463.29}, {"symbol": "GOOG", "date": "2008-09-01", "price": 400.52}, {"symbol": "GOOG", "date": "2008-10-01", "price": 359.36}, {"symbol": "GOOG", "date": "2008-11-01", "price": 292.96}, {"symbol": "GOOG", "date": "2008-12-01", "price": 307.65}, {"symbol": "GOOG", "date": "2009-01-01", "price": 338.53}, {"symbol": "GOOG", "date": "2009-02-01", "price": 337.99}, {"symbol": "GOOG", "date": "2009-03-01", "price": 348.06}, {"symbol": "GOOG", "date": "2009-04-01", "price": 395.97}, {"symbol": "GOOG", "date": "2009-05-01", "price": 417.23}, {"symbol": "GOOG", "date": "2009-06-01", "price": 421.59}, {"symbol": "GOOG", "date": "2009-07-01", "price": 443.05}, {"symbol": "GOOG", "date": "2009-08-01", "price": 461.67}, {"symbol": "GOOG", "date": "2009-09-01", "price": 495.85}, {"symbol": "GOOG", "date": "2009-10-01", "price": 536.12}, {"symbol": "GOOG", "date": "2009-11-01", "price": 583.0}, {"symbol": "GOOG", "date": "2009-12-01", "price": 619.98}, {"symbol": "GOOG", "date": "2010-01-01", "price": 529.94}, {"symbol": "GOOG", "date": "2010-02-01", "price": 526.8}, {"symbol": "GOOG", "date": "2010-03-01", "price": 560.19}, {"symbol": "AAPL", "date": "2000-01-01", "price": 25.94}, {"symbol": "AAPL", "date": "2000-02-01", "price": 28.66}, {"symbol": "AAPL", "date": "2000-03-01", "price": 33.95}, {"symbol": "AAPL", "date": "2000-04-01", "price": 31.01}, {"symbol": "AAPL", "date": "2000-05-01", "price": 21.0}, {"symbol": "AAPL", "date": "2000-06-01", "price": 26.19}, {"symbol": "AAPL", "date": "2000-07-01", "price": 25.41}, {"symbol": "AAPL", "date": "2000-08-01", "price": 30.47}, {"symbol": "AAPL", "date": "2000-09-01", "price": 12.88}, {"symbol": "AAPL", "date": "2000-10-01", "price": 9.78}, {"symbol": "AAPL", "date": "2000-11-01", "price": 8.25}, {"symbol": "AAPL", "date": "2000-12-01", "price": 7.44}, {"symbol": "AAPL", "date": "2001-01-01", "price": 10.81}, {"symbol": "AAPL", "date": "2001-02-01", "price": 9.12}, {"symbol": "AAPL", "date": "2001-03-01", "price": 11.03}, {"symbol": "AAPL", "date": "2001-04-01", "price": 12.74}, {"symbol": "AAPL", "date": "2001-05-01", "price": 9.98}, {"symbol": "AAPL", "date": "2001-06-01", "price": 11.62}, {"symbol": "AAPL", "date": "2001-07-01", "price": 9.4}, {"symbol": "AAPL", "date": "2001-08-01", "price": 9.27}, {"symbol": "AAPL", "date": "2001-09-01", "price": 7.76}, {"symbol": "AAPL", "date": "2001-10-01", "price": 8.78}, {"symbol": "AAPL", "date": "2001-11-01", "price": 10.65}, {"symbol": "AAPL", "date": "2001-12-01", "price": 10.95}, {"symbol": "AAPL", "date": "2002-01-01", "price": 12.36}, {"symbol": "AAPL", "date": "2002-02-01", "price": 10.85}, {"symbol": "AAPL", "date": "2002-03-01", "price": 11.84}, {"symbol": "AAPL", "date": "2002-04-01", "price": 12.14}, {"symbol": "AAPL", "date": "2002-05-01", "price": 11.65}, {"symbol": "AAPL", "date": "2002-06-01", "price": 8.86}, {"symbol": "AAPL", "date": "2002-07-01", "price": 7.63}, {"symbol": "AAPL", "date": "2002-08-01", "price": 7.38}, {"symbol": "AAPL", "date": "2002-09-01", "price": 7.25}, {"symbol": "AAPL", "date": "2002-10-01", "price": 8.03}, {"symbol": "AAPL", "date": "2002-11-01", "price": 7.75}, {"symbol": "AAPL", "date": "2002-12-01", "price": 7.16}, {"symbol": "AAPL", "date": "2003-01-01", "price": 7.18}, {"symbol": "AAPL", "date": "2003-02-01", "price": 7.51}, {"symbol": "AAPL", "date": "2003-03-01", "price": 7.07}, {"symbol": "AAPL", "date": "2003-04-01", "price": 7.11}, {"symbol": "AAPL", "date": "2003-05-01", "price": 8.98}, {"symbol": "AAPL", "date": "2003-06-01", "price": 9.53}, {"symbol": "AAPL", "date": "2003-07-01", "price": 10.54}, {"symbol": "AAPL", "date": "2003-08-01", "price": 11.31}, {"symbol": "AAPL", "date": "2003-09-01", "price": 10.36}, {"symbol": "AAPL", "date": "2003-10-01", "price": 11.44}, {"symbol": "AAPL", "date": "2003-11-01", "price": 10.45}, {"symbol": "AAPL", "date": "2003-12-01", "price": 10.69}, {"symbol": "AAPL", "date": "2004-01-01", "price": 11.28}, {"symbol": "AAPL", "date": "2004-02-01", "price": 11.96}, {"symbol": "AAPL", "date": "2004-03-01", "price": 13.52}, {"symbol": "AAPL", "date": "2004-04-01", "price": 12.89}, {"symbol": "AAPL", "date": "2004-05-01", "price": 14.03}, {"symbol": "AAPL", "date": "2004-06-01", "price": 16.27}, {"symbol": "AAPL", "date": "2004-07-01", "price": 16.17}, {"symbol": "AAPL", "date": "2004-08-01", "price": 17.25}, {"symbol": "AAPL", "date": "2004-09-01", "price": 19.38}, {"symbol": "AAPL", "date": "2004-10-01", "price": 26.2}, {"symbol": "AAPL", "date": "2004-11-01", "price": 33.53}, {"symbol": "AAPL", "date": "2004-12-01", "price": 32.2}, {"symbol": "AAPL", "date": "2005-01-01", "price": 38.45}, {"symbol": "AAPL", "date": "2005-02-01", "price": 44.86}, {"symbol": "AAPL", "date": "2005-03-01", "price": 41.67}, {"symbol": "AAPL", "date": "2005-04-01", "price": 36.06}, {"symbol": "AAPL", "date": "2005-05-01", "price": 39.76}, {"symbol": "AAPL", "date": "2005-06-01", "price": 36.81}, {"symbol": "AAPL", "date": "2005-07-01", "price": 42.65}, {"symbol": "AAPL", "date": "2005-08-01", "price": 46.89}, {"symbol": "AAPL", "date": "2005-09-01", "price": 53.61}, {"symbol": "AAPL", "date": "2005-10-01", "price": 57.59}, {"symbol": "AAPL", "date": "2005-11-01", "price": 67.82}, {"symbol": "AAPL", "date": "2005-12-01", "price": 71.89}, {"symbol": "AAPL", "date": "2006-01-01", "price": 75.51}, {"symbol": "AAPL", "date": "2006-02-01", "price": 68.49}, {"symbol": "AAPL", "date": "2006-03-01", "price": 62.72}, {"symbol": "AAPL", "date": "2006-04-01", "price": 70.39}, {"symbol": "AAPL", "date": "2006-05-01", "price": 59.77}, {"symbol": "AAPL", "date": "2006-06-01", "price": 57.27}, {"symbol": "AAPL", "date": "2006-07-01", "price": 67.96}, {"symbol": "AAPL", "date": "2006-08-01", "price": 67.85}, {"symbol": "AAPL", "date": "2006-09-01", "price": 76.98}, {"symbol": "AAPL", "date": "2006-10-01", "price": 81.08}, {"symbol": "AAPL", "date": "2006-11-01", "price": 91.66}, {"symbol": "AAPL", "date": "2006-12-01", "price": 84.84}, {"symbol": "AAPL", "date": "2007-01-01", "price": 85.73}, {"symbol": "AAPL", "date": "2007-02-01", "price": 84.61}, {"symbol": "AAPL", "date": "2007-03-01", "price": 92.91}, {"symbol": "AAPL", "date": "2007-04-01", "price": 99.8}, {"symbol": "AAPL", "date": "2007-05-01", "price": 121.19}, {"symbol": "AAPL", "date": "2007-06-01", "price": 122.04}, {"symbol": "AAPL", "date": "2007-07-01", "price": 131.76}, {"symbol": "AAPL", "date": "2007-08-01", "price": 138.48}, {"symbol": "AAPL", "date": "2007-09-01", "price": 153.47}, {"symbol": "AAPL", "date": "2007-10-01", "price": 189.95}, {"symbol": "AAPL", "date": "2007-11-01", "price": 182.22}, {"symbol": "AAPL", "date": "2007-12-01", "price": 198.08}, {"symbol": "AAPL", "date": "2008-01-01", "price": 135.36}, {"symbol": "AAPL", "date": "2008-02-01", "price": 125.02}, {"symbol": "AAPL", "date": "2008-03-01", "price": 143.5}, {"symbol": "AAPL", "date": "2008-04-01", "price": 173.95}, {"symbol": "AAPL", "date": "2008-05-01", "price": 188.75}, {"symbol": "AAPL", "date": "2008-06-01", "price": 167.44}, {"symbol": "AAPL", "date": "2008-07-01", "price": 158.95}, {"symbol": "AAPL", "date": "2008-08-01", "price": 169.53}, {"symbol": "AAPL", "date": "2008-09-01", "price": 113.66}, {"symbol": "AAPL", "date": "2008-10-01", "price": 107.59}, {"symbol": "AAPL", "date": "2008-11-01", "price": 92.67}, {"symbol": "AAPL", "date": "2008-12-01", "price": 85.35}, {"symbol": "AAPL", "date": "2009-01-01", "price": 90.13}, {"symbol": "AAPL", "date": "2009-02-01", "price": 89.31}, {"symbol": "AAPL", "date": "2009-03-01", "price": 105.12}, {"symbol": "AAPL", "date": "2009-04-01", "price": 125.83}, {"symbol": "AAPL", "date": "2009-05-01", "price": 135.81}, {"symbol": "AAPL", "date": "2009-06-01", "price": 142.43}, {"symbol": "AAPL", "date": "2009-07-01", "price": 163.39}, {"symbol": "AAPL", "date": "2009-08-01", "price": 168.21}, {"symbol": "AAPL", "date": "2009-09-01", "price": 185.35}, {"symbol": "AAPL", "date": "2009-10-01", "price": 188.5}, {"symbol": "AAPL", "date": "2009-11-01", "price": 199.91}, {"symbol": "AAPL", "date": "2009-12-01", "price": 210.73}, {"symbol": "AAPL", "date": "2010-01-01", "price": 192.06}, {"symbol": "AAPL", "date": "2010-02-01", "price": 204.62}, {"symbol": "AAPL", "date": "2010-03-01", "price": 223.02}]}, "height": 300, "title": "Stock History", "width": 600, "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt = {"mode": "vega-lite"};

function showError(el, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el = document.getElementById('vis');
vegaEmbed("#vis1", spec, embed_opt)
.catch(error => showError(el, error));
</script>




## Airports Example

Here's the first chart, US airports based on this example:

Also, I would love to recreate this [vega example chart](http://vega.github.io/vega-tutorials/airports/) that shows flights between cities in the US.

```python
import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, feature='states')
airports = data.airports.url

# US states background
background = alt.Chart(states).mark_geoshape(
	fill='lightgray',
	stroke='white',
	).properties(
	width=800,
	height=500
	).project('albersUsa')

# airport positions on background
points = alt.Chart(airports).mark_circle().encode(
	longitude='longitude:Q',
	latitude='latitude:Q',
	size=alt.value(15),
	color=alt.value('#3377B3'),
	tooltip=['iata:N','name:N','city:N','state:N','latitude:Q','longitude:Q'],
	)

chart = (background + points)
chart.save('airports.html')
chart
```

<div id="vis2"></div>
<script type="text/javascript">
var spec2 = {"config": {"view": {"width": 400, "height": 300}}, "layer": [{"data": {"url": "https://vega.github.io/vega-datasets/data/us-10m.json", "format": {"feature": "states", "type": "topojson"}}, "mark": {"type": "geoshape", "fill": "lightgray", "stroke": "white"}, "height": 500, "projection": {"type": "albersUsa"}, "width": 800}, {"data": {"url": "https://vega.github.io/vega-datasets/data/airports.csv"}, "mark": "circle", "encoding": {"color": {"value": "#3377B3"}, "latitude": {"type": "quantitative", "field": "latitude"}, "longitude": {"type": "quantitative", "field": "longitude"}, "size": {"value": 15}, "tooltip": [{"type": "nominal", "field": "iata"}, {"type": "nominal", "field": "name"}, {"type": "nominal", "field": "city"}, {"type": "nominal", "field": "state"}, {"type": "quantitative", "field": "latitude"}, {"type": "quantitative", "field": "longitude"}]}}], "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt2 = {"mode": "vega-lite"};

function showError(el2, error){
el2.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el2 = document.getElementById('vis2');
vegaEmbed("#vis2", spec2, embed_opt2)
.catch(error => showError(el2, error));
</script>



## Birdstrikes Example

```python
# This example borrows heavily from the Seattle Weather Interactive example:
# https://altair-viz.github.io/gallery/seattle_weather_interactive.html

import altair as alt 
from vega_datasets import data

# scale = alt.Scale(domain=['European starling', 'Rock pigeon', 'Mourning dove'
#                           , 'Canada goose', 'Red-tailed hawk'],
#                   range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
# color = alt.Color('Wildlife__Species:N', scale=scale)

color = alt.Color('Wildlife__Species:N')

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_circle().encode(
    alt.X('Flight_Date:T', axis=alt.Axis(title='Date')),
    alt.Y('Speed_IAS_in_knots:Q',
        axis=alt.Axis(title='Indicated Airspeed (kts)'),
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
).properties(
    width=600,
    height=300
).add_selection(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of species
bars = alt.Chart().mark_bar().encode(
    alt.Y('count()', scale=alt.Scale(type='log')),
    alt.X('Wildlife__Species:N', sort=alt.SortField(field='sort_order', op='count', order='descending')),
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=600,
).add_selection(
    click
)

alt.vconcat(points, bars,
    data=data.birdstrikes.url,
    title="Aircraft Birdstrikes: 1990-2003"
).save('birdstrikes.html')
```


<div id="vis3"></div>
<script type="text/javascript">
var spec3 = {"config": {"view": {"width": 400, "height": 300}}, "vconcat": [{"mark": "circle", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector094"}, "value": "lightgray"}, "tooltip": [{"type": "nominal", "field": "Airport__Name"}, {"type": "nominal", "field": "Aircraft__Make_Model"}, {"type": "temporal", "field": "Flight_Date"}, {"type": "nominal", "field": "Aircraft__Airline_Operator"}, {"type": "nominal", "field": "Origin_State"}, {"type": "nominal", "field": "When__Phase_of_flight"}, {"type": "nominal", "field": "Wildlife__Species"}, {"type": "nominal", "field": "Wildlife__Size"}, {"type": "nominal", "field": "Speed_IAS_in_knots"}], "x": {"type": "temporal", "axis": {"title": "Date"}, "field": "Flight_Date"}, "y": {"type": "quantitative", "axis": {"title": "Indicated Airspeed (kts)"}, "field": "Speed_IAS_in_knots"}}, "height": 300, "selection": {"selector094": {"type": "interval", "encodings": ["x"]}}, "transform": [{"filter": {"selection": "selector095"}}], "width": 600}, {"mark": "bar", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector095"}, "value": "lightgray"}, "x": {"type": "nominal", "field": "Wildlife__Species", "sort": {"op": "count", "field": "sort_order", "order": "descending"}}, "y": {"type": "quantitative", "aggregate": "count", "scale": {"type": "log"}}}, "selection": {"selector095": {"type": "multi", "encodings": ["color"]}}, "transform": [{"filter": {"selection": "selector094"}}], "width": 600}], "data": {"url": "https://vega.github.io/vega-datasets/data/birdstrikes.json"}, "title": "Aircraft Birdstrikes: 1990-2003", "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt3 = {"mode": "vega-lite"};

function showError(el3, error){
el3.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el3 = document.getElementById('vis3');
vegaEmbed("#vis3", spec3, embed_opt3)
.catch(error => showError(el3, error));
</script>




# Sharing Interactive Altair Charts

<!-- {% notebook downloads/notebooks/altair-interactive/Altair-interactive.ipynb cells[:] %} -->
Tried notebook, but does not render interctive plots..., so do manually



## Pelican Template

Add to `<article-name>.md`:

`include: vega`

Add to `theme/templates/article.html`. This loads the vega javascript libraries and style if required. 

```html
{% if 'vega' in article.include %}
<style>
.vega-actions a {
	margin-right: 12px;
	color: #757575;
	font-weight: normal;
	font-size: 13px;
}
.error {
	color: red;
}
</style>
<script src="https://cdn.jsdelivr.net/npm//vega@3.3.1"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-lite@2.4.3"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-embed@3.11"></script>
{% endif %}
```


## Single Plot in MD

To add a single plot, we open the `<chart-name>.html` file and copy this portion (note that you need to remove indentation): 

```html
<div id="vis1"></div>
<script type="text/javascript">
var spec = {"config": {"view": {"width": 400, "height": 300}}, "layer": [{"data": {"url": "https://vega.github.io/vega-datasets/data/us-10m.json", "format": {"feature": "states", "type": "topojson"}}, "mark": {"type": "geoshape", "fill": "lightgray", "stroke": "white"}, "height": 500, "projection": {"type": "albersUsa"}, "width": 800}, {"data": {"url": "https://vega.github.io/vega-datasets/data/airports.csv"}, "mark": "circle", "encoding": {"color": {"value": "#3377B3"}, "latitude": {"type": "quantitative", "field": "latitude"}, "longitude": {"type": "quantitative", "field": "longitude"}, "size": {"value": 15}, "tooltip": [{"type": "nominal", "field": "iata"}, {"type": "nominal", "field": "name"}, {"type": "nominal", "field": "city"}, {"type": "nominal", "field": "state"}, {"type": "quantitative", "field": "latitude"}, {"type": "quantitative", "field": "longitude"}]}}], "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt = {"mode": "vega-lite"};

function showError(el, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el = document.getElementById('vis1');
vegaEmbed("#vis1", spec, embed_opt)
.catch(error => showError(el, error));
</script>
```

## Multiple Plots in MD

When adding subsequent plots to the same page, we need to increment certain variables to enable the additional plot to render:

```html
<div id="vis2"></div>
<script type="text/javascript">
var spec2 = {"config": {"view": {"width": 400, "height": 300}}, "vconcat": [{"mark": "circle", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector094"}, "value": "lightgray"}, "tooltip": [{"type": "nominal", "field": "Airport__Name"}, {"type": "nominal", "field": "Aircraft__Make_Model"}, {"type": "temporal", "field": "Flight_Date"}, {"type": "nominal", "field": "Aircraft__Airline_Operator"}, {"type": "nominal", "field": "Origin_State"}, {"type": "nominal", "field": "When__Phase_of_flight"}, {"type": "nominal", "field": "Wildlife__Species"}, {"type": "nominal", "field": "Wildlife__Size"}, {"type": "nominal", "field": "Speed_IAS_in_knots"}], "x": {"type": "temporal", "axis": {"title": "Date"}, "field": "Flight_Date"}, "y": {"type": "quantitative", "axis": {"title": "Indicated Airspeed (kts)"}, "field": "Speed_IAS_in_knots"}}, "height": 300, "selection": {"selector094": {"type": "interval", "encodings": ["x"]}}, "transform": [{"filter": {"selection": "selector095"}}], "width": 600}, {"mark": "bar", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector095"}, "value": "lightgray"}, "x": {"type": "nominal", "field": "Wildlife__Species", "sort": {"op": "count", "field": "sort_order", "order": "descending"}}, "y": {"type": "quantitative", "aggregate": "count", "scale": {"type": "log"}}}, "selection": {"selector095": {"type": "multi", "encodings": ["color"]}}, "transform": [{"filter": {"selection": "selector094"}}], "width": 600}], "data": {"url": "https://vega.github.io/vega-datasets/data/birdstrikes.json"}, "title": "Aircraft Birdstrikes: 1990-2003", "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt2 = {"mode": "vega-lite"};

function showError(el2, error){
el2.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el2 = document.getElementById('vis2');
vegaEmbed("#vis2", spec2, embed_opt2)
.catch(error => showError(el2, error));
</script>
```

# Closing Thoughts
Next step is to make full dashbaords...
Other...


# Resources:
- Data to play with: https://github.com/vega/vega-datasets/tree/gh-pages/data
- Example: https://altair-viz.github.io/user_guide/saving_charts.html#json-format
- [Altair Tutorials](https://github.com/altair-viz/altair-tutorial/tree/master/notebooks)
- [This Intro](http://vallandingham.me/altair_intro.html)
- [pbpython](http://pbpython.com/altair-intro.html)

- Jake VanderPlas' Pycon 2018 tutorial:
<div class="video-container">
        <iframe width="750" height="500" src="https://www.youtube.com/embed/ms29ZPUKxbU" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</div>



---

- *You can view the original [Jupyter Notebook](https://github.com/mkudija/General-Examples/blob/master/Altair/Altair-interactive.ipynb) that was used to generate these examples.*
- *All code examples in this notebook use Altair 2.1.0*