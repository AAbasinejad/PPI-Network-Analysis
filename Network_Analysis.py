#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Interactions
import pandas as pd
import networkx as nx
import random as rd
import markov_clustering as mc
import community
import matplotlib.pyplot as plt
import os



def adjacency_matrix(SG, biogrid, iid):
    sgi, union_ = Interactions._integrations(SG, biogrid, iid)
    intersections = Interactions.intersection_interactions(SG, biogrid, iid)
    
    # making adjacency matrix of union_integrated dataset
    union_adjacency = pd.crosstab(union_['interactor A'], union_['interactor B'])
    idx = union_adjacency.columns.union(union_adjacency.index)
    union_adjacency = union_adjacency.reindex(index = idx, columns=idx, fill_value=0)
    
    # making adjacency matrix of sgi_integrated dataset
    sgi_adjacency = pd.crosstab(sgi['interactor A'], sgi['interactor B'])
    idx = sgi_adjacency.columns.union(sgi_adjacency.index)
    sgi_adjacency = sgi_adjacency.reindex(index = idx, columns=idx, fill_value=0)
    
    # making adjacency matrix of intersections dataset
    I_adjacency = pd.crosstab(intersections['interactor A'], intersections['interactor B'])
    idx = I_adjacency.columns.union(I_adjacency.index)
    I_adjacency = I_adjacency.reindex(index = idx, columns=idx, fill_value=0)
    
    return union_adjacency, sgi_adjacency, I_adjacency

def create_graph(union_adjacency, sgi_adjacency, I_adjacency):
    
    # making complete graph of union data_set
    G_union = nx.from_pandas_adjacency(union_adjacency)
    G_union.name = 'Union_Interactions Graph'
    
    # making complete graph of sgi data_set
    G_sgi = nx.from_pandas_adjacency(sgi_adjacency)
    G_sgi.name = 'SGI Graph'
    
    # making complete graph of intersection data_set
    G_I = nx.from_pandas_adjacency(I_adjacency)
    G_I.name = 'Intersection interactions Graph'
    
    return G_union, G_sgi, G_I

def large_connected_component():
    
    
    
    
def network_measures():
    
def save_results():
    
    f = open('Network_Analysis_results.txt', 'w')
    
    ### Results of G_Union
    f.write('Union_complete_graph details....\n')
    f.write(nx.info(G_union))
    f.write('No. of connected component: '+ str(nx.number_connected_components(G_union))+ '\n')
    f.write('No. of isolated Nodes: '+ str(len(nx.isolates(G_union)))+ '\n')
    f.write('Average_path_length: '+ str(nx.average_shortest_path_length(G_union))+ '\n')
    
    # The average degree connectivity is the average nearest neighbor degree of nodes with degree k. 
    avg_deg_union = nx.average_degree_connectivity(G_union)
    avg_deg_union_res = open('average_degree_union.txt', 'w')
    avg_deg_union_res.write('\t'.join(['#degree k','average connectivity'])+ '\n')
    for k, v in avg_deg_union.items():
        avg_deg_union_res.write('\t'.join(map(str,([k,v])))+ '\n')
    avg_deg_union_res.close()
    
    f.write('Average clustering coefficient: '+ str(nx.average_clustering(G_union))+ '\n')
    # The diameter is the maximum eccentricity.
    f.write('Network diameter: ' + str(nx.diameter(G_union))+ '\n')
    # The radius is the minimum eccentricity.
    f.write('Network radius: ' + str(nx.radius(G_union)) + '\n')
    
    
    ### Results of G_sgi
    f.write('SGI_complete_graph details....\n')
    f.write(nx.info(G_sgi))
    f.write('No. of connected component: '+ str(nx.number_connected_components(G_sgi))+ '\n')
    f.write('No. of isolated Nodes: '+ str(len(nx.isolates(G_sgi)))+ '\n')
    f.write('Average_path_length: '+ str(nx.average_shortest_path_length(G_sgi))+ '\n')
    
    # The average degree connectivity is the average nearest neighbor degree of nodes with degree k. 
    avg_deg_sgi = nx.average_degree_connectivity(G_sgi)
    avg_deg_sgi_res = open('average_degree_union.txt', 'w')
    avg_deg_sgi_res.write('\t'.join(['#degree k','average connectivity'])+ '\n')
    for k, v in avg_deg_sgi.items():
        avg_deg_sgi_res.write('\t'.join(map(str,([k,v])))+ '\n')
    avg_deg_sgi_res.close()
    
    f.write('Average clustering coefficient: '+ str(nx.average_clustering(G_sgi))+ '\n')
    # The diameter is the maximum eccentricity.
    f.write('Network diameter: ' + str(nx.diameter(G_sgi))+ '\n')
    # The radius is the minimum eccentricity.
    f.write('Network radius: ' + str(nx.radius(G_sgi)) + '\n')
    
    ### Results of G_I
    f.write('Intersections_complete_graph details....\n')
    f.write(nx.info(G_I))
    f.write('No. of connected component: '+ str(nx.number_connected_components(G_I))+ '\n')
    f.write('No. of isolated Nodes: '+ str(len(nx.isolates(G_I)))+ '\n')
    f.write('Average_path_length: '+ str(nx.average_shortest_path_length(G_I))+ '\n')
    
    # The average degree connectivity is the average nearest neighbor degree of nodes with degree k. 
    avg_deg_I = nx.average_degree_connectivity(G_I)
    avg_deg_I_res = open('average_degree_union.txt', 'w')
    avg_deg_I_res.write('\t'.join(['#degree k','average connectivity'])+ '\n')
    for k, v in avg_deg_I.items():
        avg_deg_I_res.write('\t'.join(map(str,([k,v])))+ '\n')
    avg_deg_I_res.close()
    
    f.write('Average clustering coefficient: '+ str(nx.average_clustering(G_I))+ '\n')
    # The diameter is the maximum eccentricity.
    f.write('Network diameter: ' + str(nx.diameter(G_I))+ '\n')
    # The radius is the minimum eccentricity.
    f.write('Network radius: ' + str(nx.radius(G_I)) + '\n')
    
    f.close()
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    