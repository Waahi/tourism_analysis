import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

xlsx_data = pd.read_excel("./list_1.xlsx", error_bad_lines=False)
xlsx_data = np.array(xlsx_data)

print(xlsx_data)
node_list = []
resource_list = []
value_list = []
re_list = []

for i in range(1, len(xlsx_data) + 1):
    for j in range(1, len(xlsx_data) + 1):
        re_list.append((str(i), str(j)))

for i in range(0, len(xlsx_data)):
    a = '%.2f' % xlsx_data[i][1]
    node_list.append(str(int(xlsx_data[i][0])) + '\n(' + str(a) + ')')
    resource_list.append(str(int(xlsx_data[i][0])))
    value_list.append(a)

print(node_list)
print(resource_list)
print(value_list)

G = nx.Graph()
G.add_nodes_from(node_list)
'''G.add_edges_from(re_list)'''
'''size_of_node= value_list'''

pos = nx.spiral_layout(G, scale=1, center=None, dim=2, resolution=1, equidistant=True)
nx.draw(G, pos = pos, with_labels=True, font_weight='bold', width=0, node_color='#A0CBE2', node_size=5000, alpha=0.7)
plt.show(G)
G.clear()

'''codes for the first graph'''