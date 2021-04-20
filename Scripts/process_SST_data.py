import setup
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits import mplot3d

setup.dataPath

if __name__ == '__main__':
	
	#set up variables
	filename = 'HadISST_sst.nc'

	#import file
	data = xr.open_dataset(filename)

	#set up the variables
	sst = data.sst

	#plotting
	plt.figure()
	plt.contourf(sst.longitude,sst.latitude,sst.where(sst >= -5).mean(dim="time"), cmap= "cool")
	plt.colorbar(label = 'Temperature')
	plt.xlabel('longitude')
	plt.ylabel('latitude')
	plt.savefig("Global Ocean SST", dpi =300)
	plt.show()

	#variables for the Atlantic Ocean plot
	atlantic1 = sst.where(sst.longitude <= 50)
	atlantic2 = atlantic1.where(atlantic1.longitude >= -100)

	#plotting the Atlantic Ocean
	plt.figure()
	plt.contourf(atlantic2.longitude,atlantic2.latitude,atlantic2.where(sst >= -5).mean(dim="time"), cmap= "cool")
	plt.colorbar(label = 'Temperature')
	plt.title("Ocean Temperatures of the Atlantic Ocean")
	plt.xlabel('longitude')
	plt.ylabel('latitude')
	plt.savefig("Atlantic Ocean SST", dpi =300)
	plt.show()
	
	

	#mean = data.sst.mean("time")
	#print(mean.dims)
#plotting:
	#plt.figure()
	#plt.contourf(mean["longitude"],mean["latitude"],mean)
	#plt.show()
	