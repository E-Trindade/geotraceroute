import sys
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def generate_map(coordinates):
    plt.figure(figsize=(8, 8))
    
    m = Basemap()
    m.drawcoastlines()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral',lake_color='aqua')
    
    lats = [float(lat) for _, lat, __ in coordinates]
    longs = [float(lon) for _, __, lon in coordinates]
    labels = [str(i) for i, _, __ in coordinates]

    m.plot(longs, lats, 'H', color='m')

    for lat, lon, label in zip(lats, longs, labels):
        plt.text(lon+2, lat, s=label)

    plt.show()
    #plt.savefig('map.png')
    print('done')


if __name__ == '__main__':
    file_name = sys.argv[1]
    coordinates = []

    cont = 0

    with open(file_name) as f:
        for line in f:
            if len(line) == 1: continue
            if 'City Edition' not in line: continue
            if 'not found' in line: continue
            cont += 1
            splitted = line.split()
            lat, lon = splitted[12].strip(','), splitted[13].strip(',')
            if lat == 'N/A' or lon == 'N/A': continue
            coordinates.append((cont, lat, lon))
    print(coordinates)
    generate_map(coordinates)
