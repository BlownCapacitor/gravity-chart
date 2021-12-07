import pandas as pd 
import csv
import plotly.express as px


cleandata = pd.read_csv("PDS2.csv")
rows = []
with open ('PDS2.csv', 'r') as f:
  file = csv.reader(f)
  for row in file:
    rows.append(row)
headers = rows[0]
stardata = rows[1:]
print(headers)
print(stardata)
headers[0] = 'row number'

starmass = []
starradius = []
starname = []

for i in stardata:
  starmass.append(i[3])
  starradius.append(i[4])
  starname.append(i[1])
stargravity = []
print("strr", starradius)
for index,name in enumerate(starname):
#Cut it into pieces for debugging purposes
  g = float(starmass[index])
  g2 =  g*5.972e+24
  g3 = g2/(float(starradius[index]))
  g4 = g3*(float(starradius[index]))
  g5 = g4*(6371000*637100)
  g6 = g5*6.674e-11
  stargravity.append(g6)
print(stargravity)

plot = px.scatter(x = starradius, y = starmass, size = stargravity)

plot.show()
