import pandas as pd
import numpy as np

from sklearn import datasets, preprocessing, feature_selection
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN