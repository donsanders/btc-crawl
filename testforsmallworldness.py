#Python code to search for a Watts Strogatz 1998 small-world in bitcoin network space scans
#Test that the uSPL of the largest connected component found in btc network space is < log of its node count

import networkx as nx
import json
import math
import datetime

# Make sure that the graph constructed is a digraph
# with no loops or parallel edges
# Can take awhile so as a side effect print summary info to console when completed
def ensureDiGraph(G, filename):
    G.remove_edges_from(G.selfloop_edges()) # Remove loops
    G = nx.DiGraph(G) # Remove parallel edges
    print datetime.datetime.now() , "Reading scan" , filename , "of btc network space." ,
    print "Cumulative totals: nodes" , len(G) , "edges" ,  len(G.edges)
    return G

# Read in a json file containing a json array of objects
# each object defines the ip address of the node and an array of peer ip addresses
def addNodesFromFile(G, filename):
    js_graph = json.load(open(filename))
    for node in js_graph:
        for edge in node['peers']:
            G.add_edge(node['address'],edge)
    G = ensureDiGraph(G, filename)

# Create graph space (forest) enclosing connected components
def btcGraphSpace(a, b):
    G = nx.DiGraph()
    for i in range(a, b, 1):
        filename =  "./scans/Satoshi-0-16-3-cleaned-" + str(i) + ".json"
        addNodesFromFile(G, filename)
    return G

# Analyze graph to determine if it is a small-world
def analyze(G):
    largest = max(nx.strongly_connected_component_subgraphs(G), key=len)
    #TODO some kind of check to ensure the lscc is much larger than others
    print("Node count of largest strongly connected component") , len(largest)
    print("Node count of first 10 strongly connected components") ,
    print [len(c) for c in sorted(nx.strongly_connected_components(G), key=len, reverse=True)[0:10]]
    H = largest
    uSPL = nx.average_shortest_path_length(H)
    logNodeCount = math.log(len(H)) # natural logarithm
    print("H = largest strongly connected sub component")
    print "H average clustering coefficient" , nx.average_clustering(nx.Graph(H))
    print "H nodes" , len(H) , "H.edges" , len(H.edges) , "ln(nodes)" ,
    print("%.2f" % logNodeCount)
    print "H average shortest path length" , uSPL
    print "Small-world found:"
    if uSPL < logNodeCount:
        print "YES"
    else:
        print "NO"

# Load and analyze scan data
G = btcGraphSpace(1, 100)
analyze(G)
