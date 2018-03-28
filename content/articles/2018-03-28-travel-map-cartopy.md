Title: Where I Travelled in 2018 with Cartopy
date: 2018-03-27 06:00
updated: 2018-03-27 06:00
comments: true
slug: travel-map-cartopy
tags: cartopy, map, python, matplotlib
status: draft

<!-- PELICAN_BEGIN_SUMMARY -->
![alt]({filename}/images/2018_travel.png)

See former post about [2016 travel](http://matthewkudija.com/blog/2016/12/17/travel-map/) plotted with Basemap. This post uses Cartopy.


<!-- PELICAN_END_SUMMARY -->

```python
# # basic line plot
# import matplotlib.pyplot as plt
# import cartopy.crs as ccrs

# ax = plt.axes(projection=ccrs.Robinson())
# ax.set_global()
# ax.coastlines()

# plt.plot([-0.08, 132], [51.53, 43.17], color='#2E5FAC',  transform=ccrs.Geodetic())
# # plt.plot([-0.08, 132], [51.53, 43.17], color='blue', transform=ccrs.PlateCarree())

# plt.savefig('cartopy.png',bbox_inches='tight')



# # shade land
# import matplotlib.pyplot as plt
# import cartopy.crs as ccrs
# import cartopy

# ax = plt.axes(projection=ccrs.Robinson())
# ax.set_global()
# ax.coastlines()

# # color land and water
# ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='#7f7f7f', facecolor='#B1B2B4')
# ax.add_feature(cartopy.feature.OCEAN, zorder=0, facecolor='white')

# # [lng1, lng2], [lat1, lat2]
# plt.plot([-6.26, -82.99], [53.35, 39.96], color='#2E5FAC',  transform=ccrs.Geodetic())

# plt.savefig('cartopy.png',bbox_inches='tight')


# # zoom in on region
# import matplotlib.pyplot as plt
# import cartopy.crs as ccrs
# import cartopy

# ax = plt.axes(projection=ccrs.Robinson())
# ax.set_global()
# ax.coastlines()

# # [lon_min, lon_max, lat_min, lat_max]
# ax.set_extent([-140, 20, 20, 65])

# # color land and water
# ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='#7f7f7f', facecolor='#B1B2B4')
# ax.add_feature(cartopy.feature.OCEAN, zorder=0, facecolor='white')

# # [lon1, lon2], [lat1, lat2]
# plt.plot([-6.26, -82.99], [53.35, 39.96], color='#2E5FAC',  transform=ccrs.Geodetic())

# plt.savefig('cartopy.png',bbox_inches='tight')

# change projection
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy

ax = plt.axes(projection=ccrs.Mercator(central_longitude=-60, min_latitude=20,
    max_latitude=65, latitude_true_scale=30))
ax.set_global()
ax.coastlines()

# [lon_min, lon_max, lat_min, lat_max]
ax.set_extent([-140, 20, 20, 65])

# color land and water
ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='#7f7f7f', facecolor='#B1B2B4')
ax.add_feature(cartopy.feature.OCEAN, zorder=0, facecolor='white')

# [lon1, lon2], [lat1, lat2]
plt.plot([-6.26, -82.99], [53.35, 39.96], color='#2E5FAC',  transform=ccrs.Geodetic())

plt.savefig('cartopy.png',bbox_inches='tight', dpi=300)
```




## CARTOPY RESOURCES

# https://uoftcoders.github.io/studyGroup/lessons/python/cartography/lesson/

