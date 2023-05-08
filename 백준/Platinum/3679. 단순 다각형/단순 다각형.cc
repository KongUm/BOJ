#include <bits/stdc++.h>
#define int long long
#define ll long long
#define all(a) (a).begin(), (a).end()
using namespace std;
const int MAX = 100010, INF = (int) 1e12 + 7;

struct Point {
    int x, y, id;
};

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y };}
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; }

int getDist(Point a) { return (a.x * a.x + a.y * a.y); }

int n; Point lp = { INF, INF, INF };
vector<Point> crd, hull;

bool cmp(Point a, Point b) {
    Point pa = a - lp, pb = b - lp;
    int ret = pa ^ pb;
    if (ret == 0) return (abs(pa.x) + abs(pa.y)) < (abs(pb.x) + abs(pb.y));
    else return ret < 0;
}

void sol() {
    int a, b; lp = { INF, INF, INF }; crd.clear(); hull.clear();
    cin >> n;
    for (int i = 0; i < n; i++) { 
        cin >> a >> b; crd.push_back({ a, b, i });
        if (b < lp.y || (lp.y == b && a < lp.x)) lp = { a, b, i }; 
    }
    sort(all(crd), cmp);

    vector<Point> tmp;

    for (int i = 1; i < n; i++) {
        if (((crd[0] - crd[n - 1]) ^ (crd[0] - crd[i])) == 0) tmp.push_back(crd[i]);
    }

    for (int i = 0; i < n - tmp.size(); i++) cout << crd[i].id << " ";
    while (!tmp.empty()) {
        cout << tmp.back().id << " "; 
        tmp.pop_back();
    }

    cout << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}