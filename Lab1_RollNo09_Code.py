from matplotlib import pyplot as plot
from matplotlib import style
import pandas as pd
import numpy as np
from statistics import mean, stdev, mode,median,  StatisticsError
file='Gait_data.xlsx'
excel=pd.ExcelFile(file)
f = open("testfile.txt","w") 
new_names=pd.read_excel(excel,'without cp')

new_names=new_names.rename(columns={'stride length (m)': 'stride_length','Cadence (step/min)':'Cadence', 'Leg len (m)':'leg_length','Age (year)':'age'})
f.write("without cp\n")
column_array=['stride_length', 'Cadence', 'leg_length', 'age']
for i in range(0,4):
	for j in range(i+1,4):
		style.use('ggplot')
		plot.scatter(new_names.get(column_array[i]), new_names.get(column_array[j]))
		f.write(column_array[i] + " " + column_array[j] + "\n")
		f.write(str(np.corrcoef(new_names.get(column_array[i]),new_names.get(column_array[j])))+"\n")
		plot.title(column_array[i] +' vs ' + column_array[j])
		plot.ylabel('Cadence(step/min)')
		plot.xlabel('Stride Length')
		plot.show()
	f.write("Mean of " + column_array[i]+ " is:")
	m=mean(new_names.get(column_array[i]))
	f.write(str(m)+"\n")
	f.write("Standard deviation of " + column_array[i]+ " is:")
	f.write(str(stdev(new_names.get(column_array[i])))+"\n")
	f.write("Median of " + column_array[i]+ " is:")
	f.write(str(median(new_names.get(column_array[i])))+"\n")
	try:
		f.write("Mode of " + column_array[i]+ " is:")
		f.write(str(mode(new_names.get(column_array[i])))+"\n")
	except StatisticsError:
		f.write ("No unique mode found"+"\n")


new_names=pd.read_excel(excel,'with cp')
f.write("\n\nwith cp\n")
new_names=new_names.rename(columns={'stride length (m)': 'stride_length','cadence (step/min)':'Cadence', 'leg len (m)':'leg_length','age (year)':'age'})
for i in range(0,4):
	for j in range(i+1,4):
		style.use('ggplot')
		plot.scatter(new_names.get(column_array[i]), new_names.get(column_array[j]))
		f.write(column_array[i] + " " + column_array[j]+"\n")
		f.write(str(np.corrcoef(new_names.get(column_array[i]),new_names.get(column_array[j])))+"\n")
		plot.title(column_array[i] +' vs ' + column_array[j])
		plot.ylabel('Cadence(step/min)')
		plot.xlabel('Stride Length')
		plot.show()
	f.write("Mean of " + column_array[i]+ " is:")
	f.write(str(mean(new_names.get(column_array[i])))+"\n")
	f.write("Standard deviation of " + column_array[i]+ " is:")
	f.write(str(stdev(new_names.get(column_array[i])))+"\n")
	f.write("Median of " + column_array[i]+ " is:")
	f.write(str(median(new_names.get(column_array[i])))+"\n")
	try:
		f.write("Mode of " + column_array[i]+ " is:")
		f.write(str(mode(new_names.get(column_array[i])))+"\n")
	except StatisticsError:
		f.write ("No unique mode found"+"\n")

new_names=pd.read_excel(excel,'Combined')
f.write("\n\nCombined\n")
new_names=new_names.rename(columns={'stride length (m)': 'stride_length','cadence (step/min)':'Cadence', 'leg len (m)':'leg_length','age (year)':'age'})
for i in range(0,4):
	for j in range(i+1,4):
		style.use('ggplot')
		plot.scatter(new_names.get(column_array[i]), new_names.get(column_array[j]))
		f.write(column_array[i] + " " + column_array[j]+"\n")
		f.write(str(np.corrcoef(new_names.get(column_array[i]),new_names.get(column_array[j])))+"\n")
		plot.title(column_array[i] +' vs ' + column_array[j])
		plot.ylabel('Cadence(step/min)')
		plot.xlabel('Stride Length')
		plot.show()
	f.write("mean of " + column_array[i]+ " is:")
	f.write(str(mean(new_names.get(column_array[i])))+"\n")
	f.write("standard deviation of " + column_array[i]+ " is:")
	f.write(str(stdev(new_names.get(column_array[i])))+"\n")
	f.write("Median of " + column_array[i]+ " is:")
	f.write(str(median(new_names.get(column_array[i])))+"\n")
	try:
		f.write("Mode of " + column_array[i]+ " is:")
		f.write(str(mode(new_names.get(column_array[i])))+"\n")
	except StatisticsError:
		f.write ("No unique mode found"+"\n")
