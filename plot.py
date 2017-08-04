import matplotlib.pyplot as plt
import csv


files = [('alublfx_fast_new3','alublfx_slow_new3'), ('bl_localization_fast', 'bl_localization_slow'),  ('blvpn_fast', 'blvpn_slow')]

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
