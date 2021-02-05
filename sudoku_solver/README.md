# sudoku_solver
_Un risolutore di sudoku scritto in Python_

sudoku_solver è un semplice programma che, preso in input un sudoku da completare, ne stampa la soluzione.


### Come funziona
Il programma prende in input il sudoku scritto sottoforma di matrice, vengono inseriti i valori già noti nelle apposite caselle, 0 altrimenti.

Prendendo come esempio il seguente sudoku di prova:
```
sudoku = [[5, 4, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 0, 0, 0, 9, 1, 6, 0],
          [0, 0, 2, 6, 0, 0, 0, 8, 0],
          [0, 0, 8, 4, 0, 2, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 0, 7, 0, 5, 3, 0, 0],
          [0, 9, 0, 0, 0, 1, 7, 0, 0],
          [0, 3, 7, 2, 0, 0, 0, 0, 4],
          [0, 0, 0, 0, 0, 0, 0, 9, 8]]
```

l'output del programma sarà il seguente:
```
Sudoku iniziale: 

 5 4 - | - - - | - - - 
 7 - - | - - 9 | 1 6 - 
 - - 2 | 6 - - | - 8 - 
 ------+-------+------ 
 - - 8 | 4 - 2 | - 5 - 
 - - - | - - - | - - - 
 - 2 - | 7 - 5 | 3 - - 
 ------+-------+------ 
 - 9 - | - - 1 | 7 - - 
 - 3 7 | 2 - - | - - 4 
 - - - | - - - | - 9 8 


Sudoku completato:

 5 4 6 | 1 2 8 | 9 7 3 
 7 8 3 | 5 4 9 | 1 6 2 
 9 1 2 | 6 3 7 | 4 8 5 
 ------+-------+------ 
 3 7 8 | 4 1 2 | 6 5 9 
 4 5 1 | 9 6 3 | 8 2 7 
 6 2 9 | 7 8 5 | 3 4 1 
 ------+-------+------ 
 2 9 4 | 8 5 1 | 7 3 6 
 8 3 7 | 2 9 6 | 5 1 4 
 1 6 5 | 3 7 4 | 2 9 8 
```
