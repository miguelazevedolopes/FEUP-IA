## Problem Formulation and Solution Search

### State Representation:

-   Left Bank with n Missionaries and m Cannibals, LB(nM,mC)
-   Right Bank with n Missionaries and m Cannibals, RB(nM,mC)
-   Boat with n Missionaries and m Cannibals, B(nM,mC)

### Initial State

-   LB(3M,3C)
-   RB(0M,0C)
-   B(0M,0C)

### Operators

-   Travel from left to right bank with n Missionaries and m Cannibals, n+m>=1 & n+m=<2, TLR(nM,mC)
-   Travel from right to left bank with n Missionaries and m Cannibals, n+m>=1 & n+m=<2, TLR(nM,mC)

At any time the number of Missionaries, n, and the number of Cannibals, m, at any of the banks must follow the n>m condition

### Solution Cost

Cost is defined by the number of times the boat crosses the river
