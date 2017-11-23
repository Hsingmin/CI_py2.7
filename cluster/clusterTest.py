
# clusterTest.py

import cluster

blognames, words, data = cluster.readfile('blogdata.txt')
clust = cluster.hcluster(data)

cluster.printclust(clust, labels = blognames)























