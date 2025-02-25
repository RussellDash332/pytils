# pytils
> Not to be confused with the [`pytils`](https://pypi.org/project/pytils/) library for Russian-specific string utilities.

My collection of **Py**thon u**til**ity code**s** primarily designed for solving Kattis and Advent of Code (AoC) problems. It is intended to be as fast as possible, if not as short as possible. Feel free to use and customize them for your own use as you see fit.

## Treasure List

Classification taken from [`cp-algorithms`](https://cp-algorithms.com/).

### Algebra and Number Theory
#### Prime Numbers
- [`number_theory_prime_sieve`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_sieve.py)

    The classic Eratosthenes prime sieve that runs in $O(n\log\log n)$ time. Makes use of an array that stores the smallest prime factor.

    Kattis problems to try on: ...

- [`number_theory_prime_factorization`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_factorization.py)

    Applications of the prime sieve:
    - prime factorization of $n$
    - number of divisors of $n$
    - Euler's totient function, $\phi(n)$.

    Kattis problems to try on: ...

- [`number_theory_miller_rabin`](https://github.com/RussellDash332/pytils/blob/main/number_theory_miller_rabin.py)

    Checks if a number $n$ is probable prime. Works well in tandem with Pollard-Rho for integer factorization.

    Kattis problems to try on: ...

- [`number_theory_pollard_rho`](https://github.com/RussellDash332/pytils/blob/main/number_theory_pollard_rho.py)

    Finds a trivial factor of an integer $n$. Also includes Brent modification for faster version. Expected to run in $O(n^\frac{1}{4})$ time.

    Kattis problems to try on: ...

- [`number_theory_prime_counting`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_counting.py)

    Counts the number of prime numbers up to $n$ in $O(\sqrt{n})$ time. Also includes Meissel-Lehmer algorithm that runs in $O(n^\frac{2}{3})$ time.

    Kattis problems to try on: ...

#### Modular Arithmetic
- [`number_theory_gcd_lcm`](https://github.com/RussellDash332/pytils/blob/main/number_theory_gcd_lcm.py)

    Basic GCD and LCM.

    Kattis problems to try on: ...

- [`number_theory_chinese_remainder`](https://github.com/RussellDash332/pytils/blob/main/number_theory_chinese_remainder.py)

    Classic Chinese Remainder Theorem.

    Kattis problems to try on: ...

- [`number_theory_lucas_theorem`](https://github.com/RussellDash332/pytils/blob/main/number_theory_lucas_theorem.py)

    Lucas' theorem, mainly used to compute a large binomial coefficient modulo some integer.

    Kattis problems to try on: ...

#### Miscellaneous
- [`fast_fourier_transform`](https://github.com/RussellDash332/pytils/blob/main/fast_fourier_transform.py)

    Fast Fourier Transform (FFT) used mainly for multiplying two polynomials, runs in $O(n\log n)$ time, where $n$ is the polynomial degree.

    Kattis problems to try on: ...

- [`number_theory_mobius_function`](https://github.com/RussellDash332/pytils/blob/main/number_theory_mobius_function.py)

    Computes the Möbius function and stores them in an array, runs in $O(n\log\log n)$ time.

    Kattis problems to try on: ...

- [`number_theory_tonelli_shanks_cornacchia`](https://github.com/RussellDash332/pytils/blob/main/number_theory_tonelli_shanks_cornacchia.py)

    Solves $r^2 \equiv n \pmod p$ given an integer $n$ and prime number $p$, then uses the solution $r$ to solve $x^2 + dy^2 = p$.

    Kattis problems to try on: ...

### Data Structures
#### Lists
- [`circular_linked_list`](https://github.com/RussellDash332/pytils/blob/main/circular_linked_list.py)

    Simple implementation of circular linked list.

    Kattis problems to try on: ...

- [`sliding_window`](https://github.com/RussellDash332/pytils/blob/main/sliding_window.py)

    Four variants of sliding windows mentioned in CP Book (all run in $O(n)$ time)
    - smallest subarray size whose sum is `>= K`
    - smallest subarray size where all numbers in range `[1..K]` are within
    - `max(sum(A[i:i+K]) for i in range(len(A)-K+1))`
    - `[min(A[i:i+K]) for i in range(len(A)-K+1)]`

    Kattis problems to try on: ...

- [`next_greater_element`](https://github.com/RussellDash332/pytils/blob/main/next_greater_element.py)

    Computes the next greater element for each element in an array. Runs in $O(n)$ time.

    Kattis problems to try on: ...

#### Trees
- [`avl_tree`](https://github.com/RussellDash332/pytils/blob/main/avl_tree.py)

    AVL tree implementation, including the self-rebalancing part. All queries are done in $O(\log n)$ time, except inorder traversal that takes $O(n)$ time.

    Kattis problems to try on: ...

- [`fenwick_tree_rsq`](https://github.com/RussellDash332/pytils/blob/main/fenwick_tree_rsq.py)

    Classic Fenwick tree to answer range sum queries (RSQ). Both PURQ (point update, range query) and RURQ (range update, range query) versions are available. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`fenwick_tree_rmq`](https://github.com/RussellDash332/pytils/blob/main/fenwick_tree_rmq.py)

    Binary-indexed tree but to answer range minimum/maximum queries (RMQ). Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`segment_tree_general`](https://github.com/RussellDash332/pytils/blob/main/segment_tree_general.py)

    General recursive implementation of segment tree, which can be customized to handle different aggregate functions. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`segment_tree_dynamic`](https://github.com/RussellDash332/pytils/blob/main/segment_tree_dynamic.py)

    Recursive implementation of the dynamic segment tree, which is currently optimized only for summation as aggregate. Updates and queries all run in $O(\log n)$ time.

    Kattis problems to try on: ...

- [`treap`](https://github.com/RussellDash332/pytils/blob/main/treap.py)

    Quick implementation of a treap data structure.

    Kattis problems to try on: N/A

- [`wavelet_tree`](https://github.com/RussellDash332/pytils/blob/main/wavelet_tree.py)

    Incomplete implementation of the wavelet tree.

    Kattis problems to try on: N/A

#### Miscellaneous
- [`sqrt_decomposition`](https://github.com/RussellDash332/pytils/blob/main/sqrt_decomposition.py)

    Sqrt-based data structure to support updates and sum queries in $O(\sqrt{n})$ time.

    Kattis problems to try on: ...

- [`ufds`](https://github.com/RussellDash332/pytils/blob/main/ufds.py)

    Classic union-find disjoint set (UFDS), also known as disjoint set union (DSU).

    Kattis problems to try on: ...

### Dynamic Programming
#### Knapsack
- [`knapsack`](https://github.com/RussellDash332/pytils/blob/main/knapsack.py)

    0-1 Knapsack with given capacity and list of weights and values.

    Kattis problems to try on: ...

#### Convex Hull Trick
- [`convex_hull_trick`](https://github.com/RussellDash332/pytils/blob/main/convex_hull_trick.py)

    Convex hull optimization to optimize a specific $O(n^2)$ DP problem into an $O(n\log n)$ one. Here, we assume that the queries and slopes are sorted, thus reducing the problem into a sliding window after sorting.

    Kattis problems to try on: ...

- [`dynamic_convex_hull_trick_line_container`](https://github.com/RussellDash332/pytils/blob/main/dynamic_convex_hull_trick_line_container.py)

    Dynamic convex hull optimization, also known as the line container, solves a more general problem where lines and queries are not necessarily given in sorted order. Due to list insertion and deletion being $O(n)$, each operation should run in $O(n)$ time instead of $O(\log n)$, but should still be fast enough in most cases.

    Kattis problems to try on: ...

#### Miscellaneous
- [`longest_increasing_subsequence`](https://github.com/RussellDash332/pytils/blob/main/longest_increasing_subsequence.py)

    Finds the LIS length and outputs any of them. Another variant counts the number of distinct LIS in an array of $n$ numbers. Both functions run in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`travelling_salesman_problem_dp`](https://github.com/RussellDash332/pytils/blob/main/travelling_salesman_problem_dp.py)

    Finds the TSP cost in a graph of $n$ vertices and prints the TSP tour when needed. Both run in $O(n^2 2^n)$ time.

    Kattis problems to try on: ...

### String Processing
#### Suffix Array
- [`suffix_array_lcp`](https://github.com/RussellDash332/pytils/blob/main/suffix_array_lcp.py)

    Suffix array data structure alongside the longest common prefix (LCP) array for a string of length $n$. Suffix array construction runs in $O(n \log n)$ time.

    Kattis problems to try on: ...

#### String Matching
- [`string_matching_kmp`](https://github.com/RussellDash332/pytils/blob/main/string_matching_kmp.py)

    The Knuth-Morris-Pratt (KMP) algorithm to find all matches of a string within the target string of length $n$. Runs in $O(n)$ time.

    Kattis problems to try on: ...

- [`string_multimatching_aho_corasick`](https://github.com/RussellDash332/pytils/blob/main/string_multimatching_aho_corasick.py)

    The Aho-Corasick algorithm to find all matches of all query strings within the target string.

    Kattis problems to try on: ...

- [`string_multimatching_suffix_array`](https://github.com/RussellDash332/pytils/blob/main/string_multimatching_suffix_array.py)

    Suffix array can also be used to find all matches of all query strings within the target string.

    Kattis problems to try on: ...

#### Miscellaneous
- [`manacher_subpalindromes`](https://github.com/RussellDash332/pytils/blob/main/manacher_subpalindromes.py)

    Enumerates all palindromic substrings of a given string with length $n$ in $O(n)$ time.

    Kattis problems to try on: ...

- [`lexicographically_minimum_string_rotation_booth`](https://github.com/RussellDash332/pytils/blob/main/lexicographically_minimum_string_rotation_booth.py)

    Booth's lexicographically minimum string rotation algorithm that runs in $O(n)$ time where $n$ is the length of the string.

    Kattis problems to try on: ...

- [`z_function`](https://github.com/RussellDash332/pytils/blob/main/z_function.py)

    Computes the Z-function where `z = [lcp(s, s[i:]) for i in range(len(s))]`.

    Kattis problems to try on: ...

### Linear Algebra
- [`rref_gaussian_elimination`](https://github.com/RussellDash332/pytils/blob/main/rref_gaussian_elimination.py)

    Converts a matrix $A$ into its reduced row-echelon form (RREF). Very useful for Gaussian elimination.

    Kattis problems to try on: ...

- [`simplex_linear_programming`](https://github.com/RussellDash332/pytils/blob/main/simplex_linear_programming.py)

    Simplex algorithm for linear programming, supports both maximization and minimization.

    Kattis problems to try on: ...

### Numerical Methods
- [`binary_search`](https://github.com/RussellDash332/pytils/blob/main/binary_search.py)

    Binary search for both lower bound and upper bound. Function has to be monotonic. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    Kattis problems to try on: ...

- [`ternary_search`](https://github.com/RussellDash332/pytils/blob/main/ternary_search.py)

    Ternary search on both integer cases and double/float cases. Finds the minimum of a decreasing-then-increasing function. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    Kattis problems to try on: ...

### Geometry
#### 2D
- [`compgeo_2d_polygon_area_centroid`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_polygon_area_centroid.py)

    Area and centroid of a 2D-polygon consisting of $n$ vertices. Runs in $O(n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_point_in_polygon`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_point_in_polygon.py)

    Checks if a point is within a polygon using two different approaches: angle calculation and ray intersection.

    Kattis problems to try on: ...

- [`compgeo_2d_intersect`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_intersect.py)

    Line segment intersection.

    Kattis problems to try on: ...

- [`compgeo_2d_closest_pair`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_closest_pair.py)

    Closest pair problem. Given $n$ 2D-coordinates, find the closest pair among all $O(n^2)$ possible pairs. Runs in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_convex_hull`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_convex_hull.py)

    Given $n$ 2D-coordinates, compute its convex hull (smallest polygon that contains all points). Runs in $O(n\log n)$ time.

    Kattis problems to try on: ...

- [`compgeo_2d_half_plane`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_half_plane.py)

    Half-plane intersection. Given $n$ half-planes in 2D, find the polygon that is contained within all the half-planes.

    Kattis problems to try on: ...

#### 3D
- [`compgeo_3d_projection_intersection`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_projection_intersection.py)

    Solves different simple queries in 3D coordinate system:
    - point-to-segment projection
    - point-to-plane projection
    - point-line distance
    - point-plane distance
    - line-plane intersection

    Kattis problems to try on: ...

- [`compgeo_3d_convex_hull`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_convex_hull.py)

    Given $n$ 3D-coordinates where no four points lie on the same plane, compute its convex hull (smallest polyhedron that contains all points). Runs in $O(n^2)$ time.

    Kattis problems to try on: ...

- [`compgeo_3d_minimum_enclosing_circle`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_minimum_enclosing_circle.py)

    Smallest circle/sphere (2D/3D) that covers all the given points. Outputs the center and the radius.

    Kattis problems to try on: ...

### Graph Algorithms
#### Graph Representation
- [`graph_adjacency_list`](https://github.com/RussellDash332/pytils/blob/main/graph_adjacency_list.py)

    Description.

    Kattis problems to try on: ...

#### Graph Traversal
- [`traversal_bfs`](https://github.com/RussellDash332/pytils/blob/main/traversal_bfs.py)

    Description.

    Kattis problems to try on: ...

- [`traversal_dfs`](https://github.com/RussellDash332/pytils/blob/main/traversal_dfs.py)

    Description.

    Kattis problems to try on: ...

#### Connected Components & Graph Properties
- [`tarjan_bridges_cut_vertices`](https://github.com/RussellDash332/pytils/blob/main/tarjan_bridges_cut_vertices.py)

    Description.

    Kattis problems to try on: ...

- [`topological_sorting`](https://github.com/RussellDash332/pytils/blob/main/topological_sorting.py)

    Description.

    Kattis problems to try on: ...

- [`scc_kosaraju`](https://github.com/RussellDash332/pytils/blob/main/scc_kosaraju.py)

    Description.

    Kattis problems to try on: ...

#### Shortest Paths
- [`sssp_bellman_ford`](https://github.com/RussellDash332/pytils/blob/main/sssp_bellman_ford.py)

    Description.

    Kattis problems to try on: ...

- [`sssp_dijkstra`](https://github.com/RussellDash332/pytils/blob/main/sssp_dijkstra.py)

    Description.

    Kattis problems to try on: ...

- [`apsp_floyd_warshall`](https://github.com/RussellDash332/pytils/blob/main/apsp_floyd_warshall.py)

    Description.

    Kattis problems to try on: ...

#### Minimum Spanning Trees
- [`minimum_spanning_tree_prim`](https://github.com/RussellDash332/pytils/blob/main/minimum_spanning_tree_prim.py)

    Description.

    Kattis problems to try on: ...

- [`minimum_spanning_tree_kruskal`](https://github.com/RussellDash332/pytils/blob/main/minimum_spanning_tree_kruskal.py)

    Description.

    Kattis problems to try on: ...

#### Lowest Common Ancestor
- [`tarjan_offline_lca`](https://github.com/RussellDash332/pytils/blob/main/tarjan_offline_lca.py)

    Description.

    Kattis problems to try on: ...

#### Network Flows
- [`max_flow_ford_fulkerson`](https://github.com/RussellDash332/pytils/blob/main/max_flow_ford_fulkerson.py)

    Description.

    Kattis problems to try on: ...

- [`max_flow_dinic`](https://github.com/RussellDash332/pytils/blob/main/max_flow_dinic.py)

    Description.

    Kattis problems to try on: ...

- [`min_cost_max_flow`](https://github.com/RussellDash332/pytils/blob/main/min_cost_max_flow.py)

    Description.

    Kattis problems to try on: ...

#### Matchings
- [`mcbm_unweighted_augmenting_path`](https://github.com/RussellDash332/pytils/blob/main/mcbm_unweighted_augmenting_path.py)

    Description.

    Kattis problems to try on: ...

- [`mcbm_weighted_hungarian_kuhn_munkres`](https://github.com/RussellDash332/pytils/blob/main/mcbm_weighted_hungarian_kuhn_munkres.py)

    Description.

    Kattis problems to try on: ...

- [`mcm_unweighted_edmonds`](https://github.com/RussellDash332/pytils/blob/main/mcm_unweighted_edmonds.py)

    Description.

    Kattis problems to try on: ...

- [`mcm_weighted_dp_bitmask`](https://github.com/RussellDash332/pytils/blob/main/mcm_weighted_dp_bitmask.py)

    Description.

    Kattis problems to try on: ...

#### Miscellaneous
- [`2sat`](https://github.com/RussellDash332/pytils/blob/main/2sat.py)

    Description.

    Kattis problems to try on: ...

- [`chinese_postman_problem`](https://github.com/RussellDash332/pytils/blob/main/chinese_postman_problem.py)

    Description.

    Kattis problems to try on: ...

- [`hierholzer_eulerian_cycle`](https://github.com/RussellDash332/pytils/blob/main/hierholzer_eulerian_cycle.py)

    Description.

    Kattis problems to try on: ...

- [`min_path_cover_dag`](https://github.com/RussellDash332/pytils/blob/main/min_path_cover_dag.py)

    Description.

    Kattis problems to try on: ...

- [`maximum_clique_bron_kerbosch`](https://github.com/RussellDash332/pytils/blob/main/maximum_clique_bron_kerbosch.py)

    Description.

    Kattis problems to try on: ...

- [`min_clique_cover_backtracking`](https://github.com/RussellDash332/pytils/blob/main/min_clique_cover_backtracking.py)

    Description.

    Kattis problems to try on: ...

- [`minimum_vertex_cover_bipartite`](https://github.com/RussellDash332/pytils/blob/main/minimum_vertex_cover_bipartite.py)

    Description.

    Kattis problems to try on: ...

### Advent of Code
- [`grid_template`](https://github.com/RussellDash332/pytils/blob/main/grid_template.py)

    Description.

    AoC problems to try on: ...

- [`game_of_life`](https://github.com/RussellDash332/pytils/blob/main/game_of_life.py)

    Description.

    AoC problems to try on: ...

- [`intcode`](https://github.com/RussellDash332/pytils/blob/main/intcode.py)

    Description.

    AoC problems to try on: ...

### Miscellaneous
- [`cryptarithm`](https://github.com/RussellDash332/pytils/blob/main/cryptarithm.py)

    Description.

    Kattis problems to try on: ...

- [`inverse_index`](https://github.com/RussellDash332/pytils/blob/main/inverse_index.py)

    Description.

    Kattis problems to try on: ...