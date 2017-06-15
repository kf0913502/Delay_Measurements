import matplotlib.pyplot as plt
import csv


files = [('airportFast','airportSlow'),('airportFast2','airportSlow2'),('androidFast','androidSlow'),('blocFast','blocSlow'),('iphoneFast','iphoneSlow'),('iphoneFast2','iphoneSlow2'),('iphoneFast3','iphoneSlow3'),('nokiaApFast','nokiaApSlow'),('nokiaApFast2','nokiaApSlow2'),('nokiaApFast3','nokiaApSlow3'),('TCDwifiFast','TCDwifiSlow'),('tplinkFast','tplinkSlow'), ('monteroseFast','monteroseSlow')]

for f in files:
	fastFile = open(f[0], 'rb')
	slowFile = open(f[1],'rb')
        fastReader = csv.reader(fastFile, delimiter=',')
        slowReader = csv.reader(slowFile, delimiter=',')
	slowXValues = list()
	slowYValues = list()
	fastXValues = list()
	fastYValues = list()
	for row in slowReader:
		slowXValues.append(row[0])
		slowYValues.append(row[1])
	for row in fastReader:
		fastXValues.append(row[0])
		fastYValues.append(row[1])


	fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
	ax.plot(slowXValues, slowYValues,'r--', fastXValues,fastYValues,'b--')
	fig.savefig('figures/' + f[0] + '.png')   # save the figure to file
	plt.close(fig)    # close the figure
