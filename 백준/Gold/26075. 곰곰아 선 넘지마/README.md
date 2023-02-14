# [Gold IV] 곰곰아 선 넘지마 - 26075 

[문제 링크](https://www.acmicpc.net/problem/26075) 

### 성능 요약

메모리: 123408 KB, 시간: 136 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="max-height:125px; object-fit:contain; display:inline-block;"> <img alt="" src="" style="max-height:125px; object-fit:contain; display:inline-block;"></p>

<p>$N$ 개의 숫자 $0$ 과 $M$ 개의 숫자 $1$ 로 이루어진 길이의 $N+M$ 의 두 문자열 <strong>S</strong> 와 <strong>T</strong> 가 있다. 이 문자열을 가지고 두 곰곰이 친구가 서로 재미있게 놀다가 갑자기 한 곰곰이가 선을 넘어버렸다.</p>

<p><strong>“선 넘지마”</strong></p>

<p>라는 선언과 함께 문자열 <strong>S</strong> 와 <strong>T</strong> 가 선을 사이에 두고 분리되어 버렸다. 곰곰이는 이제 노는 것을 그만두고 문자열을 정리하기로 했다. 하지만 선을 넘을 수 없기 때문에 <strong>S</strong> 문자열 앞에 앉은 곰곰이는 <strong>S</strong> 문자열만, <strong>T</strong> 문자열 앞에 앉은 곰곰이는 <strong>T</strong> 문자열만 수정할 수 있다.</p>

<p>곰곰이는 문자열에서 임의의 인접한 두 문자의 위치를 바꿀 수 있다. 문자의 위치를 바꾸는 연산을 $X$ 번 수행하면 $X^2$ 만큼의 비용이 든다.</p>

<p>두 곰곰이는 각각 <strong>S</strong> 문자열에서 $X$ 번, <strong>T</strong> 문자열에서 $Y$ 번의 연산을 수행하여, <strong>S</strong> 와 <strong>T</strong> 가 같은 문자열이 되도록 만들고 싶다. 이 때, 두 곰곰이가 사용한 비용의 합의 최솟값, 즉 $X^2 + Y^2$ 값의 최솟값을 구해보자.</p>

### 입력 

 <p>첫째 줄에는 음이 아닌 정수 $N$, $M$ 이 공백을 사이에 두고 주어진다. ($1 \le N + M \le 100\,000$)</p>

<p>이어 두 번째 줄과 세 번째 줄에 각각 문자열 <strong>S</strong> 와 <strong>T</strong> 가 주어진다.</p>

<p>문자열 <strong>S</strong> 와 <strong>T</strong> 의 길이는 $N+M$ 이며, $N$ 개의 숫자 $0$ 과 $M$ 개의 숫자 $1$ 로 이루어져 있다.</p>

### 출력 

 <p>가능한 $X^2 + Y^2$ 의 최소값을 출력한다.</p>

