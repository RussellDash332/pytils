# pytils
> Not to be confused with the [`pytils`](https://pypi.org/project/pytils/) library for Russian-specific string utilities.

My collection of **Py**thon u**til**ity code**s** primarily designed for solving Kattis and Advent of Code (AoC) problems. It is intended to be as fast as possible, if not as short as possible. Feel free to use and customize them for your own use as you see fit.

## Treasure List

Classification taken from [`cp-algorithms`](https://cp-algorithms.com/).

### Algebra and Number Theory
#### Prime Numbers
- [`number_theory_prime_sieve`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_sieve.py)

    The classic Eratosthenes prime sieve that runs in $O(n\log\log n)$ time. Makes use of an array that stores the smallest prime factor.

- [`number_theory_prime_factorization`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_factorization.py)

    Applications of the prime sieve:
    - prime factorization of $n$
    - number of divisors of $n$
    - Euler's totient function, $\phi(n)$.

    > Kattis problem(s) to try on: [productdivisors](https://open.kattis.com/problems/productdivisors), [trickyfactoring](https://open.kattis.com/problems/trickyfactoring)

- [`number_theory_miller_rabin`](https://github.com/RussellDash332/pytils/blob/main/number_theory_miller_rabin.py)

    Checks if a number $n$ is probable prime. Works well in tandem with Pollard-Rho for integer factorization.

    > Kattis problem(s) to try on: [goldbach3](https://open.kattis.com/problems/goldbach3), [goldbach4](https://open.kattis.com/problems/goldbach4)

- [`number_theory_pollard_rho`](https://github.com/RussellDash332/pytils/blob/main/number_theory_pollard_rho.py)

    Finds a trivial factor of an integer $n$. Also includes Brent modification for faster version. Expected to run in $O(n^\frac{1}{4})$ time.

    > Kattis problem(s) to try on: [atrivialpursuit](https://open.kattis.com/problems/atrivialpursuit), [bigfactoring](https://open.kattis.com/problems/bigfactoring), [divisorsofasum](https://open.kattis.com/problems/divisorsofasum), [batchgcd](https://open.kattis.com/problems/batchgcd)

- [`number_theory_prime_counting`](https://github.com/RussellDash332/pytils/blob/main/number_theory_prime_counting.py)

    Counts the number of prime numbers up to $n$ in $O(\sqrt{n})$ time. Also includes Meissel-Lehmer algorithm that runs in $O(n^\frac{2}{3})$ time.

    > Kattis problem(s) to try on: [primecount](https://open.kattis.com/problems/primecount), [frumtolutalning](https://open.kattis.com/problems/frumtolutalning)

#### Modular Arithmetic
- [`number_theory_gcd_lcm`](https://github.com/RussellDash332/pytils/blob/main/number_theory_gcd_lcm.py)

    Basic GCD and LCM.

- [`number_theory_chinese_remainder`](https://github.com/RussellDash332/pytils/blob/main/number_theory_chinese_remainder.py)

    Classic Chinese Remainder Theorem.

    > Kattis problem(s) to try on: [chineseremainder](https://open.kattis.com/problems/chineseremainder), [generalchineseremainder](https://open.kattis.com/problems/generalchineseremainder)

- [`number_theory_lucas_theorem`](https://github.com/RussellDash332/pytils/blob/main/number_theory_lucas_theorem.py)

    Lucas' theorem, mainly used to compute a large binomial coefficient modulo some integer.

    > Kattis problem(s) to try on: [ghostbusters3](https://open.kattis.com/problems/ghostbusters3), [lights](https://open.kattis.com/problems/lights), [countingtrees](https://open.kattis.com/problems/countingtrees), [classicalcounting](https://open.kattis.com/problems/classicalcounting)

#### Miscellaneous
- [`fast_fourier_transform`](https://github.com/RussellDash332/pytils/blob/main/fast_fourier_transform.py)

    Fast Fourier Transform (FFT) and number theoretic transform (NTT) used mainly for multiplying two polynomials, runs in $O(n\log n)$ time, where $n$ is the polynomial degree.

    > Kattis problem(s) to try on: [polymul1](https://open.kattis.com/problems/polymul1), [polymul2](https://open.kattis.com/problems/polymul2), [fastfouriertransform](https://open.kattis.com/problems/fastfouriertransform), [allmodulopythagorean](https://open.kattis.com/problems/allmodulopythagorean), [allpairsums](https://open.kattis.com/problems/allpairsums), [numbertheoretictransform](https://open.kattis.com/problems/numbertheoretictransform), [diceresults](https://open.kattis.com/problems/diceresults)

- [`number_theory_mobius_function`](https://github.com/RussellDash332/pytils/blob/main/number_theory_mobius_function.py)

    Computes the Möbius function and stores them in an array, runs in $O(n\log\log n)$ time.

    > Kattis problem(s) to try on: [yule](https://open.kattis.com/problems/yule), [coprimeintegers](https://open.kattis.com/problems/coprimeintegers), [anothercoinweighingpuzzle](https://open.kattis.com/problems/anothercoinweighingpuzzle)

- [`number_theory_tonelli_shanks_cornacchia`](https://github.com/RussellDash332/pytils/blob/main/number_theory_tonelli_shanks_cornacchia.py)

    Solves $r^2 \equiv n \pmod p$ given an integer $n$ and prime number $p$, then uses the solution $r$ to solve $x^2 + dy^2 = p$.

    > Kattis problem(s) to try on: [gausssquares](https://open.kattis.com/problems/gausssquares), [allsquaresums](https://open.kattis.com/problems/allsquaresums)

### Data Structures
#### Lists
- [`circular_linked_list`](https://github.com/RussellDash332/pytils/blob/main/circular_linked_list.py)

    Simple implementation of circular linked list.

    > Kattis problem(s) to try on: [congaline](https://open.kattis.com/problems/congaline), [interviewqueue](https://open.kattis.com/problems/interviewqueue)

- [`sliding_window`](https://github.com/RussellDash332/pytils/blob/main/sliding_window.py)

    Four variants of sliding windows mentioned in CP Book (all run in $O(n)$ time)
    - smallest subarray size whose sum is `>= K`
    - smallest subarray size where all numbers in range `[1..K]` are within
    - `max(sum(A[i:i+K]) for i in range(len(A)-K+1))`
    - `[min(A[i:i+K]) for i in range(len(A)-K+1)]`

    > Kattis problem(s) to try on: [slidecount](https://open.kattis.com/problems/slidecount), [martiandna](https://open.kattis.com/problems/martiandna), [treeshopping](https://open.kattis.com/problems/treeshopping)

- [`next_greater_element`](https://github.com/RussellDash332/pytils/blob/main/next_greater_element.py)

    Computes the next greater element for each element in an array. Runs in $O(n)$ time.

    > Kattis problem(s) to try on: [whostheboss](https://open.kattis.com/problems/whostheboss), [flowingfountain](https://open.kattis.com/problems/flowingfountain)

- [`sorted_list`](https://github.com/RussellDash332/pytils/blob/main/sorted_list.py)

    Heavily-optimized implementation of a Python sorted list, expected to perform as well as what an actual $O(\log n)$-time sorted set/map operation would do.

    > Kattis problem(s) to try on: [investigatingfrogbehaviouronlilypadpatterns](https://open.kattis.com/problems/investigatingfrogbehaviouronlilypadpatterns), [golf](https://open.kattis.com/problems/golf)

#### Trees
- [`avl_tree`](https://github.com/RussellDash332/pytils/blob/main/avl_tree.py)

    AVL tree implementation, including the self-rebalancing part. All queries are done in $O(\log n)$ time, except inorder traversal that takes $O(n)$ time.

    > Kattis problem(s) to try on: [hiredhelp](https://open.kattis.com/problems/hiredhelp), [gcpc](https://open.kattis.com/problems/gcpc), [physicalmusic](https://open.kattis.com/problems/physicalmusic), [distributingseats](https://open.kattis.com/problems/distributingseats), [excellentengineers](https://open.kattis.com/problems/excellentengineers)

- [`fenwick_tree_rsq`](https://github.com/RussellDash332/pytils/blob/main/fenwick_tree_rsq.py)

    Classic Fenwick tree to answer range sum queries (RSQ). Both PURQ (point update, range query) and RURQ (range update, range query) versions are available. Updates and queries all run in $O(\log n)$ time.

    > Kattis problem(s) to try on: [fenwick](https://open.kattis.com/problems/fenwick), [supercomputer](https://open.kattis.com/problems/supercomputer), [taxtherich](https://open.kattis.com/problems/taxtherich), [hringvegurinn](https://open.kattis.com/problems/hringvegurinn), [tonlistarlisti](https://open.kattis.com/problems/tonlistarlisti)

- [`fenwick_tree_rmq`](https://github.com/RussellDash332/pytils/blob/main/fenwick_tree_rmq.py)

    Binary-indexed tree but to answer range minimum/maximum queries (RMQ). Updates and queries all run in $O(\log n)$ time.

- [`segment_tree_general`](https://github.com/RussellDash332/pytils/blob/main/segment_tree_general.py)

    General recursive implementation of segment tree, which can be customized to handle different aggregate functions. Updates and queries all run in $O(\log n)$ time.

    > Kattis problem(s) to try on: [stigavordur](https://open.kattis.com/problems/stigavordur)

- [`segment_tree_dynamic`](https://github.com/RussellDash332/pytils/blob/main/segment_tree_dynamic.py)

    Recursive implementation of the dynamic segment tree, which is currently optimized only for summation as aggregate. Updates and queries all run in $O(\log n)$ time.

    > Kattis problem(s) to try on: [japaneselottery](https://open.kattis.com/problems/japaneselottery), [queryonarray](https://open.kattis.com/problems/queryonarray)

- [`treap`](https://github.com/RussellDash332/pytils/blob/main/treap.py)

    Quick implementation of a treap data structure.

    > Kattis problem(s) to try on: [spilahlustun](https://open.kattis.com/problems/spilahlustun)

- [`wavelet_tree`](https://github.com/RussellDash332/pytils/blob/main/wavelet_tree.py)

    Incomplete implementation of the wavelet tree.

#### Miscellaneous
- [`sqrt_decomposition`](https://github.com/RussellDash332/pytils/blob/main/sqrt_decomposition.py)

    Sqrt-based data structure to support updates and sum queries in $O(\sqrt{n})$ time.

    > Kattis problem(s) to try on: [modulodatastructures](https://open.kattis.com/problems/modulodatastructures)

- [`ufds`](https://github.com/RussellDash332/pytils/blob/main/ufds.py)

    Classic union-find disjoint set (UFDS), also known as disjoint set union (DSU). Equipped with rank heuristics and path-compression, making both merging/union and querying run in $O(\alpha(n))$ time.

    > Kattis problem(s) to try on: [unionfind](https://open.kattis.com/problems/unionfind), [reachableroads](https://open.kattis.com/problems/reachableroads), [skolavslutningen](https://open.kattis.com/problems/skolavslutningen), [busnumbers](https://open.kattis.com/problems/busnumbers), [tildes](https://open.kattis.com/problems/tildes)

### Dynamic Programming
#### Knapsack
- [`knapsack`](https://github.com/RussellDash332/pytils/blob/main/knapsack.py)

    0-1 Knapsack with given capacity and list of weights and values. Runs in $O(nW)$ time where $n$ is the number of items and $W$ is the maximum capacity.

    > Kattis problem(s) to try on: [knapsack](https://open.kattis.com/problems/knapsack), [muzicari](https://open.kattis.com/problems/muzicari), [ninepacks](https://open.kattis.com/problems/ninepacks), [orders](https://open.kattis.com/problems/orders), [networking](https://open.kattis.com/problems/networking)

#### Convex Hull Trick
- [`convex_hull_trick`](https://github.com/RussellDash332/pytils/blob/main/convex_hull_trick.py)

    Convex hull optimization to optimize a specific $O(n^2)$ DP problem into an $O(n\log n)$ one. Here, we assume that the queries and slopes are sorted, thus reducing the problem into a sliding window after sorting.

    > Kattis problem(s) to try on: [coveredwalkway](https://open.kattis.com/problems/coveredwalkway)

- [`dynamic_convex_hull_trick_line_container`](https://github.com/RussellDash332/pytils/blob/main/dynamic_convex_hull_trick_line_container.py)

    Dynamic convex hull optimization, also known as the line container, solves a more general problem where lines and queries are not necessarily given in sorted order. Due to list insertion and deletion being $O(n)$, each operation should run in $O(n)$ time instead of $O(\log n)$, but should still be fast enough in most cases.

    > Kattis problem(s) to try on: [quintessentialbirthdaysurprise](https://open.kattis.com/problems/quintessentialbirthdaysurprise), [yatp](https://open.kattis.com/problems/yatp)

#### Miscellaneous
- [`knuth_optimization`](https://github.com/RussellDash332/pytils/blob/main/knuth_optimization.py)

    Knuth's optimization. Also known as a 1D1D dynamic programming, which optimizes a $O(n^2)$ DP into a $O(n \log n)$ one.

    > Kattis problem(s) to try on: [coveredwalkway](https://open.kattis.com/problems/coveredwalkway), [marathon2](https://open.kattis.com/problems/marathon2)

- [`longest_increasing_subsequence`](https://github.com/RussellDash332/pytils/blob/main/longest_increasing_subsequence.py)

    Finds the LIS length and outputs any of them. Another variant counts the number of distinct LIS in an array of $n$ numbers. Both functions run in $O(n\log n)$ time.

    > Kattis problem(s) to try on: [increasingsubsequence](https://open.kattis.com/problems/increasingsubsequence), [longincsubseq](https://open.kattis.com/problems/longincsubseq), [manhattanmornings](https://open.kattis.com/problems/manhattanmornings), [growingupishardtodo](https://open.kattis.com/problems/growingupishardtodo)

- [`travelling_salesman_problem_dp`](https://github.com/RussellDash332/pytils/blob/main/travelling_salesman_problem_dp.py)

    Finds the TSP cost in a graph of $n$ vertices and prints the TSP tour when needed. Both run in $O(n^2 2^n)$ time.

    > Kattis problem(s) to try on: [beepers](https://open.kattis.com/problems/beepers), [maximizingyourpay](https://open.kattis.com/problems/maximizingyourpay), [stystiskogarleidangurinn](https://open.kattis.com/problems/stystiskogarleidangurinn), [errands](https://open.kattis.com/problems/errands)

### String Processing
#### Suffix Array
- [`suffix_array_lcp`](https://github.com/RussellDash332/pytils/blob/main/suffix_array_lcp.py)

    Suffix array data structure alongside the longest common prefix (LCP) array for a string of length $n$. Suffix array construction runs in $O(n \log n)$ time.

    > Kattis problem(s) to try on: [suffixsorting](https://open.kattis.com/problems/suffixsorting), [burrowswheeler](https://open.kattis.com/problems/burrowswheeler), [dvaput](https://open.kattis.com/problems/dvaput), [repeatedsubstrings](https://open.kattis.com/problems/repeatedsubstrings)

#### String Matching
- [`string_matching_kmp`](https://github.com/RussellDash332/pytils/blob/main/string_matching_kmp.py)

    The Knuth-Morris-Pratt (KMP) algorithm to find all matches of a string within the target string of length $n$. Runs in $O(n)$ time.

    > Kattis problem(s) to try on: [stringmatching](https://open.kattis.com/problems/stringmatching), [powerstrings](https://open.kattis.com/problems/powerstrings), [radiotransmission](https://open.kattis.com/problems/radiotransmission), [clockpictures](https://open.kattis.com/problems/clockpictures)

- [`string_multimatching_aho_corasick`](https://github.com/RussellDash332/pytils/blob/main/string_multimatching_aho_corasick.py)

    The Aho-Corasick algorithm to find all matches of all query strings within the target string.

    > Kattis problem(s) to try on: [stringmultimatching](https://open.kattis.com/problems/stringmultimatching)

- [`string_multimatching_suffix_array`](https://github.com/RussellDash332/pytils/blob/main/string_multimatching_suffix_array.py)

    Suffix array can also be used to find all matches of all query strings within the target string.

    > Kattis problem(s) to try on: [stringmultimatching](https://open.kattis.com/problems/stringmultimatching)

#### Miscellaneous
- [`manacher_subpalindromes`](https://github.com/RussellDash332/pytils/blob/main/manacher_subpalindromes.py)

    Enumerates all palindromic substrings of a given string with length $n$ in $O(n)$ time.

    > Kattis problem(s) to try on: [genefolding](https://open.kattis.com/problems/genefolding), [palindromes](https://open.kattis.com/problems/palindromes)

- [`lexicographically_minimum_string_rotation_booth`](https://github.com/RussellDash332/pytils/blob/main/lexicographically_minimum_string_rotation_booth.py)

    Booth's lexicographically minimum string rotation algorithm that runs in $O(n)$ time where $n$ is the length of the string.

    > Kattis problem(s) to try on: [passwordrotation](https://open.kattis.com/problems/passwordrotation)

- [`z_function`](https://github.com/RussellDash332/pytils/blob/main/z_function.py)

    Computes the Z-function where `z = [lcp(s, s[i:]) for i in range(len(s))]`.

### Linear Algebra
- [`matrix_exponentiation_determinant_kirchoff`](https://github.com/RussellDash332/pytils/blob/main/matrix_exponentiation_determinant_kirchoff.py)

    Basic matrix (fast) exponentiation, determinant computation, and Kirchoff's tree theorem. The last two run in $O(N^3)$ time where $N$ is the size of the (square) matrix.

    > Kattis problem(s) to try on: [statetransfer](https://open.kattis.com/problems/statetransfer), [numbers2](https://open.kattis.com/problems/numbers2), [organising](https://open.kattis.com/problems/organising), [unicycliccount](https://open.kattis.com/problems/unicycliccount)

- [`rref_gaussian_elimination`](https://github.com/RussellDash332/pytils/blob/main/rref_gaussian_elimination.py)

    Converts a matrix $A$ into its reduced row-echelon form (RREF). Very useful for Gaussian elimination.

    > Kattis problem(s) to try on: [circumsphere](https://open.kattis.com/problems/circumsphere), [stoichiometry](https://open.kattis.com/problems/stoichiometry), [whiterabbit](https://open.kattis.com/problems/whiterabbit), [equationsolver](https://open.kattis.com/problems/equationsolver), [equationsolverplus](https://open.kattis.com/problems/equationsolverplus)

- [`simplex_linear_programming`](https://github.com/RussellDash332/pytils/blob/main/simplex_linear_programming.py)

    Simplex algorithm for linear programming, supports both maximization and minimization.

    > Kattis problem(s) to try on: [cheeseifyouplease](https://open.kattis.com/problems/cheeseifyouplease), [roadtimes](https://open.kattis.com/problems/roadtimes)

- [`conjugate_gradient`](https://github.com/RussellDash332/pytils/blob/main/conjugate_gradient.py)

    Solves the linear system $Ax=b$ where $A$ is a $n \times n$ real symmetric positive-definite matrix and $b$ is a $n$-dimensional vector in $O(kn^2)$ time, where $k << n$.

    > Kattis problem(s) to try on: [dreams](https://open.kattis.com/problems/dreams)

- [`qr_decomposition`](https://github.com/RussellDash332/pytils/blob/main/qr_decomposition.py)

    Decomposes $A$, a square matrix, into two matrices $Q$ and $R$ of the same size, where $Q$ is orthonormal and $R$ is upper triangular.

    > Kattis problem(s) to try on: [vector](https://open.kattis.com/problems/vector)

### Numerical Methods
- [`binary_search`](https://github.com/RussellDash332/pytils/blob/main/binary_search.py)

    Binary search for both lower bound and upper bound. Function has to be monotonic. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    > Kattis problem(s) to try on: [financialplanning](https://open.kattis.com/problems/financialplanning)

- [`ternary_search`](https://github.com/RussellDash332/pytils/blob/main/ternary_search.py)

    Ternary search on both integer cases and double/float cases. Finds the minimum of a decreasing-then-increasing function. Runs in $O(\log(b-a))$ time given two starting bounds $[a, b]$.

    > Kattis problem(s) to try on: [reconnaissance](https://open.kattis.com/problems/reconnaissance), [infiniteslides](https://open.kattis.com/problems/infiniteslides), [tricktreat](https://open.kattis.com/problems/tricktreat), [euclideantsp](https://open.kattis.com/problems/euclideantsp), [bottleflip](https://open.kattis.com/problems/bottleflip)

### Geometry
#### 2D
- [`compgeo_2d_polygon_area_centroid`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_polygon_area_centroid.py)

    Area and centroid of a 2D-polygon consisting of $n$ vertices. Runs in $O(n)$ time.

    > Kattis problem(s) to try on: [convexpolygonarea](https://open.kattis.com/problems/convexpolygonarea), [polygonarea](https://open.kattis.com/problems/polygonarea), [greedypolygons2](https://open.kattis.com/problems/greedypolygons2)

- [`compgeo_2d_point_in_polygon`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_point_in_polygon.py)

    Checks if a point is within a polygon using two different approaches: angle calculation and ray intersection.

    > Kattis problem(s) to try on: [pointinpolygon](https://open.kattis.com/problems/pointinpolygon)

- [`compgeo_2d_simple_polygon`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_simple_polygon.py)

    Checks if a polygon is simple, i.e. not self-intersecting.

    > Kattis problem(s) to try on: [polygon](https://open.kattis.com/problems/polygon), [girdingaherping](https://open.kattis.com/problems/girdingaherping)

- [`compgeo_2d_intersect`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_intersect.py)

    Line segment intersection.

    > Kattis problem(s) to try on: [segmentintersection](https://open.kattis.com/problems/segmentintersection), [target](https://open.kattis.com/problems/target), [carlsvacation](https://open.kattis.com/problems/carlsvacation)

- [`compgeo_2d_closest_pair`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_closest_pair.py)

    Closest pair problem. Given $n$ 2D-coordinates, find the closest pair among all $O(n^2)$ possible pairs. Runs in $O(n\log n)$ time.

    > Kattis problem(s) to try on: [closestpair1](https://open.kattis.com/problems/closestpair1), [closestpair2](https://open.kattis.com/problems/closestpair2)

- [`compgeo_2d_convex_hull`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_convex_hull.py)

    Given $n$ 2D-coordinates, compute its convex hull (smallest polygon that contains all points). Runs in $O(n\log n)$ time.

    > Kattis problem(s) to try on: [convexhull](https://open.kattis.com/problems/convexhull), [convexhull2](https://open.kattis.com/problems/convexhull2), [humanobservation](https://open.kattis.com/problems/humanobservation)

- [`compgeo_2d_half_plane`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_half_plane.py)

    Half-plane intersection. Given $n$ half-planes in 2D, find the polygon that is contained within all the half-planes.

    > Kattis problem(s) to try on: [marshlandrescues](https://open.kattis.com/problems/marshlandrescues), [bigbrother](https://open.kattis.com/problems/bigbrother)

- [`compgeo_2d_delaunay_triangulation_voronoi_diagram`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_delaunay_triangulation_voronoi_diagram.py)

    Computes the Delaunay triangulation (and/or the Voronoi diagram) of a set of $n$ points in 2D. Runs in $O(n \log n)$ time. Useful to compute Euclidean MST efficiently.

    > Kattis problem(s) to try on: [connections](https://open.kattis.com/problems/connections), [pandapreserve](https://open.kattis.com/problems/pandapreserve)

- [`compgeo_2d_minkowski_polygon_sum`](https://github.com/RussellDash332/pytils/blob/main/compgeo_2d_minkowski_polygon_sum.py)

    Compute the Minkowski sum of two convex polygons. In mathematical terms, $\{a+b \forall a \in A, b \in B\}$ for two convex polygons $A$ and $B$. Runs in $O(|A|+|B|)$ time.

    > Kattis problem(s) to try on: [geometryisfun](https://open.kattis.com/problems/geometryisfun), [takeonmeme](https://open.kattis.com/problems/takeonmeme)

#### 3D
- [`compgeo_3d_projection_intersection`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_projection_intersection.py)

    Solves different simple queries in 3D coordinate system:
    - point-to-segment projection
    - point-to-plane projection
    - point-line distance
    - point-plane distance
    - line-plane intersection

- [`compgeo_3d_convex_hull`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_convex_hull.py)

    Given $n$ 3D-coordinates where no four points lie on the same plane, compute its convex hull (smallest polyhedron that contains all points). KACTL version runs in $O(n^2)$ time, but an expected $O(n \log n)$ time algorithm exists as well.

    > Kattis problem(s) to try on: [worminapple](https://open.kattis.com/problems/worminapple)

- [`compgeo_3d_minimum_enclosing_circle`](https://github.com/RussellDash332/pytils/blob/main/compgeo_3d_minimum_enclosing_circle.py)

    Smallest circle/sphere (2D/3D) that covers all the given points. Outputs the center and the radius.

    > Kattis problem(s) to try on: [starsinacan](https://open.kattis.com/problems/starsinacan)

### Graph Algorithms
#### Graph Representation
- [`graph_adjacency_list`](https://github.com/RussellDash332/pytils/blob/main/graph_adjacency_list.py)

    Basic implementation of an adjacency list as a list of lists/dictionaries.

#### Graph Traversal
- [`traversal_bfs`](https://github.com/RussellDash332/pytils/blob/main/traversal_bfs.py)

    Simple BFS implementation. Runs in $O(V+E)$ time.

- [`traversal_dfs`](https://github.com/RussellDash332/pytils/blob/main/traversal_dfs.py)

    Simple iterative DFS implementation using stacks (because recursion is slow in Python). Runs in $O(V+E)$ time.

#### Connected Components & Graph Properties
- [`tarjan_bridges_cut_vertices`](https://github.com/RussellDash332/pytils/blob/main/tarjan_bridges_cut_vertices.py)

    Tarjan's algorithm to find bridges and cut vertices. Runs in $O(V+E)$ time.

    > Kattis problem(s) to try on: [birthday](https://open.kattis.com/problems/birthday), [caveexploration](https://open.kattis.com/problems/caveexploration)

- [`topological_sorting`](https://github.com/RussellDash332/pytils/blob/main/topological_sorting.py)

    Topological sorting using Kahn's algorithm or using the DFS approach. Runs in $O(V+E)$ time.

    > Kattis problem(s) to try on: [namsleid](https://open.kattis.com/problems/namsleid), [rodun](https://open.kattis.com/problems/rodun), [brexitnegotiations](https://open.kattis.com/problems/brexitnegotiations), [pachinkoprobability](https://open.kattis.com/problems/pachinkoprobability)

- [`scc_kosaraju`](https://github.com/RussellDash332/pytils/blob/main/scc_kosaraju.py)

    Extension of DFS topological sorting, Kosaraju's algorithm, to enumerate the strongly connected components (SCC). Runs in $O(V+E)$ time.

    > Kattis problem(s) to try on: [dominos](https://open.kattis.com/problems/dominos), [equivalences](https://open.kattis.com/problems/equivalences)

#### Minimum Spanning Trees
- [`minimum_spanning_tree_prim`](https://github.com/RussellDash332/pytils/blob/main/minimum_spanning_tree_prim.py)

    Prim's algorithm to compute the minimum spanning tree (MST) and its cost. Both sparse graph and dense graph variants are available. Former runs in $O(E\log V)$ time, but latter runs in $O(V^2)$.

    > Kattis problem(s) to try on: [minimumspanningtree](https://open.kattis.com/problems/minimumspanningtree), [freckles](https://open.kattis.com/problems/freckles), [lostmap](https://open.kattis.com/problems/lostmap), [naturereserve](https://open.kattis.com/problems/naturereserve)

- [`minimum_spanning_tree_kruskal`](https://github.com/RussellDash332/pytils/blob/main/minimum_spanning_tree_kruskal.py)

    Kruskal's algorithm to compute the minimum spanning tree (MST) and its cost using UFDS. Runs in $O(E\log E)$ time.

    > Kattis problem(s) to try on: [minimumspanningtree](https://open.kattis.com/problems/minimumspanningtree), [freckles](https://open.kattis.com/problems/freckles), [lostmap](https://open.kattis.com/problems/lostmap), [treehouses](https://open.kattis.com/problems/treehouses), [gridmst](https://open.kattis.com/problems/gridmst)

- [`wdsu_dynamic_mst`](https://github.com/RussellDash332/pytils/blob/main/wdsu_dynamic_mst.py)

    Weighted disjoint sets, particularly used to solve the dynamic MST problem: maintain MST given some edge insertions.

    > Kattis problem(s) to try on: [brillianceofwings2](https://open.kattis.com/problems/brillianceofwings2)

#### Shortest Paths
- [`sssp_bellman_ford`](https://github.com/RussellDash332/pytils/blob/main/sssp_bellman_ford.py)

    Single-source shortest path (SSSP) using Bellman-Ford's algorithm, which also includes negative cycle detection. Runs in $O(VE)$ time.

    > Kattis problem(s) to try on: [shortestpath3](https://open.kattis.com/problems/shortestpath3), [shortestpath4](https://open.kattis.com/problems/shortestpath4), [hauntedgraveyard](https://open.kattis.com/problems/hauntedgraveyard)

- [`sssp_dijkstra`](https://github.com/RussellDash332/pytils/blob/main/sssp_dijkstra.py)

    Single-source shortest path (SSSP) using modified Dijkstra's algorithm. Runs in $O(E\log E)$ time.

    > Kattis problem(s) to try on: [shortestpath1](https://open.kattis.com/problems/shortestpath1), [shortestpath2](https://open.kattis.com/problems/shortestpath2), [getshorty](https://open.kattis.com/problems/getshorty), [fendofftitan](https://open.kattis.com/problems/fendofftitan), [invasion](https://open.kattis.com/problems/invasion), [xentopia](https://open.kattis.com/problems/xentopia), [hopscotch50](https://open.kattis.com/problems/hopscotch50), [visualgo](https://open.kattis.com/problems/visualgo), [catchingnoodles](https://open.kattis.com/problems/catchingnoodles)

- [`apsp_floyd_warshall`](https://github.com/RussellDash332/pytils/blob/main/apsp_floyd_warshall.py)

    All-pairs shortest path (APSP) using Floyd-Warshall's algorithm. Runs in $O(V^3)$ time. Different variants are also available.
    - minimax/maximin (useful for min/maximum spanning trees)
    - transitive closure
    - +ve/-ve cycle detection
    - enumerate shortest path from anywhere to anywhere

    > Kattis problem(s) to try on: [allpairspath](https://open.kattis.com/problems/allpairspath), [arbitrage](https://open.kattis.com/problems/arbitrage), [speedyescape](https://open.kattis.com/problems/speedyescape), [assembly](https://open.kattis.com/problems/assembly)

#### Lowest Common Ancestor
- [`tarjan_offline_lca`](https://github.com/RussellDash332/pytils/blob/main/tarjan_offline_lca.py)

    Tarjan's algorithm to compute the LCA of some query pair of vertices on a tree rooted at vertex $0$. Runs in $O(V+Q)$ time.

    > Kattis problem(s) to try on: [rootedsubtrees](https://open.kattis.com/problems/rootedsubtrees), [treehopping](https://open.kattis.com/problems/treehopping), [tourists](https://open.kattis.com/problems/tourists), [easyascab](https://open.kattis.com/problems/easyascab)

#### Network Flows
- [`max_flow_ford_fulkerson`](https://github.com/RussellDash332/pytils/blob/main/max_flow_ford_fulkerson.py)

    Ford-Fulkerson's algorithm to compute the maximum flow of a graph. Runs in $O(Ef)$ time, where $f$ is the maximum flow itself.

    > Kattis problem(s) to try on: [conveyorbelts](https://open.kattis.com/problems/conveyorbelts)

- [`max_flow_dinic`](https://github.com/RussellDash332/pytils/blob/main/max_flow_dinic.py)

    Dinic's algorithm to compute the maximum flow of a graph. Runs in $O(V^2E)$ time.

    > Kattis problem(s) to try on: [maxflow](https://open.kattis.com/problems/maxflow), [mincut](https://open.kattis.com/problems/mincut), [waif](https://open.kattis.com/problems/waif), [avoidingtheapocalypse](https://open.kattis.com/problems/avoidingtheapocalypse), [gravamen](https://open.kattis.com/problems/gravamen)

- [`min_cost_max_flow`](https://github.com/RussellDash332/pytils/blob/main/min_cost_max_flow.py)

    Two different approaches to compute the minimum cost maximum flow of a graph, including the shortest-path fast algorithm (SPFA). Maximize flow, then among all solutions of that same flow, find the minimum cost.

    > Kattis problem(s) to try on: [mincostmaxflow](https://open.kattis.com/problems/mincostmaxflow), [ragingriver](https://open.kattis.com/problems/ragingriver), [tourist](https://open.kattis.com/problems/tourist), [catering](https://open.kattis.com/problems/catering), [aqueducts,](https://open.kattis.com/problems/aqueducts,)

#### Matchings
- [`mcbm_unweighted_augmenting_path`](https://github.com/RussellDash332/pytils/blob/main/mcbm_unweighted_augmenting_path.py)

    Minimum cardinality bipartite matching (MCBM) on an unweighted bipartite graph using augmenting paths. Also known as the Hopcroft-Karp algorithm, which runs in $O(\sqrt{V}E)$ time.

    > Kattis problem(s) to try on: [pianolessons](https://open.kattis.com/problems/pianolessons), [catvsdog](https://open.kattis.com/problems/catvsdog), [bioferd](https://open.kattis.com/problems/bioferd), [talltowers](https://open.kattis.com/problems/talltowers), [bookclub](https://open.kattis.com/problems/bookclub), [bookcircle](https://open.kattis.com/problems/bookcircle), [gopher2](https://open.kattis.com/problems/gopher2), [codenames](https://open.kattis.com/problems/codenames), [superdoku](https://open.kattis.com/problems/superdoku), [linije](https://open.kattis.com/problems/linije), [elementarymath](https://open.kattis.com/problems/elementarymath), [taxicab](https://open.kattis.com/problems/taxicab), [guardianofdecency](https://open.kattis.com/problems/guardianofdecency), [paintball](https://open.kattis.com/problems/paintball), [antennaplacement](https://open.kattis.com/problems/antennaplacement), [borders](https://open.kattis.com/problems/borders), [escapeplan](https://open.kattis.com/problems/escapeplan), [latinsquare](https://open.kattis.com/problems/latinsquare)

- [`mcbm_weighted_hungarian_kuhn_munkres`](https://github.com/RussellDash332/pytils/blob/main/mcbm_weighted_hungarian_kuhn_munkres.py)

    Minimum (cost and) cardinality bipartite matching (MCBM) on a weighted bipartite graph using the Hungarian algorithm. Also known as the Kuhn-Munkres algorithm, which runs in $O(V^3)$ time. Rows are a single partition, then columns for the other partition.

    > Kattis problem(s) to try on: [hungarianservices](https://open.kattis.com/problems/hungarianservices), [bond](https://open.kattis.com/problems/bond), [cheatingatwar](https://open.kattis.com/problems/cheatingatwar), [hexagon](https://open.kattis.com/problems/hexagon)

- [`mcm_unweighted_edmonds`](https://github.com/RussellDash332/pytils/blob/main/mcm_unweighted_edmonds.py)

    Minimum cardinality matching on general unweighted graphs using Edmond's blossom algorithm. Runs in $O(EV^2)$ time.

    > Kattis problem(s) to try on: [translatorsdinner](https://open.kattis.com/problems/translatorsdinner), [debellatio](https://open.kattis.com/problems/debellatio)

- [`mcm_weighted_dp_bitmask`](https://github.com/RussellDash332/pytils/blob/main/mcm_weighted_dp_bitmask.py)

    Minimum cost matching on general weighted graphs using DP and bitmask. Runs in $O(V2^V)$ time.

    > Kattis problem(s) to try on: [hidingchickens](https://open.kattis.com/problems/hidingchickens)

#### Miscellaneous
- [`2sat`](https://github.com/RussellDash332/pytils/blob/main/2sat.py)

    Check for 2-satisfiability of conjunctive normal forms (CNF). On top of checking if it's satisfiable, also finds such boolean assignment if any. Makes use of Kosaraju's algorithm. 

    > Kattis problem(s) to try on: [palindromicdna](https://open.kattis.com/problems/palindromicdna)

- [`chinese_postman_problem`](https://github.com/RussellDash332/pytils/blob/main/chinese_postman_problem.py)

    Shortest circuit on a weighted undirected graph that visits every edge **at least** once (as opposed to TSP that requires visiting every vertex other than starting node **exactly** once). Makes use of Floyd-Warshall's APSP algorithm.

    > Kattis problem(s) to try on: [joggingtrails](https://open.kattis.com/problems/joggingtrails)

- [`dominator_tree`](https://github.com/RussellDash332/pytils/blob/main/dominator_tree.py)

    Constructs the dominator tree on a directed graph. More details within the code.

    > Kattis problem(s) to try on: [roadblock](https://open.kattis.com/problems/roadblock)

- [`havel_hakimi_graph_realization`](https://github.com/RussellDash332/pytils/blob/main/havel_hakimi_graph_realization.py)

    Solves the graph realization, which constructs an undirected graph given the degree sequence (array of degrees of each vertex).

    > Kattis problem(s) to try on: [kjordaemikonigsbergs](https://open.kattis.com/problems/kjordaemikonigsbergs)

- [`heavy_light_decomposition`](https://github.com/RussellDash332/pytils/blob/main/heavy_light_decomposition.py)

    Heavy-light decomposition on a tree graph to efficiently answer aggregate queries on it, e.g. sum/max path between any two vertices in the tree.

    > Kattis problem(s) to try on: [vedur](https://open.kattis.com/problems/vedur), [vedurvegakerfi](https://open.kattis.com/problems/vedurvegakerfi)

- [`hierholzer_eulerian_cycle`](https://github.com/RussellDash332/pytils/blob/main/hierholzer_eulerian_cycle.py)

    Prints the Eulerian circuit given a directed Eulerian graph (visits every edge **exactly** once).

    > Kattis problem(s) to try on: [eulerianpath](https://open.kattis.com/problems/eulerianpath)

- [`min_path_cover_dag`](https://github.com/RussellDash332/pytils/blob/main/min_path_cover_dag.py)

    You can use Hopcroft Karp's algorithm to find the minimum number of paths needed to cover the edges of a directed acyclic graph (DAG).

- [`maximum_clique_bron_kerbosch`](https://github.com/RussellDash332/pytils/blob/main/maximum_clique_bron_kerbosch.py)

    Finds the maximum number such that exists a complete subgraph (clique) consisting of this many vertices using Bron-Kerbosch's algorithm, which is supposes to run in $O(3^\frac{V}{3})$ time.

    > Kattis problem(s) to try on: [maxclique](https://open.kattis.com/problems/maxclique), [letterballoons](https://open.kattis.com/problems/letterballoons)

- [`minimum_vertex_cover_bipartite`](https://github.com/RussellDash332/pytils/blob/main/minimum_vertex_cover_bipartite.py)

    Minimum number of vertices needed to cover all edges of the graph using Kőnig's theorem.

    > Kattis problem(s) to try on: [bilateral](https://open.kattis.com/problems/bilateral)

- [`min_clique_cover_backtracking`](https://github.com/RussellDash332/pytils/blob/main/min_clique_cover_backtracking.py)

    Minimum number of cliques needed to cover the entire graph, simply using the plain old backtracking.

    > Kattis problem(s) to try on: [busplanning](https://open.kattis.com/problems/busplanning), [committeeassignment](https://open.kattis.com/problems/committeeassignment)

### Advent of Code
- [`grid_template`](https://github.com/RussellDash332/pytils/blob/main/grid_template.py)

    Just a grid template.

- [`game_of_life`](https://github.com/RussellDash332/pytils/blob/main/game_of_life.py)

    Simulation of the well-known Conway's game of life.

- [`intcode`](https://github.com/RussellDash332/pytils/blob/main/intcode.py)

    [Advent of Code's signature esoteric language to "annoy" whoever is attempting AoC 2019.](https://esolangs.org/wiki/Intcode)

### Miscellaneous
- [`cryptarithm`](https://github.com/RussellDash332/pytils/blob/main/cryptarithm.py)

    Backtracking with optimized prunings to solve cryptarithm.

    > Kattis problem(s) to try on: [greatswercporto](https://open.kattis.com/problems/greatswercporto), [sendmoremoney](https://open.kattis.com/problems/sendmoremoney)

- [`gale_shapley_stable_matching`](https://github.com/RussellDash332/pytils/blob/main/gale_shapley_stable_matching.py)

    Constructs a stable matching given the list of preferences from both sides.

    > Kattis problem(s) to try on: [jealousyoungsters](https://open.kattis.com/problems/jealousyoungsters)

- [`inverse_index`](https://github.com/RussellDash332/pytils/blob/main/inverse_index.py)

    Computes the number of pairs on an array with switched orders, also interpretable as the number of swaps needed when performing bubble sort on the array of size $n$. Runs in $O(n\log n)$ time.

    > Kattis problem(s) to try on: [excursion](https://open.kattis.com/problems/excursion), [ultraquicksort](https://open.kattis.com/problems/ultraquicksort), [froshweek](https://open.kattis.com/problems/froshweek), [bread](https://open.kattis.com/problems/bread), [bilskurar](https://open.kattis.com/problems/bilskurar), [camels](https://open.kattis.com/problems/camels), [vudu](https://open.kattis.com/problems/vudu)

- [`sprague_grundy_mex`](https://github.com/RussellDash332/pytils/blob/main/sprague_grundy_mex.py)

    Sprague-Grundy theorem to find the Grundy value of a game state using minimum excluded value (MEX).

    > Kattis problem(s) to try on: [snim](https://open.kattis.com/problems/snim), [cuboidslicinggame](https://open.kattis.com/problems/cuboidslicinggame), [wheelgame](https://open.kattis.com/problems/wheelgame)