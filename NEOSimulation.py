from numpy import radians
from scipy.constants import kilo

from orbital import earth, KeplerianElements, Maneuver, plot, plot3d

from NEOClass import Neo
from NEODownloader import generateNEOSDate, apikey

NEOs = generateNEOSDate("2015-09-07","2015-09-08", apikey)
orbits = {}
for i in NEOs:
    obj = NEOs[i]
    orbits[i] = KeplerianElements(a = obj.semi_major_axis, e = obj.eccentricity,
                                  i = obj.inclination, arg_pe=obj.perihelion_distance,
                                  ref_epoch=obj.refEpoch,body=earth)

k = 0
for i in orbits:
    k = i
print(orbits[k])
plot(orbits[k], title=k, animate=True)