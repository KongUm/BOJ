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

int n, res; Point lp = { INF, INF };
vector<Point> crd, stack1;

bool cmp(Point a, Point b) {
    Point pa = a - lp, pb = b - lp;
    int ret = pa ^ pb;
    if (ret == 0) return (abs(pa.x) + abs(pa.y)) < (abs(pb.x) + abs(pb.y));
    else return ret < 0;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    for (int i = 0; i < n; i++) { 
        cin >> a >> b; crd.push_back({ a, b });
        if (b < lp.y || (lp.y == b && a < lp.x)) lp = { a, b }; 
    }
    sort(all(crd), cmp);

    int idx = 0;
    while (idx < n) {
        while (stack1.size() >= 2) {
            auto p2 = stack1.back(); stack1.pop_back(); 
            auto p1 = stack1.back();
            if (((p1 - crd[idx]) ^ (p2 - crd[idx])) < 0) { stack1.push_back(p2); break; }
        }
        stack1.push_back(crd[idx++]);
    }

    for (int i = 2; i < stack1.size(); i++) res += ((stack1[i - 1] - stack1[0]) ^ (stack1[i] - stack1[0]));
    cout << abs(res) / 100;
}