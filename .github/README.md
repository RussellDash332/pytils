# pytils
> Not to be confused with the [`pytils`](https://pypi.org/project/pytils/) library for Russian-specific string utilities.

My collection of **Py**thon u**til**ity code**s** primarily designed for solving Kattis and Advent of Code (AoC) problems. It is intended to be as fast as possible, if not as short as possible. Feel free to use and customize them for your own use as you see fit.

## Treasure List

Classification taken from [`cp-algorithms`](https://cp-algorithms.com/).

### Algebra and Number Theory
#### Prime Numbers
- [`number_theory_prime_sieve`](../number_theory_prime_sieve.py)

    The classic Eratosthenes prime sieve that runs in $O(n\log\log n)$ time. Makes use of an array that stores the smallest prime factor.

    Kattis problems to try on: ...

- [`number_theory_prime_factorization`](../number_theory_prime_factorization.py)

    Applications of the prime sieve:
    - prime factorization of $n$
    - number of divisors of $n$
    - Euler's totient function, $\phi(n)$.

    Kattis problems to try on: ...

- [`number_theory_miller_rabin`](../number_theory_miller_rabin.py)

    Checks if a number $n$ is probable prime. Works well in tandem with Pollard-Rho for integer factorization.

    Kattis problems to try on: ...

- [`number_theory_pollard_rho`](../number_theory_pollard_rho.py)

    Finds a trivial factor of an integer $n$. Also includes Brent modification for faster version. Expected to run in $O(n^\frac{1}{4})$ time.

    Kattis problems to try on: ...

- [`number_theory_prime_counting`](../number_theory_prime_counting.py)

    Counts the number of prime numbers up to $n$ in $O(\sqrt{n})$ time. Also includes Meissel-Lehmer algorithm that runs in $O(n^\frac{2}{3})$ time.

    Kattis problems to try on: ...

#### Modular Arithmetic
- [`number_theory_gcd_lcm`](../number_theory_gcd_lcm.py)

    Basic GCD and LCM.

    Kattis problems to try on: ...

- [`number_theory_chinese_remainder`](../number_theory_chinese_remainder.py)

    Classic Chinese Remainder Theorem.

    Kattis problems to try on: ...

- [`number_theory_lucas_theorem`](../number_theory_lucas_theorem.py)

    Lucas' theorem, mainly used to compute a large binomial coefficient modulo some integer.

    Kattis problems to try on: ...

#### Miscellaneous
- [`fast_fourier_transform`](../fast_fourier_transform.py)

    Fast Fourier Transform (FFT) used mainly for multiplying two polynomials, runs in $O(n\log n)$ time, where $n$ is the polynomial degree.

    Kattis problems to try on: ...

- [`number_theory_mobius_function`](../number_theory_mobius_function.py)

    Computes the Möbius function and stores them in an array, runs in $O(n\log\log n)$ time.

    Kattis problems to try on: ...

- [`number_theory_tonelli_shanks_cornacchia`](../number_theory_tonelli_shanks_cornacchia.py)

    Solves $r^2 \equiv n \pmod p$ given an integer $n$ and prime number $p$, then uses the solution $r$ to solve $x^2 + dy^2 = p$.

    Kattis problems to try on: ...

### Data Structures
#### Lists
- [`circular_linked_list`](../circular_linked_list.py)

    Simple implementation of circular linked list.

    Kattis problems to try on: ...

- [`sliding_window`](../sliding_window.py)

    Four variants of sliding windows mentioned in CP Book (all run in $O(n)$ time)
    - smallest subarray size whose sum is `>= K`
    - smallest subarray size where all numbers in range `[1..K]` are within
    - `max(sum(A[i:i+K]) for i in range(len(A)-K+1))`
    - `[min(A[i:i+K]) for i in range(len(A)-K+1)]`

    Kattis problems to try on: ...

- [`next_greater_element`](../next_greater_element.py)

    Computes the next greater element for each element in an array. Runs in $O(n)$ time.

    Kattis problems to try on: ...

#### Trees
- [`avl_tree`](../avl_tree.py)

    AVL tree implementation, including the self-rebalancing part. All queries are done in $O(\log n)$ time, except inorder traversal that takes $O(n)$ time.

    Kattis problems to try on: ...

- [`fenwick_tree_rsq`](../fenwick_tree_rsq.py)

    Classic Fenwick tree to answer range sum queries (RSQ). Both PURQ (point update, range query) and RURQ (range update, range query) versions are available. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`fenwick_tree_rmq`](../fenwick_tree_rmq.py)

    Binary-indexed tree but to answer range minimum/maximum queries (RMQ). Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`segment_tree_general`](../segment_tree_general.py)

    General recursive implementation of segment tree, which can be customized to handle different aggregate functions. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`segment_tree_dynamic`](../segment_tree_dynamic.py)

    Recursive implementation of the dynamic segment tree, which is currently optimized only for summation as aggregate. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`treap`](../treap.py)

    Quick implementation of a treap data structure.

    Kattis problems to try on: N/A

