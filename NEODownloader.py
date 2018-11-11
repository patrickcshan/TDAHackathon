import requests
from NEOClass import Neo

# Information for GET requests
NEOstring = "https://api.nasa.gov/neo/rest/v1/feed?"
apikey = "XQiw6h4tvvj7R3MWkZhcgukq3MeYzfBonn2Duyp2"

def downloadNEOsDate(startdate, enddate, key):
    """
    Access the Nasa api.
    :param startdate: Start Date
    :param enddate: End Date
    :param key: API key used to access
    :return: JSON list of all near earth objects with links to themselves.
    """
    return requests.get(NEOstring+"start_date="+startdate+"&end_date="+enddate+"&api_key="+apikey)

# r2 = downloadNEOsDate("2015-09-07","2015-09-08",apikey).json()

# print(type(r2["near_earth_objects"]["2015-09-08"]))

def generateNEOSDate(startdate, enddate, key):
    """

    :param startdate:
    :param enddate:
    :param key:
    :return:
    """
    r = requests.get(NEOstring+"start_date="+startdate+"&end_date="+enddate+"&api_key="+key).json()
    ret = {}
    for date in r["near_earth_objects"]:
        for obj in r["near_earth_objects"][date]:
            objid = obj["id"]
            jason = requests.get(obj["links"]["self"]).json()
            ret[objid] = Neo(jason,startdate,enddate)
    return ret

dictionary = generateNEOSDate("2015-09-07","2015-09-08",apikey)
print(dictionary)