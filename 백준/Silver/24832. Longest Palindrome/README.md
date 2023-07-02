# [Silver I] Longest Palindrome - 24832 

[문제 링크](https://www.acmicpc.net/problem/24832) 

### 성능 요약

메모리: 115004 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘, 문자열

### 문제 설명

<p>Returning back to problem solving, Gildong is now studying about palindromes. He learned that a <em>palindrome</em> is a string that is the same as its reverse. For example, strings "pop", "noon", "x", and "kkkkkk" are palindromes, while strings "moon", "tv", and "abab" are not. <strong>An empty string is also a palindrome.</strong></p>

<p>Gildong loves this concept so much, so he wants to play with it. He has $n$ <em>distinct</em> strings of equal length $m$. He wants to discard some of the strings (possibly none or all) and reorder the remaining strings so that the concatenation becomes a palindrome. He also wants the palindrome to be as long as possible. Please help him find one.</p>

### 입력 

 <p>The first line contains two integers $n$ and $m$ ($1 \le n \le 100$, $1 \le m \le 50$) — the number of strings and the length of each string.</p>

<p>Next $n$ lines contain a string of length $m$ each, consisting of lowercase Latin letters only. All strings are <em>distinct</em>.</p>

### 출력 

 <p>In the first line, print the length of the longest palindrome string you made.</p>

<p>In the second line, print that palindrome. If there are multiple answers, print any one of them. If the palindrome is empty, print an empty line or don't print this line at all.</p>

