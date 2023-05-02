#include <bits/stdc++.h>
#define int long long
#define ll long long
#define all(a) (a).begin(), (a).end()
using namespace std;
const int MAX = 100010, INF = (int) 1e9 + 7;

struct Point {
    int x, y, r, id;
};

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y };}
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; }

int getDist(Point a) { return (a.x * a.x + a.y * a.y); }

double getArc(Point A, Point B, Point C) { // angle ABC -> seta B
    int a = getDist(B - C), b = getDist(C - A), c = getDist(A - B);
    double cos = ((a + c - b) / (2 * sqrt(a * c)));
    return acos(cos);
}

int n, a, b, r;
vector<Point> v;

bool cmp(Point a, Point b) {
    int d1 = getDist(a), d2 = getDist(b); 
    int ret1 = (d1 * b.r * b.r), ret2 = (d2 * a.r * a.r);
    if (ret1 == ret2) return a.id < b.id;
    return ret1 < ret2;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b >> r;
        v.push_back({ a, b, r, i + 1 });
    }
    sort(all(v), cmp);
    for (auto p : v) cout << p.id << "\n";
}