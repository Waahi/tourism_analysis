import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

csv_data = pd.read_csv("C:/Users/shaot/Desktop/list1.csv", error_bad_lines = False)
csv_data = np.array(csv_data)

print(type(csv_data))
print(csv_data)

node_list = []
value_list = []
print(len(csv_data))
csv_data = csv_data.astype(np.str)
for i in range(0, len(csv_data)):
    node_list.append(str(csv_data[i][0]))
    value_list.append(str(csv_data[i][1]))
print(node_list)
print(value_list)

G = nx.Graph()
G.add_nodes_from(node_list)
print(G)
plt.show(G)
