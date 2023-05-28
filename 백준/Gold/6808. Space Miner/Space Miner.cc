#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
const int MAX = 1010, INF = (int) 1e9 + 7;

struct Point {
    int x, y, z, v, r;
};

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y, a.z + b.z }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y, a.z - b.z }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y + (ll) a.z * b.z };}
Point operator ^ (Point a, Point b) { return { a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x }; }

int int_getDist(Point a) { return (a.x * a.x + a.y * a.y + a.z * a.z); }

double getDist(Point a) { return sqrt(a.x * a.x + a.y * a.y + a.z * a.z); }

double absCross(Point a, Point b) { return getDist(a ^ b); }

double getArc(Point A, Point B, Point C) { // angle ABC -> theta B
    int a = getDist(B - C), b = getDist(C - A), c = getDist(A - B);
    double cos = ((a + c - b) / (2 * sqrt(a * c)));
    return acos(cos);
}

void print(Point a) { cout << a.x << ", " << a.y << ", " << a.z << "\n"; }

double getPointToLine(Point A, Point B, Point C) { // segment AB to point C 
    double ret = min(getDist(C - A), getDist(C - B));

    if ((B - A) * (C - A) >= 0 && (A - B) * (C - B) >= 0) {
        double h = absCross((A - C), (B - C)) / getDist((A - B));        
        ret = min(ret, h);
    }  
    return ret;
}

int n, m, d, ans = 0;
Point planet[MAX], way[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> planet[i].x >> planet[i].y >> planet[i].z >> planet[i].v >> planet[i].r;
    cin >> m;
    for (int i = 0; i < m; i++) cin >> way[i].x >> way[i].y >> way[i].z;
    cin >> d;

    for (int i = 0; i < n; i++) {
        for (int j = 1; j < m; j++) {
            double tmp = getPointToLine(way[j - 1], way[j], planet[i]);
            if (tmp <= planet[i].r + d) {
                ans += planet[i].v;
                break;
            }
        }
    }
    cout << ans;
}