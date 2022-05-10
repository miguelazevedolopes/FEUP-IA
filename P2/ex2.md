2.1

a) C
b) E
c) D
d) C (menor heuristica)
e) G

2.2

a) 

State Representation:

Matrix B[N][N] where (xs,ys) represents the position of 0

Operators:

- Up
- Down
- Left
- Right


| Operator | Precondition | Effect              | Cost |
|----------|--------------|---------------------|------|
| Up       | ys>1         | B[xs,ys]=B[xs,ys-1]=0 | 1    |
| Down     | ys<N         |                     | 1    |
| Left     | xs>1         |                     | 1    |
| Right    | xs<N         |                     | 1    |

