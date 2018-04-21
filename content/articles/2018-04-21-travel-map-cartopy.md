Title: Travel Map With Cartopy
date: 2018-04-21 06:00
updated: 2018-04-20 06:00
authors: Matthew Kudija
comments: true
slug: travel-map-cartopy
tags: cartopy, map, python, matplotlib

<!-- PELICAN_BEGIN_SUMMARY -->
![alt]({filename}../downloads/notebooks/travel-map-cartopy/2018_Travel.png)

In a [former post](http://matthewkudija.com/blog/2016/12/17/travel-map/) I generated a travel map plotted with Basemap. From the [Basemap documentation](https://matplotlib.org/basemap/users/intro.html#cartopy-new-management-and-eol-announcement), however, Cartopy will replace Basemap:

> Starting in 2016, Basemap came under new management. The Cartopy project will replace Basemap, but it hasn’t yet implemented all of Basemap’s features. All new software development should try to use Cartopy whenever possible, and existing software should start the process of switching over to use Cartopy. All maintenance and development efforts should be focused on Cartopy.


In this post, I generate a similar travel map using Cartopy.

<!-- PELICAN_END_SUMMARY -->

{% notebook downloads/notebooks/travel-map-cartopy/Cartopy.ipynb cells[1:] %}

*This post was written entirely in the Jupyter notebook. You can [download](downloads/notebooks/CartopyTravel/Cartopy.ipynb) the original notebook.*