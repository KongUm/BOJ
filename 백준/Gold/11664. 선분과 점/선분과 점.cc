#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
const int MAX = 100010, INF = (int) 1e9 + 7;

struct Point {
    int x, y, z;
};

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y, a.z + b.z }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y, a.z - b.z }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y + (ll) a.z * b.z };}
Point operator ^ (Point a, Point b) { return { a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x }; }

int int_getDist(Point a) { return (a.x * a.x + a.y * a.y + a.z * a.z); }

double getDist(Point a) { return sqrt(a.x * a.x + a.y * a.y + a.z * a.z); }

double absCross(Point a, Point b) { return getDist(a ^ b); }

double getArc(Point A, Point B, Point C) { // angle ABC -> seta B
    int a = getDist(B - C), b = getDist(C - A), c = getDist(A - B);
    double cos = ((a + c - b) / (2 * sqrt(a * c)));
    return acos(cos);
}

void print(Point a) {
    cout << a.x << ", " << a.y << ", " << a.z << "\n";
}

Point A, B, C;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> A.x >> A.y >> A.z >> B.x >> B.y >> B.z >> C.x >> C.y >> C.z;
    double res = min(getDist(C - A), getDist(C - B));

    if ((B - A) * (C - A) >= 0 && (A - B) * (C - B) >= 0) {
        double h = absCross((A - C), (B - C)) / getDist((A - B));        
        res = min(res, h);
    }  
    cout << fixed; cout.precision(10);
    cout << res;
}