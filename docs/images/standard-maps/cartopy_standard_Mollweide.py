import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs


def main():

    # configure chart
    plt.close()
    plt.style.use('mag')

    ax = plt.axes(projection=ccrs.Mollweide())
    
    ax.add_feature(cartopy.feature.LAND, zorder=0, linewidth=.001,
               facecolor='#B1B2B4')
    ax.add_feature(cartopy.feature.OCEAN, facecolor='white')
    ax.set_global()
    ax.outline_patch.set_edgecolor('white')

    # grey
    title = 'maps/world_Mollweide_grey.png'
    plt.savefig(title, bbox_inches='tight', pad_inches=.2, dpi=300)
    print('Saved: {}'.format(title))

    # blue
    ax.add_feature(cartopy.feature.LAND, zorder=0, facecolor='#3377b3', linewidth=.001)
    title = 'maps/world_Mollweide_blue.png'
    plt.savefig(title, bbox_inches='tight', pad_inches=.2, dpi=300)
    print('Saved: {}'.format(title))

    # blue countries
    ax.add_feature(cartopy.feature.BORDERS, edgecolor='white', linewidth=.25)
    title = 'maps/world_Mollweide_blue_countries.png'
    plt.savefig(title, bbox_inches='tight', pad_inches=.2, dpi=300)
    print('Saved: {}'.format(title))

    # grey countries
    ax.add_feature(cartopy.feature.LAND, zorder=0, facecolor='#B1B2B4', linewidth=.001)
    ax.add_feature(cartopy.feature.BORDERS, edgecolor='white', linewidth=.25)
    title = 'maps/world_Mollweide_grey_countries.png'
    plt.savefig(title, bbox_inches='tight', pad_inches=.2, dpi=300)
    print('Saved: {}'.format(title))


if __name__ == '__main__':
    main()