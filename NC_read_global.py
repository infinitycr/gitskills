import netCDF4 as nc
from PIL import Image
from pylab import *
import datetime

file='1979-2016Geopotential_500hpa.nc'

data=nc.Dataset(file)
times='2001112506'
d2 = datetime.datetime(1900, 1, 1, 0)
d1 = datetime.datetime(int(''.join(times[0:4])), int(''.join(times[4:6])), int(''.join(times[6:8])),
                       int(''.join(times[8:])))
hour = (d1 - d2).days * 24 + int(''.join(times[8:]))
remain = hour % 6
time_index = (hour - 692496) // 6
if remain == 0:
    print (data.variables['z'][time_index])
    imshow(data.variables['z'][time_index])
    show()
