# Determinant of a matrix

This simple Python program takes a square matrix in input and checks if the matrix is actually square; if so, the program calculates recursively the determinant of the matrix.


### Algorithm

The program implements the _Laplace expansion_ algorithm.

Considering a 2x2 matrix such as

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;A&space;=&space;\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}\\&space;a_{21}&space;&&space;a_{22}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;A&space;=&space;\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}\\&space;a_{21}&space;&&space;a_{22}&space;\end{bmatrix}" title="A = \begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix}" /></a>


The calculus of the determinant is immediate and it goes as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;det(A)&space;=&space;a_{11}a_{22}&space;-&space;a_{12}a_{21}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;det(A)&space;=&space;a_{11}a_{22}&space;-&space;a_{12}a_{21}" title="det(A) = a_{11}a_{22} - a_{12}a_{21}" /></a>


Now, given the base case, we can generalize the function for bigger square matrices:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;det(A)&space;=&space;[(-1)^{1&plus;1}a_{11}det(A_{1,1})]&space;&plus;&space;[(-1)^{1&plus;2}a_{12}det(A_{1,2})]&space;&plus;&space;...&space;&plus;&space;[(-1)^{1&plus;n}a_{1n}det(A_{1,n})]" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;det(A)&space;=&space;[(-1)^{1&plus;1}a_{11}det(A_{1,1})]&space;&plus;&space;[(-1)^{1&plus;2}a_{12}det(A_{1,2})]&space;&plus;&space;...&space;&plus;&space;[(-1)^{1&plus;n}a_{1n}det(A_{1,n})]" title="det(A) = [(-1)^{1+1}a_{11}det(A_{1,1})] + [(-1)^{1+2}a_{12}det(A_{1,2})] + ... + [(-1)^{1+n}a_{1n}det(A_{1,n})]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;=&space;\sum_{j=1}^{n}&space;(-1)^{1&plus;j}a_{1j}det(A_{1,j})" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;=&space;\sum_{j=1}^{n}&space;(-1)^{1&plus;j}a_{1j}det(A_{1,j})" title="= \sum_{j=1}^{n} (-1)^{1+j}a_{1j}det(A_{1,j})" /></a>

Where det(A1j) is the minor of element a1j, i.e. the determinant of the submatrix A1j, formed out of the matrix A by excluding the row and column of the element.
