import math

''' calculation class '''

EARTH_RADIUS = 6377.830 

def rad(temp):
	return temp*math.pi/180.0

def CalDistance(lat1,lng1,lat2,lng2):
	radLat1 = rad(lat1)
	radLat2 = rad(lat2)
	a = radLat1 - radLat2
	b = rad(lng1) - rad(lng2)
	s = 2*math.asin(math.sqrt(math.pow(a/2,2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))
	s = s*EARTH_RADIUS*1000
	return s