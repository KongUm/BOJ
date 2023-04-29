# [Gold II] Rectilinear Regions - 14957 

[문제 링크](https://www.acmicpc.net/problem/14957) 

### 성능 요약

메모리: 4508 KB, 시간: 12 ms

### 분류

기하학

### 문제 설명

<p>A rectilinear path connecting two points in the plane is a path consisting of only horizontal and vertical line segments. A rectilinear path is said to be <em>monotone</em> with respect to the <em>x</em>-axis (resp., <em>y</em>-axis) if and only if its intersection with every vertical (resp., horizontal) line is either empty or a contiguous portion of that line. A <em>staircase</em> is a rectilinear path if it is monotone to both the <em>x</em>-axis and the <em>y</em>-axis, and a staircase is <em>unbounded</em> if it starts and ends with a semi-infinite horizontal segment, i.e., a segment that extends to infinity on both ends of the <em>x</em>-axis. Note that staircases can be either increasing or decreasing, depending on whether they go up or down as we move along them from left to right on the <em>y</em>-axis. A staircase with <em>n</em> vertical line segments is called a staircase with <em>n</em> steps.</p>

<p>Considering two unbounded staircases L and U, there can be several or no <em>closed</em> <em>rectilinear</em> <em>regions</em> bounded by staircases L and U. Among the closed rectilinear regions, some regions are bounded by a staircase L to the bottom and by a staircase U to the top. For example, in the following figure, the two regions colored yellow are that kind of closed rectilinear regions. We would like to compute the total area of such regions.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14957/1.png" style="height:262px; width:449px"></p>

<p style="text-align:center"><strong>Figure</strong> <strong>G.1.</strong> Two staircases L and U, where U has 3-steps and L has 4-steps. The two yellow colored regions are closed rectilinear regions bounded by a staircase L to the bottom, and a staircase U to the top. The <em>x<sub>i</sub><sup>L</sup></em>,<em>y<sub>i</sub><sup>L</sup></em> (resp., <em>x<sub>i</sub><sup>U</sup></em>,<em>y<sub>i</sub><sup>U</sup></em>) are the <em>x</em>-, <em>y</em>-coordinates of corner points of the staircase L (resp., U).</p>

<p style="text-align:center"><em>y</em><sub>0</sub> <em>x</em><sub>1</sub> <em>y</em><sub>1</sub> <em>x</em><sub>2</sub> <em>y</em><sub>2</sub> … <em>x<sub>n</sub></em> <em>y<sub>n</sub></em>  --------------------------------      (1)</p>

<p>where <em>x</em><sub>1</sub> < <em>x</em><sub>2</sub> < … < <em>x<sub>n</sub></em> for <em>x</em>-coordinates of vertical line segments, and <em>y</em><sub>0</sub> < <em>y</em><sub>1</sub> < … < <em>y<sub>n</sub></em> for <em>y</em>-coordinates of horizontal line segments of an increasing staircase or <em>y</em><sub>0</sub> > <em>y</em><sub>1</sub> > … > <em>y<sub>n</sub></em> for a decreasing staircase.</p>

<p>For example, given a 4-step staircase L represented with</p>

<blockquote>
<p>6 2 9 11 11 15 16 21 19</p>
</blockquote>

<p>and a 3-step staircase U represented with</p>

<blockquote>
<p>3 6 12 10 14 18 17</p>
</blockquote>

<p>the number of bounded rectilinear regions is 2 and the total area of the regions is 32 (see figure G.1).</p>

<p>Given two unbounded staircases L and U that <em>all</em> <em>x-coordinates</em> <em>represented</em> <em>in</em> <em>(1)</em> <em>of</em> <em>corner</em> <em>points</em> <em>of</em> <em>both</em> <em>L</em> <em>and</em> <em>U</em> <em>are</em> <em>unique,</em> <em>and</em> <em>all</em> <em>y-coordinates</em> <em>represented</em> <em>in</em> <em>(1)</em> <em>of</em> <em>corner</em> <em>points</em> <em>of</em> <em>both</em> <em>L</em> <em>and</em> <em>U</em> <em>are</em> <em>unique</em>, compute the total area of bounded rectilinear regions that bounded by L to the bottom of the regions and by U to the top of the regions.</p>

### 입력 

 <p>Your program is to read from standard input. The first line contains two positive integers <em>n</em> and <em>m</em>, respectively, representing the number of steps of unbounded staircases L and U, where 1 ≤ <em>n</em>,<em>m</em> ≤ 25,000    25,000. The second (resp., third) line contains 2<em>n</em> + 1 (resp., 2<em>m</em> + 1) integers representing the <em>x</em>-, <em>y</em>-coordinates of corner points of the staircase L (resp., U), and the integers are sequenced in the order of the notation (1). The coordinates are represented with non-negative integers less than or equal to 50,000.</p>

### 출력 

 <p>Your program is to write to standard output. The first line should contain two integers <em>k</em> and <em>w</em>, where <em>k </em>represents the number of closed rectilinear regions and <em>w</em> represents the total area of those regions. If there is no such regions, then your program should write 0 for both <em>k</em> and <em>w</em>.</p>

