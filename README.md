# Tabular Playground Series Assignment

Authors:
- Łukasz Andryszewski
- Eryk Walter

This a [repository](https://github.com/ErykWalter/tabular-playground-series) in which my friend Łukasz and I tries solve a [Tabular Playground Series](https://www.kaggle.com/competitions/tabular-playground-series-jul-2022/overview) kaggle challenge.

The dataset is composed of 29 different features, both numerical and categorical.
Before performing clustering some normalization was performed.

## Normalization and selection

A test for low variance features was performed, however nothing was filtered out.
Next a test for features correlation was done, but it was also futile as the correlation between the features was very low:

![correlation](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/a5288b0d-b980-418e-8836-20f4443c4583)

We wanted to performed UMAP on the dataset as it preserves local distances. For that the data was standardized.

![umap](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/8e82ec53-78cc-45fe-8784-83b70184ef64)

For DBSCAN however the dataset was normalized, to make looking for epsilon easier.

## K-means

K-means was the first clustering method to be tested. To perform it we need to find the cluster count. The metric used was euclidean.

### Number of clusters:

The quality of clustering can be evaluated using Silhouette score and also Davies-Bouldin score. The first one is maximized and the second one is minimized.

Silhouette score:

![silhouette](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/5d1d5f0d-3840-4aca-9265-8f40c78c2ae5)

Davies-Bouldin score:

![davies-bouldin](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/5bdd26e1-187c-4cee-b210-311f3027afa4)

Some notable k-sizes are 3, 4 and 8, but we propose 4 as the best k.

## DBSCAN

DBSCAN was tested next. It is a density based clustering, with two parameters: $\epsilon$ and $min_{sample}$. The $\epsilon$ describes the radius of a points neighbourhood. In turn $min_{sample}$ defines the minimum number of other points in this neighbourhood.

First optimal range for $\epsilon$ was checked using NearestNeighbours algorithm for the normalized data:

![elbow](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/0efb02f2-38af-4b34-8a47-fe4fde2dd05c)

Here we are interested in the second elbow, concluding that the optimal $\epsilon$ is somewhere between 0.47 up to 0.6. We checked the optimal value similarly to the k for k-means, concluding at 0.6.

Then the optimal $min_{sample}$ was concluded to be 140.

Unfortunately DBSCAN does not seem to be a good method for this dataset:

![dbscan](https://github.com/ErykWalter/tabular-playground-series/assets/107052397/5edba5c6-c071-4f61-a4ce-e6ce815f0d00)


