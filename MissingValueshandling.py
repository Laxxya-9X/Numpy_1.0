import numpy as np

arr = np.array([1,2,np.nan,5,np.nan,np.nan])

print(np.isnan(arr))

print(np.isnan(arr).sum())  #total null values

#replace null values with mean

mean = np.nanmean(arr)

clean = np.where(np.isnan(arr),mean,arr)

print(clean)