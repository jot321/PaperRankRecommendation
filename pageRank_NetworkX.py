import networkx as nx
import numpy as np
import csv
import operator


def creategraph(file_obj):
	
	reader = csv.reader(file_obj, delimiter = ",")
	G = nx.Graph()
	uniqueIds = []

	for row in reader:

		uniqueIds.append(row[0].strip())
		uniqueIds.append(row[1].strip())

		G.add_node(row[0].strip())
		G.add_node(row[1].strip())

		G.add_edge(row[0].strip(), row[1].strip())

	uniqueIds = set(uniqueIds)	
	
	return G, uniqueIds	

def calculatePersonalizationMatrix(nodes):

	cititedPapers = ["C08-3004", "D09-1141", "D12-1027"]
	d = {}

	for paper in nodes:

		if(paper in cititedPapers):
			d[paper] = 0.3
		else:
			d[paper] = 0

	return d

def calculatePageRank(G,d):

	pr= nx.pagerank(G, alpha = 0.85, personalization=d)

	for i in range(10):
		print sorted(pr.iteritems(), key=operator.itemgetter(1))[len(d) -i -1]


f = open("acl.txt","r")
nodes = []
d = {}
G = nx.Graph()

G, nodes = creategraph(f)	
d = calculatePersonalizationMatrix(nodes)

print len(d)

calculatePageRank(G,d)

