#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;

struct Point {
    int x, y;
};

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y };}
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; }

int ccw(Point a, Point b, Point c) {
    auto v = (a - b) ^ (c - b);
    if (v < 0) return 1; // 반시계 방향
    else if (v > 0) return -1; // 시계 방향
    return 0; // 일직선 상
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b; 
    cin >> a >> b; Point p1 = { a, b };
    cin >> a >> b; Point p2 = { a, b };
    cin >> a >> b; Point p3 = { a, b };
    cout << ccw(p1, p2, p3);
}