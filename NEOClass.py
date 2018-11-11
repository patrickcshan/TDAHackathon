import math
class Neo:

    def __init__(self,JSON,startdate,enddate):
        self.min_diameter = float(JSON["estimated_diameter"]["kilometers"]["estimated_diameter_min"])
        self.max_diameter = float(JSON["estimated_diameter"]["kilometers"]["estimated_diameter_max"])
        self.semi_major_axis = float(JSON["orbital_data"]["semi_major_axis"])*149598000
        self.perihelion_distance = float(JSON["orbital_data"]["perihelion_distance"])*149598000
        self.inclination = float(JSON["orbital_data"]["inclination"])*2*math.pi/360
        self.isDangerous = float(JSON["is_potentially_hazardous_asteroid"])
        self.semi_minor_axis = float(math.sqrt(pow(self.semi_major_axis,2)-math.pow(self.perihelion_distance,2)))
        self.eccentricity = float(JSON["orbital_data"]["eccentricity"])
        self.x = []
        self.y = []
        horz_offset = self.semi_major_axis - self.perihelion_distance
        thetas = range(0, int(2 * math.pi//0.01))
        for t in thetas:
            self.x.append(horz_offset + self.semi_major_axis * math.cos(t*0.01))
            self.y.append(self.semi_minor_axis * math.cos(t*0.01))
        self.pos = 0
        self.refEpoch = None

        for i in JSON["close_approach_data"]:
            if i["close_approach_date"] == startdate or i["close_approach_date"] == enddate:
                self.refEpoch = i["epoch_date_close_approach"]

    def update(self):
        self.pos = (self.pos + 1) % len(self.x)







