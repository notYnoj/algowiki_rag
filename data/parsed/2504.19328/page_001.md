# Scalable Substructure Discovery Algorithm For Homogeneous Multilayer Networks

Arshdeep Singh, Abhishek Santra and Sharma Chakravarthy <br>
IT Lab and CSE Department, University of Texas at Arlington <br>
axs9120@mavs.uta.edu, abhishek.santra@mavs.uta.edu, sharmac@cse.uta.edu

**Abstract--Graph mining analyzes real-world graphs to find core substructures (connected subgraphs) in applications modeled as graphs. Substructure discovery is a process that involves identifying meaningful patterns, structures, or components within a large data set. These substructures can be of various types, such as frequent patterns, motifs, or other relevant features within the data.**

To model complex data sets - with multiple types of entities and relationships - multilayer networks (or MLNs) have been shown to be more effective as compared to simple and attributed graphs. Analysis algorithms on MLNs using the decoupling approach have been shown to be both efficient and accurate. Hence, this paper focuses on substructure discovery in homogeneous multilayer networks (one type of MLN) using a novel decoupling-based approach. In this approach, each layer is processed independently, and then the results from two or more layers are composed to identify substructures in the entire MLN. The algorithm is designed and implemented, including the composition part, using one of the distributed processing frameworks (the Map/Reduce paradigm) to provide scalability.

After establishing the correctness, we analyze the speedup and response time of the proposed algorithm and approach through extensive experimental analysis on large synthetic and real-world data sets with diverse graph characteristics.

**_Index Terms_--Homogeneous Multilayer Networks, Substructure Discovery, Decoupling approach, Accuracy & Scalability**

## I. INTRODUCTION

Substructure discovery is an unsupervised approach to data mining to infer new knowledge and is typically applied to graph representations. Frequent patterns are a common concept in data mining that refers to item sets, subsequences, or substructures that occur frequently in a given data set, meeting or exceeding a user-defined threshold. By identifying frequent subgraphs, we can gain insights into the underlying structure of the data and identify recurring patterns or motifs.

Graph models have been used to analyze the World Wide Web’s structure [1], social-media data, bio-informatics data [2], atoms and covalent relationships in chemistry [3], etc. Graphs are better than other data representations that embed inherent relationships among objects or entities and are also easy to understand. They use vertices and edges where each vertex of the graph will correspond to an entity and each edge is a relationship between two entities. Applications can be modeled using several graph alternatives: (i) Simple graphs, (ii) Attributed graphs, and (iii) Multilayer networks.

**Need for Multilayer Networks:** Social networks and many other applications often include diverse types of nodes and relationships between them. Modeling or representing them as<tbc>

<tbc>simple graphs (also termed a network) by using only one type of node and relationship often leads to an oversimplification of reality and information loss. Attributed graphs are better, but lack algorithms for analysis.

Sociologists have long acknowledged the significance of using distinct types of connectivity among the same group of individuals [4]. Therefore, such systems are better studied through multilayer networks.

Multilayer networks are a more general framework that allows for the analysis of complex systems with multiple interacting units and inter-dependencies that are not properly captured by simple graphs. In a multilayer network, each layer represents a different type of interaction or relationship between the system’s constituents. For example, in a social network, one layer may represent friendships between individuals, while another layer may represent professional LinkedIn connections. By analyzing the interactions between layers, it is possible to gain insights into the emergent behavior of the system as a whole.

Multilayer networks can be of several types, including (i) homogeneous (HoMLNs, Figure 1(a)), (ii) heterogeneous (HeMLNs, Figure 1(b)), and (iii) hybrid (HyMLNs, Figure 1(c)), depending on the type of layers and connections between them. Figure 1 shows these types of multilayer networks. Since the focus of this paper is HoMLNs, we start with a formal definition of a MLN.

**_Definition 1_**: A multilayer network MLN(_G,X_), is defined by two sets of graphs. The set _G_={_G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>n</sub>_} contains **simple** graphs (one for each layer), where _G<sub>i</sub>(V<sub>i</sub>,E<sub>i</sub>_) is defined by a set of vertices _V<sub>i</sub>_ and a set of edges _E<sub>i</sub>_. An edge \(e(v,u)\in E_i\), connects vertices _v_ and _u_, where \(v,u\in V_i\). The set _X_={_X_<sub>1,2</sub>_,X_<sub>1,3</sub>_,...,X_<sub>_m_-1_,m_</sub>} consists of **bipartite**<tbc>

