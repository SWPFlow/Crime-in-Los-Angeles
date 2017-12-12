import gmplot
import sqlite3

# Connect to the database
conn = sqlite3.connect('CrimeDB.sqlite')

#Set the cursor
c = conn.cursor()

# Execute the database query. I am fetching business locations in a particular zip.
c.execute("SELECT latitude, longitude, CrimeCodeDescription, DateOccurred FROM crime;")

# Fetch all the data returned by the database query as a list
lat_long = c.fetchall()


# Initialize two empty lists to hold the latitude and longitude values
latitude = []
longitude = []
title = []
date = []

# Transform the the fetched latitude and longitude data into two separate lists
for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])
	title.append(lat_long[i][2])
	date.append(lat_long[i][3])


#function for drawing points on a map
def points():
	# Initialize the map to the first location in the list
	gmap = gmplot.GoogleMapPlotter("34.0522","-118.2437",11)

	# Draw the points on the map.
	n = 0
	for i in latitude:
		gmap.marker(latitude[n], longitude[n],'y',
			title = title[n] + " (" + date[n] + ")")
		n += 1

	# Write the map in an HTML file
	gmap.draw('map.html')
	return;

#function for drawing heatmap
def heatMap():
		# Initialize the map to the first location in the list
		gmap = gmplot.GoogleMapPlotter("34.0522","-118.2437",11)

		# Draw the points on the map.
		gmap.heatmap(latitude, longitude)

		# Write the map in an HTML file
		gmap.draw('map2.html')
		return;

#call plotting fucntions
points()
heatMap()


# Close the cursor and the database connection
c.close()
conn.close()
