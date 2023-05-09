#include <bits/stdc++.h>
#define int long long
#define ll long long
#define all(a) (a).begin(), (a).end()
using namespace std;
const int MAX = 100010, INF = (int) 1e9 + 7;

struct Point {
    int x, y;
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

int n;;
vector<Point> crd, hull;

bool cmp(Point a, Point b) {
    Point pa = a - crd[0], pb = b - crd[0];
    int ret = pa ^ pb;
    if (ret == 0) return (abs(pa.x) + abs(pa.y)) < (abs(pb.x) + abs(pb.y));
    else return ret < 0;
}

void grahamScan() {
    sort(crd.begin() + 1, crd.end(), cmp);

    int idx = 0;
    while (idx < n) {
        while (hull.size() >= 2) {
            auto p2 = hull.back(); hull.pop_back(); 
            auto p1 = hull.back();
            if (((p1 - crd[idx]) ^ (p2 - crd[idx])) < 0) { hull.push_back(p2); break; }
        }
        hull.push_back(crd[idx++]);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    for (int i = 0; i < n; i++) { 
        cin >> a >> b; crd.push_back({ a, b });
        if (b < crd[0].y || (b == crd[0].y && a < crd[0].x)) swap(crd[0], crd[i]); 
    }
    grahamScan();
    cout << hull.size();
}