- [`wavelet_tree`](../wavelet_tree.py)

    Incomplete implementation of the wavelet tree.

    Kattis problems to try on: N/A

#### Miscellaneous
- [`sqrt_decomposition`](../sqrt_decomposition.py)

    Sqrt-based data structure to support updates and sum queries in $O(\sqrt{n})$ time.

    Kattis problems to try on: ...

- [`ufds`](../ufds.py)

    Classic union-find disjoint set (UFDS), also known as disjoint set union (DSU). Equipped with rank heuristics and path-compression, making both merging/union and querying run in $O(\alpha(n))$ time.

    Kattis problems to try on: ...

### Dynamic Programming
#### Knapsack
- [`knapsack`](../knapsack.py)

    0-1 Knapsack with given capacity and list of weights and values. Runs in $O(nW)$ time where $n$ is the number of items and $W$ is the maximum capacity.

    Kattis problems to try on: ...

#### Convex Hull Trick
- [`convex_hull_trick`](../convex_hull_trick.py)

    Convex hull optimization to optimize a specific $O(n^2)$ DP problem into an $O(n\log n)$ one. Here, we assume that the queries and slopes are sorted, thus reducing the problem into a sliding window after sorting.

    Kattis problems to try on: ...

- [`dynamic_convex_hull_trick_line_container`](../dynamic_convex_hull_trick_line_container.py)

    Dynamic convex hull optimization, also known as the line container, solves a more general problem where lines and queries are not necessarily given in sorted order. Due to list insertion and deletion being $O(n)$, each operation should run in $O(n)$ time instead of $O(\log n)$, but should still be fast enough in most cases.

    Kattis problems to try on: ...

#### Miscellaneous
- [`longest_increasing_subsequence`](../longest_increasing_subsequence.py)

    Finds the LIS length and outputs any of them. Another variant counts the number of distinct LIS in an array of $n$ numbers. Both functions run in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`travelling_salesman_problem_dp`](../travelling_salesman_problem_dp.py)

    Finds the TSP cost in a graph of $n$ vertices and prints the TSP tour when needed. Both run in $O(n^2 2^n)$ time.

    Kattis problems to try on: ...

### String Processing
#### Suffix Array
- [`suffix_array_lcp`](../suffix_array_lcp.py)

    Suffix array data structure alongside the longest common prefix (LCP) array for a string of length $n$. Suffix array construction runs in $O(n \log n)$ time.

    Kattis problems to try on: ...

#### String Matching
- [`string_matching_kmp`](../string_matching_kmp.py)

    The Knuth-Morris-Pratt (KMP) algorithm to find all matches of a string within the target string of length $n$. Runs in $O(n)$ time.

    Kattis problems to try on: ...

