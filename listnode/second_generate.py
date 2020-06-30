import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

xlsx_data = pd.read_excel("./nodelist-Fig5.xlsx", error_bad_lines=False)
xlsx_data = np.array(xlsx_data)

print(xlsx_data)
node_list_1 = []
resource_list = []
value_list = []
re_list = []

for i in range(1, len(xlsx_data) + 1):
    for j in range(1, len(xlsx_data) + 1):
        re_list.append((str(i), str(j)))

for i in range(0, len(xlsx_data)):
    a = '%.2f' % xlsx_data[i][1]
    node_list_1.append(str(int(xlsx_data[i][0])) + '\n(' + str(a) + ')')
    resource_list.append(str(int(xlsx_data[i][0])))
    value_list.append(a)

print(node_list_1)
print(resource_list)
print(value_list)

csv_data = pd.read_excel("./nodelist-Fig5.xlsx", error_bad_lines=False, sheet_name=1)
csv_data = csv_data.fillna(0)
csv_data = np.array(csv_data)
print(csv_data)

T_lsit = []
relation_list = []

for i in range(1, len(csv_data)):
    T_lsit.append(csv_data[i][0])

for i in range(1, len(csv_data)):
    for j in range(1, len(csv_data[0])):
        if csv_data[i][j] != 0:
            relation_list.append((str(csv_data[i][0]), node_list_1[j - 1]))

print(T_lsit)
print(relation_list)

c= {}
d = 0
for i in range(1, len(T_lsit)+1):
    d = 0
    for j in range(1, len(resource_list)+1):
        d = d + float(csv_data[i][j])/len(resource_list)/5
    c.update({T_lsit[i - 1]: d})

print("--------------------------------")
c = sorted(c.items(), key=lambda x: x[1], reverse=True)
for i in range(0, len(c)):
    print(c[i])
print("--------------------------------")


'resource度中心度'
a = {}
b = 0
for i in range(1, len(resource_list)+1):
    b = 0
    for j in range(1, len(T_lsit)+1):
        b = b + float(csv_data[j][i])/len(T_lsit)/5
    a.update({resource_list[i - 1]: b})
print("--------------------------------")
a = sorted(a.items(), key=lambda x: x[1], reverse=True)
for i in range(0, len(a)):
    print(a[i])
print("--------------------------------")

degree_a = a

'''tourist node color'''
color_of_nodes_2 = []
for i in range(0, len(T_lsit)):
    color_of_nodes_2.append('#51FF00')
print(color_of_nodes_2)
print(len(color_of_nodes_2))

'''node shape'''
shape_of_nodes = []
for i in range(0, len(xlsx_data)):
    shape_of_nodes.append("s")
for i in range(0, len(T_lsit)):
    shape_of_nodes.append("s")
print(shape_of_nodes)
print(len(shape_of_nodes))

G = nx.DiGraph()
G.add_nodes_from(T_lsit)
G.add_nodes_from(node_list_1)
G.add_edges_from(relation_list)
'''resource node color'''
color_of_nodes_1 = []
node_size_list1 = []
for i in range(0, len(xlsx_data)):
    a = G.degree[node_list_1[i]]
    if xlsx_data[i][1] > 3.63 and a >= 8:
        color_of_nodes_1.append('#FF8000')
        node_size_list1.append(2500)
    else:
        color_of_nodes_1.append('#85DAE9')
        node_size_list1.append(2500)

pos = nx.spring_layout(G, k=1.6)
nx.draw_networkx_nodes(G, pos, font_weight='bold', alpha=0.5, node_shape="o", linewidths=5, width=1, nodelist=node_list_1, node_color=color_of_nodes_1, node_size=node_size_list1)
nx.draw_networkx_nodes(G, pos,
                       font_weight='bold', alpha=0.5, node_shape="s", linewidths=5, width=1, nodelist=T_lsit, node_color=color_of_nodes_2, node_size=900)
nx.draw_networkx_edges(G, pos, edgelist=relation_list, alpha=0.8, edge_color='#4CD0A0', width=0.5)
nx.draw_networkx_labels(G, pos, font_color="b")
print(G)
plt.show(G)

import methods
centrality_degree = sorted(methods.centrality_method.degree_centrality(G, node_list_1).items(), key=lambda x: x[1],
                reverse=True)


test1 = set(G)
test2 = G.degree(node_list_1)
print(test1)
for i in test2:
    print(i)

'''
nx.draw_kamada_kawai(G, with_labels=True, font_weight='bold', width=1, node_color=color_of_nodes_1, node_shape='o',
                     node_size=3000, alpha=0.9)
'''
'''
for i in centrality_degree:
    print(i)

for i in range(0, len(node_list_1)):
    a = G.degree((node_list_1[i]))
    if a >= 11:
        color_of_nodes_1[i] = '#F39C12'
pos = nx.random_layout

nx.draw_networkx_nodes(G, pos, font_weight='bold', alpha=0.8, node_shape="o", width=1, node_list=node_list_1, node_color=color_of_nodes_1, node_size=3000)
nx.draw_networkx_nodes(G, pos, font_weight='bold', alpha=0.8, node_shape="o", width=1, node_list=T_lsit, node_color=color_of_nodes_2, node_size=3000)
nx.draw_networkx_edges(G, pos, alpha=0.8)
plt.axis('off')
plt.show(G)

codes for the first graph

'''