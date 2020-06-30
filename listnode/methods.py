import networkx as nx
from math import sqrt


class centrality_method:

    def degree_centrality(G, nodes):
        '''compute degree centrality'''
        top = set(nodes)
        bottom = set(G) - top
        s = 1.0 / len(bottom)
        centrality = {n: d * s for n, d in G.degree(top)}
        s = 1.0 / len(top)
        centrality.update({n: d * s for n, d in G.degree(bottom)})
        sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        '''It seems sorted function cannot work here and other three places below'''
        return centrality

    def betweenness_centrality(G, nodes):
        '''compute betweenness_centrality'''
        top = set(nodes)
        bottom = set(G) - top
        n = float(len(top))
        m = float(len(bottom))
        s = (n - 1) // m
        t = (n - 1) % m
        bet_max_top = (((m ** 2) * ((s + 1) ** 2)) +
                       (m * (s + 1) * (2 * t - s - 1)) -
                       (t * ((2 * s) - t + 3))) / 2.0
        p = (m - 1) // n
        r = (m - 1) % n
        bet_max_bot = (((n ** 2) * ((p + 1) ** 2)) +
                       (n * (p + 1) * (2 * r - p - 1)) -
                       (r * ((2 * p) - r + 3))) / 2.0
        betweenness = nx.betweenness_centrality(G, normalized=False, weight=None)
        for node in top:
            betweenness[node] /= bet_max_top
        for node in bottom:
            betweenness[node] /= bet_max_bot
        sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
        return betweenness

    def closeness_centrality(G, nodes, normalized=True):
        '''compute closeness_centrality'''
        closeness = {}
        path_length = nx.single_source_shortest_path_length
        top = set(nodes)
        bottom = set(G) - top
        n = float(len(top))
        m = float(len(bottom))
        for node in top:
            sp = dict(path_length(G, node))
            totsp = sum(sp.values())
            if totsp > 0.0 and len(G) > 1:
                closeness[node] = (m + 2 * (n - 1)) / totsp
                if normalized:
                    s = (len(sp) - 1.0) / (len(G) - 1)
                    closeness[node] *= s
            else:
                closeness[n] = 0.0
        for node in bottom:
            sp = dict(path_length(G, node))
            totsp = sum(sp.values())
            if totsp > 0.0 and len(G) > 1:
                closeness[node] = (n + 2 * (m - 1)) / totsp
                if normalized:
                    s = (len(sp) - 1.0) / (len(G) - 1)
                    closeness[node] *= s
            else:
                closeness[n] = 0.0
        sorted(closeness.items(), key=lambda x: x[1], reverse=True)
        return closeness

    def eigenvector_centrality(G, max_iter=100, tol=1.0e-6, nstart=None, weight=None):
        '''compute eigenvector_centrality'''

        if len(G) == 0:
            raise nx.NetworkXPointlessConcept('cannot compute centrality for the'
                                              ' null graph')
        # If no initial vector is provided, start with the all-ones vector.
        if nstart is None:
            nstart = {v: 1 for v in G}
        if all(v == 0 for v in nstart.values()):
            raise nx.NetworkXError('initial vector cannot have all zero values')
        # Normalize the initial vector so that each entry is in [0, 1]. This is
        # guaranteed to never have a divide-by-zero error by the previous line.
        nstart_sum = sum(nstart.values())
        x = {k: v / nstart_sum for k, v in nstart.items()}
        nnodes = G.number_of_nodes()
        # make up to max_iter iterations
        for i in range(max_iter):
            xlast = x
            x = xlast.copy()  # Start with xlast times I to iterate with (A+I)
            # do the multiplication y^T = x^T A (left eigenvector)
            for n in x:
                for nbr in G[n]:
                    w = G[n][nbr].get(weight, 1) if weight else 1
                    x[nbr] += xlast[n] * w
            # Normalize the vector. The normalization denominator `norm`
            # should never be zero by the Perron--Frobenius
            # theorem. However, in case it is due to numerical error, we
            # assume the norm to be one instead.
            norm = sqrt(sum(z ** 2 for z in x.values())) or 1
            x = {k: v / norm for k, v in x.items()}
            # Check for convergence (in the L_1 norm).
            if sum(abs(x[n] - xlast[n]) for n in x) < nnodes * tol:
                return x
        raise nx.PowerIterationFailedConvergence(max_iter)

    def nomalization(Ties_number):
        '''nomalization for sorted list'''
        Normalized_T = []
        list_min = Ties_number[-1][1]
        list_max = Ties_number[1][1]
        for i in Ties_number:
            Normalized_T.append((i[0], (i[1] - list_min) / (list_max - list_min)))
        return Normalized_T

    def average_of_centrality(all_list, list_C):
        '''method for computing average of centrality,
        all_list means all nodes list,
        list_C means all a list with all results of centrality'''
        all_reslut = dict()
        for i in all_list:
            all_reslut[i] = 0
        for i in list_C:
            for j in all_list:
                for k in range(len(i)):
                    if i[k][0] == j:
                        all_reslut[j] += i[k][1]
                        if all_reslut[j] > i[k][1]:
                            all_reslut[j] = all_reslut[j] / 2
        all_reslut = sorted(all_reslut.items(), key=lambda x: x[1], reverse=True)
        return all_reslut


class method_of_Ties:

    def Num_of_Ties(people_list, date_list, relation_list, all_list):
        '''count every node's joint node in graph'''
        G = method_of_generate_graph.generate_graph(people_list, date_list, relation_list)
        A = dict()
        for i in all_list:
            A[i] = len(G.adj[i])
        sorted(A.items(), key=lambda x: x[1], reverse=True)
        return A


class method_of_generate_graph:

    def generate_graph(people_list, date_list, relation_list):
        """generate graph"""
        import matplotlib.pyplot as plt
        G = nx.Graph()
        G.add_nodes_from(people_list)
        G.add_nodes_from(date_list)
        G.add_edges_from(relation_list)
        return G

    def show_graph(G):
        '''show graph'''
        import matplotlib.pyplot as plt
        nx.draw(G, with_labels=True, font_weight='bold', width=1.0)
        plt.show()


class Data_process:
    def generate_row_list(csv_data):
        row_list = []
        for i in range(1, len(csv_data[0])):
            row_list.append(csv_data[0][i])
        return row_list

    def generate_col_list(csv_data):
        col_list = []
        for i in range(1, len(csv_data)):
            col_list.append((csv_data[i][0]))
        return col_list

    def generate_relation_lsit(csv_data):
        relation_list = []
        for i in range(1, len(csv_data)):
            for j in range(1, len(csv_data[0])):
                if csv_data[i][j] != '0':
                    relation_list.append((csv_data[i][0], csv_data[0][j]))
        return relation_list