- [`string_multimatching_aho_corasick`](../string_multimatching_aho_corasick.py)

    The Aho-Corasick algorithm to find all matches of all query strings within the target string.

    Kattis problems to try on: ...

- [`string_multimatching_suffix_array`](../string_multimatching_suffix_array.py)

    Suffix array can also be used to find all matches of all query strings within the target string.

    Kattis problems to try on: ...

#### Miscellaneous
- [`manacher_subpalindromes`](../manacher_subpalindromes.py)

    Enumerates all palindromic substrings of a given string with length $n$ in $O(n)$ time.

    Kattis problems to try on: ...

- [`lexicographically_minimum_string_rotation_booth`](../lexicographically_minimum_string_rotation_booth.py)

    Booth's lexicographically minimum string rotation algorithm that runs in $O(n)$ time where $n$ is the length of the string.

    Kattis problems to try on: ...

- [`z_function`](../z_function.py)

    Computes the Z-function where `z = [lcp(s, s[i:]) for i in range(len(s))]`.

    Kattis problems to try on: ...

### Linear Algebra
- [`rref_gaussian_elimination`](../rref_gaussian_elimination.py)

    Converts a matrix $A$ into its reduced row-echelon form (RREF). Very useful for Gaussian elimination.

    Kattis problems to try on: ...

- [`simplex_linear_programming`](../simplex_linear_programming.py)

    Simplex algorithm for linear programming, supports both maximization and minimization.

    Kattis problems to try on: ...

### Numerical Methods
- [`binary_search`](../binary_search.py)

    Binary search for both lower bound and upper bound. Function has to be monotonic. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    Kattis problems to try on: ...

- [`ternary_search`](../ternary_search.py)

    Ternary search on both integer cases and double/float cases. Finds the minimum of a decreasing-then-increasing function. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    Kattis problems to try on: ...

