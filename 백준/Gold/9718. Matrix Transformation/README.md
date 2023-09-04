# [Gold I] Matrix Transformation - 9718 

[문제 링크](https://www.acmicpc.net/problem/9718) 

### 성능 요약

메모리: 2152 KB, 시간: 0 ms

### 분류

애드 혹, 그리디 알고리즘, 수학

### 문제 설명

<p>You have an integer matrix A, with R rows and C columns.That means it has R rows with each row containing C integers. Two integers are adjacent if their container cells share an edge. For example, in the following grid </p>

<p>0 1 2<br>
3 4 5<br>
6 7 8</p>

<p>(0,1), (4,5), (1,4), (5,2)are adjacent but (0, 4), (2,6), (5,7) are not adjacent.</p>

<p>You are allowed to do only one kind of operation in the matrix. In each step you will select two adjacent cells and increase or decrease those two adjacent values by 1, i.e., both values are increased by 1 or both values are decreased by 1.  Given a matrix, determine whether it is possible to transform it to a zero matrix by applying the allowed operations. A zero matrix is the one where each of its entries is zero.  </p>

### 입력 

 <p>The first input line contains a positive integer,n, indicating the number of matrices (test cases). Each matrix starts with a line containing R(2≤R≤30) and C(2≤C≤30) separated by a single space. Each of the next R lines contains C integers. Each of these integers is between ‐20 and +20 inclusive.  Assume that each input matrix will have at least one non‐zero value.</p>

### 출력 

 <p>For each test case output “YES” if you can transform it to a zero matrix or “NO” otherwise (capital letter only).</p>

