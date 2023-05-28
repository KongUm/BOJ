# [Gold III] Space Miner - 6808 

[문제 링크](https://www.acmicpc.net/problem/6808) 

### 성능 요약

메모리: 2116 KB, 시간: 16 ms

### 분류

기하학, 3차원 기하학, 수학

### 문제 설명

<p>There are M (1 ≤ M ≤ 1, 000) planets each with v<sub>i</sub> (1 ≤ v<sub>i</sub> ≤ 10, 000) units of resources and radius r<sub>i</sub> (1 ≤ r<sub>i</sub> ≤ 100).</p>

<p>Starting from (0, 0, 0), you travel in straight lines through N (1 ≤ N ≤ 1, 000) waypoints in a specific order.</p>

<p>Whenever you travel within D + r<sub>i</sub> (1 ≤ D ≤ 50) units from a planet’s center, you can mine the planet using your tractor beam retrieving v<sub>i</sub> units of resources. Note that if you are exactly D units from the surface of the planet, you can mine the planet. If your path takes you through a planet, do not worry, since your spaceship can drill through planets, which makes mining even easier. Also note that you cannot mine the same planet on a subsequent visit.</p>

<p>Give the number of minerals that can be mined on your journey.</p>

<p>Hint: you should do all calculations with 64-bit integers.</p>

### 입력 

 <p>On the first line of input is the number M, the number of planets. On the next M lines are five integers describing each of the M planets. These integers are x<sub>i</sub> y<sub>i</sub> z<sub>i</sub> v<sub>i</sub> r<sub>i</sub>, where the planet i is at position (x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub>), (where −1, 000 ≤ x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> ≤ 1, 000) and this planet has v<sub>i</sub> resources and radius r<sub>i</sub>. On the next line is the number N, the number of waypoints to pass through. Each of the next N lines contains the position of these waypoints, as three integers x<sub>i</sub> y<sub>i</sub> z<sub>i</sub> (−1, 000 ≤ x<sub>i</sub>, y<sub>i</sub>, z<sub>i</sub> ≤ 1, 000). The last line of input is the number D, the maximum distance from a planet’s surface that your ship can be and still mine a planet.</p>

### 출력 

 <p>On one line, output the amount of minerals that you can mine on your journey.</p>

