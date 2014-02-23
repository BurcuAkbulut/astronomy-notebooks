import os, urllib2

DATA_SETS = [
    'ftp://cdsarc.u-strasbg.fr/pub/cats/I/239/hip_main.dat.gz',
    'ftp://cdsarc.u-strasbg.fr/pub/cats/VI/42/data.dat',
    'http://ssd.jpl.nasa.gov/dat/ELEMENTS.COMET',
    'http://ssd.jpl.nasa.gov/dat/ELEMENTS.NUMBR.gz',
    'http://ssd.jpl.nasa.gov/dat/ELEMENTS.UNNUM.gz',
    'http://www.celestrak.com/NORAD/elements/visual.txt',
    'http://www.pbarbier.com/constellations/bound_verts_18.txt',
    'https://raw.github.com/astronexus/HYG-Database/master/hygfull.csv',
    ]

def get_data_set(url):
    fname = url.split('/')[-1]
    if os.path.isfile(fname):
        return
    data = urllib2.urlopen(url).read()
    with open(fname, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    os.chdir(this_dir or '.')
    os.chdir('data')
    for url in DATA_SETS:
        get_data_set(url)