### Geometry
#### 2D
- [`compgeo_2d_polygon_area_centroid`](../compgeo_2d_polygon_area_centroid.py)

    Area and centroid of a 2D-polygon consisting of $n$ vertices. Runs in $O(n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_point_in_polygon`](../compgeo_2d_point_in_polygon.py)

    Checks if a point is within a polygon using two different approaches: angle calculation and ray intersection.

    Kattis problems to try on: ...

- [`compgeo_2d_intersect`](../compgeo_2d_intersect.py)

    Line segment intersection.

    Kattis problems to try on: ...

- [`compgeo_2d_closest_pair`](../compgeo_2d_closest_pair.py)

    Closest pair problem. Given $n$ 2D-coordinates, find the closest pair among all $O(n^2)$ possible pairs. Runs in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_convex_hull`](../compgeo_2d_convex_hull.py)

    Given $n$ 2D-coordinates, compute its convex hull (smallest polygon that contains all points). Runs in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_half_plane`](../compgeo_2d_half_plane.py)

    Half-plane intersection. Given $n$ half-planes in 2D, find the polygon that is contained within all the half-planes.

    Kattis problems to try on: ...

#### 3D
- [`compgeo_3d_projection_intersection`](../compgeo_3d_projection_intersection.py)

    Solves different simple queries in 3D coordinate system:
    - point-to-segment projection
    - point-to-plane projection
    - point-line distance
    - point-plane distance
    - line-plane intersection

    Kattis problems to try on: ...

- [`compgeo_3d_convex_hull`](../compgeo_3d_convex_hull.py)

    Given $n$ 3D-coordinates where no four points lie on the same plane, compute its convex hull (smallest polyhedron that contains all points). Runs in $O(n^2)$ time.

    Kattis problems to try on: ...

- [`compgeo_3d_minimum_enclosing_circle`](../compgeo_3d_minimum_enclosing_circle.py)

    Smallest circle/sphere (2D/3D) that covers all the given points. Outputs the center and the radius.

    Kattis problems to try on: ...

### Graph Algorithms
#### Graph Representation
- [`graph_adjacency_list`](../graph_adjacency_list.py)

    Basic implementation of an adjacency list as a list of lists/dictionaries.

    Kattis problems to try on: N/A

#### Graph Traversal
- [`traversal_bfs`](../traversal_bfs.py)

    Simple BFS implementation. Runs in $O(V+E)$ time.

    Kattis problems to try on: N/A

- [`traversal_dfs`](../traversal_dfs.py)

    Simple iterative DFS implementation using stacks (because recursion is slow in Python). Runs in $O(V+E)$ time.

    Kattis problems to try on: N/A

#### Connected Components & Graph Properties
- [`tarjan_bridges_cut_vertices`](../tarjan_bridges_cut_vertices.py)

    Tarjan's algorithm to find bridges and cut vertices. Runs in $O(V+E)$ time.

    Kattis problems to try on: ...

- [`topological_sorting`](../topological_sorting.py)

    Topological sorting using Kahn's algorithm or using the DFS approach. Runs in $O(V+E)$ time.

    Kattis problems to try on: ...

- [`scc_kosaraju`](../scc_kosaraju.py)

    Extension of DFS topological sorting, Kosaraju's algorithm, to enumerate the strongly connected components (SCC). Runs in $O(V+E)$ time.

    Kattis problems to try on: ...

#### Minimum Spanning Trees
- [`minimum_spanning_tree_prim`](../minimum_spanning_tree_prim.py)

    Prim's algorithm to compute the minimum spanning tree (MST) and its cost. Both sparse graph and dense graph variants are available. Former runs in $O(E\log V)$ time, but latter runs in $O(V^2)$.

    Kattis problems to try on: ...

- [`minimum_spanning_tree_kruskal`](../minimum_spanning_tree_kruskal.py)

    Kruskal's algorithm to compute the minimum spanning tree (MST) and its cost using UFDS. Runs in $O(E\log E)$ time.

    Kattis problems to try on: ...

#### Shortest Paths
- [`sssp_bellman_ford`](../sssp_bellman_ford.py)

    Single-source shortest path (SSSP) using Bellman-Ford's algorithm, which also includes negative cycle detection. Runs in $O(VE)$ time.

    Kattis problems to try on: ...

- [`sssp_dijkstra`](../sssp_dijkstra.py)

    Single-source shortest path (SSSP) using modified Dijkstra's algorithm. Runs in $O(E\log E)$ time.

    Kattis problems to try on: ...

- [`apsp_floyd_warshall`](../apsp_floyd_warshall.py)

    All-pairs shortest path (APSP) using Floyd-Warshall's algorithm. Runs in $O(V^3)$ time. Different variants are also available.
    - minimax/maximin (useful for min/maximum spanning trees)
    - transitive closure
    - +ve/-ve cycle detection
    - enumerate shortest path from anywhere to anywhere

    Kattis problems to try on: ...

#### Lowest Common Ancestor
- [`tarjan_offline_lca`](../tarjan_offline_lca.py)

    Tarjan's algorithm to compute the LCA of some query pair of vertices on a tree rooted at vertex $0$. Runs in $O(V+Q)$ time.

    Kattis problems to try on: ...

#### Network Flows
- [`max_flow_ford_fulkerson`](../max_flow_ford_fulkerson.py)

    Ford-Fulkerson's algorithm to compute the maximum flow of a graph. Runs in $O(Ef)$ time, where $f$ is the maximum flow itself.

    Kattis problems to try on: ...

- [`max_flow_dinic`](../max_flow_dinic.py)

    Dinic's algorithm to compute the maximum flow of a graph. Runs in $O(V^2E)$ time.

    Kattis problems to try on: ...

- [`min_cost_max_flow`](../min_cost_max_flow.py)

    Two different approaches to compute the minimum cost maximum flow of a graph, including the shortest-path fast algorithm (SPFA). Maximize flow, then among all solutions of that same flow, find the minimum cost.

    Kattis problems to try on: ...

#### Matchings
- [`mcbm_unweighted_augmenting_path`](../mcbm_unweighted_augmenting_path.py)

    Minimum cardinality bipartite matching (MCBM) on an unweighted bipartite graph using augmenting paths. Also known as the Hopcroft-Karp algorithm, which runs in $O(\sqrt{V}E)$ time.

    Kattis problems to try on: ...

- [`mcbm_weighted_hungarian_kuhn_munkres`](../mcbm_weighted_hungarian_kuhn_munkres.py)

    Minimum (cost and) cardinality bipartite matching (MCBM) on a weighted bipartite graph using the Hungarian algorithm. Also known as the Kuhn-Munkres algorithm, which runs in $O(V^3)$ time. Rows are a single partition, then columns for the other partition.

    Kattis problems to try on: ...

- [`mcm_unweighted_edmonds`](../mcm_unweighted_edmonds.py)

    Minimum cardinality matching on general unweighted graphs using Edmond's blossom algorithm. Runs in $O(EV^2)$ time.

    Kattis problems to try on: ...

- [`mcm_weighted_dp_bitmask`](../mcm_weighted_dp_bitmask.py)

    Minimum cost matching on general weighted graphs using DP and bitmask. Runs in $O(V2^V)$ time.

    Kattis problems to try on: ...

#### Miscellaneous
- [`2sat`](../2sat.py)

    Check for 2-satisfiability of conjunctive normal forms (CNF). On top of checking if it's satisfiable, also finds such boolean assignment if any. Makes use of Kosaraju's algorithm. 

    Kattis problems to try on: ...

- [`chinese_postman_problem`](../chinese_postman_problem.py)

    Shortest circuit on a weighted undirected graph that visits every edge **at least** once (as opposed to TSP that requires visiting every vertex other than starting node **exactly** once). Makes use of Floyd-Warshall's APSP algorithm.

    Kattis problems to try on: ...

- [`hierholzer_eulerian_cycle`](../hierholzer_eulerian_cycle.py)

    Prints the Eulerian circuit given a directed Eulerian graph (visits every edge **exactly** once).

    Kattis problems to try on: ...

- [`min_path_cover_dag`](../min_path_cover_dag.py)

    You can use Hopcroft Karp's algorithm to find the minimum number of paths needed to cover the edges of a directed acyclic graph (DAG).

    Kattis problems to try on: ...

- [`maximum_clique_bron_kerbosch`](../maximum_clique_bron_kerbosch.py)

    Finds the maximum number such that exists a complete subgraph (clique) consisting of this many vertices using Bron-Kerbosch's algorithm, which is supposes to run in $O(3^\frac{V}{3})$ time.

    Kattis problems to try on: ...

- [`minimum_vertex_cover_bipartite`](../minimum_vertex_cover_bipartite.py)

    Minimum number of vertices needed to cover all edges of the graph using Kőnig's theorem.

    Kattis problems to try on: ...

- [`min_clique_cover_backtracking`](../min_clique_cover_backtracking.py)

    Minimum number of cliques needed to cover the entire graph, simply using the plain old backtracking.

    Kattis problems to try on: ...

### Advent of Code
- [`grid_template`](../grid_template.py)

    Just a grid template.

    AoC problems to try on: ...

- [`game_of_life`](../game_of_life.py)

    Simulation of the well-known Conway's game of life.

    AoC problems to try on: ...

- [`intcode`](../intcode.py)

    [Advent of Code's signature esoteric language.](https://esolangs.org/wiki/Intcode)

    AoC problems to try on: ...

### Miscellaneous
- [`cryptarithm`](../cryptarithm.py)

    Backtracking with optimized prunings to solve cryptarithm.

    Kattis problems to try on: ...

- [`inverse_index`](../inverse_index.py)

    Computes the number of pairs on an array with switched orders, also interpretable as the number of swaps needed when performing bubble sort on the array of size $n$. Runs in $O(n\log n)$ time.

    Kattis problems to try on: ...