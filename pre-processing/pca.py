from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


dataRaw = []
df = pd.read_csv('../data/standardised_data_460.csv')
data = df.to_numpy()
data = data[1:, 1:] #getting rid of column and row labels

standardisedData = data[:,0:332] #including all subgroup data, not including response, lab or pass

#n_components was changed to find how much variance is explained by the PCA
#n=77 gives 95%, n=59 gives 90% and n=47 gives 85%
pca = PCA(n_components=77) 
pca.fit(standardisedData)
Coeff = pca.components_

#prints the total ratio of explained variance 
print(sum(pca.explained_variance_ratio_))