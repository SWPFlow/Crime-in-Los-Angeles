import gmplot
import sqlite3

# Connect to the database
conn = sqlite3.connect('CrimeDB.sqlite')

#Set the cursor
c = conn.cursor()

# Execute the database query. I am fetching business locations in a particular zip.
c.execute("SELECT latitude, longitude FROM crime;")

# Fetch all the data returned by the database query as a list
lat_long = c.fetchall()

# Initialize two empty lists to hold the latitude and longitude values
latitude = []
longitude = []


# Transform the the fetched latitude and longitude data into two separate lists
for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])

#sort in ascending order
sort = sorted(latitude)

#get zones and return number at those index
q1 = sort[round(len(sort)*.20)]
q2 = sort[round(len(sort)*.40)]
q3 = sort[round(len(sort)*.60)]
q4 = sort[round(len(sort)*.80)]

#lists to hold points in zones
lat1 = []
lat2 = []
lat3 = []
lat4 = []
lat5 = []

lon1 = []
lon2 = []
lon3 = []
lon4 = []
lon5 = []

n = 0
for i in latitude:
    if latitude[n] <= q1:
        lat1.append(latitude[n])
        lon1.append(longitude[n])
        n+=1

    elif latitude[n] > q1 and latitude[n] <= q2:
        lat2.append(latitude[n])
        lon2.append(longitude[n])
        n+=1

    elif latitude[n] > q2 and latitude[n] <= q3:
        lat3.append(latitude[n])
        lon3.append(longitude[n])
        n+=1

    elif latitude[n] > q3 and latitude[n] <= q4:
        lat4.append(latitude[n])
        lon4.append(longitude[n])
        n+=1

    elif latitude[n] > q4:
        lat5.append(latitude[n])
        lon5.append(longitude[n])
        n+=1

#take the average
latAvg1 = [(sum(lat1) / float(len(lat1)))]
lonAvg1 = [(sum(lon1) / float(len(lon1)))]

latAvg2 = [(sum(lat2) / float(len(lat2)))]
lonAvg2 = [(sum(lon2) / float(len(lon2)))]

latAvg3 = [(sum(lat3) / float(len(lat3)))]
lonAvg3 = [(sum(lon3) / float(len(lon3)))]

latAvg4 = [(sum(lat4) / float(len(lat4)))]
lonAvg4 = [(sum(lon4) / float(len(lon4)))]

latAvg5 = [(sum(lat5) / float(len(lat5)))]
lonAvg5 = [(sum(lon5) / float(len(lon5)))]


# Initialize the map to the first location in the list
gmap = gmplot.GoogleMapPlotter("34.0522","-118.2437",11)

# Plot the region
gmap.plot(lat1, lon1, 'yellow', edge_width=10)
gmap.plot(lat2, lon2, 'violet', edge_width=10)
gmap.plot(lat3, lon3, 'red', edge_width=10)
gmap.plot(lat4, lon4, 'orange', edge_width=10)
gmap.plot(lat5, lon5, 'cornflowerblue', edge_width=10)

# find the percent of crimes
p1 = (len(lat1)/len(latitude))*100
p2 = (len(lat2)/len(latitude))*100
p3 = (len(lat3)/len(latitude))*100
p4 = (len(lat4)/len(latitude))*100
p5 = (len(lat5)/len(latitude))*100

# Plot the center of the circle
n = 0
for i in latAvg1:
    gmap.marker(latAvg1[n], lonAvg1[n],'k', title = str(round(p1)) + '% of crime')
    gmap.marker(latAvg2[n], lonAvg2[n],'k', title = str(round(p2)) + '% of crime')
    gmap.marker(latAvg3[n], lonAvg3[n],'k', title = str(round(p3)) + '% of crime')
    gmap.marker(latAvg4[n], lonAvg4[n],'k', title = str(round(p4)) + '% of crime')
    gmap.marker(latAvg5[n], lonAvg5[n],'k', title = str(round(p5)) + '% of crime')
    n+=1




# Write the map in an HTML file
gmap.draw('avg.html')

