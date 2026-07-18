Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===================== RESTART: C:/Users/sanke/DAA exp 1.py =====================
Interpolation Search Demonstration
----------------------------------
Array   : [4, 9, 15, 21, 28, 36, 44, 53, 68, 79, 91, 110]
Element : 44
Result  : Element found at index 6
Comparisons : 3

Performance Comparison
--------------------------------------------------------------------------------
Size      IS Time(ms)     BS Time(ms)     IS Count          BS Count          
--------------------------------------------------------------------------------
1000      0.00211         0.00276         3                 10                
5000      0.00148         0.00130         5                 10                
10000     0.00296         0.00259         2                 13                
50000     0.00390         0.00501         6                 15                
100000    0.00210         0.00443         4                 15                

============================ RESTART: C:/Users/sanke/DAA exp - 2.py ===========================
Pattern Matching Algorithms
---------------------------
Text    : COMPUTERSCIENCECOMPUTER
Pattern : COM

Naive Search
Match Positions : [0, 15]
Comparisons     : 27

KMP Search
Match Positions : [0, 15]
Comparisons     : 25

Rabin-Karp Search
Match Positions : [0, 15]
Comparisons     : 6

Performance Analysis
-------------------------------------------------------
Pattern     Naive     KMP       RK        
-------------------------------------------------------
ABC         14900     14337     350       
BCDA        14955     14374     111       
ABCDEA      15011     14424     152       
ABCDEABC    15011     14426     172       

================================== RESTART: C:/Users/sanke/DAA exp - 3.py =================================
Minimum Spanning Tree
==================================================

Using Kruskal's Algorithm
------------------------------
Edge 4 - 5 : 2
Edge 2 - 4 : 3
Edge 0 - 2 : 4
Edge 5 - 6 : 4
Edge 1 - 2 : 5
Edge 3 - 5 : 6
Total Weight : 24

Using Prim's Algorithm
------------------------------
Edge 0 - 2 : 4
Edge 2 - 4 : 3
Edge 4 - 5 : 2
Edge 5 - 6 : 4
Edge 2 - 1 : 5
Edge 5 - 3 : 6
Total Weight : 24
>>> 
================================== RESTART: C:/Users/sanke/DAA exp - 4.py =================================
Shortest Path Using Dijkstra's Algorithm
====================================================================
Vertex    Distance    Path
--------------------------------------------------------------------
0         0           0
1         2           0 -> 1
2         5           0 -> 1 -> 2
3         6           0 -> 1 -> 3
4         7           0 -> 1 -> 3 -> 4
5         9           0 -> 1 -> 3 -> 4 -> 5
6         11          0 -> 1 -> 3 -> 4 -> 6
