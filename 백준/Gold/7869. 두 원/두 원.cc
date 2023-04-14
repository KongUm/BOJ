#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;

struct Point {
    double x, y;
};
Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; } 
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
double operator * (Point a, Point b) { return { (double) a.x * b.x + (double) a.y * b.y }; } // dot product
double operator ^ (Point a, Point b) { return { (double) a.x * b.y - (double) a.y * b.x }; } // cross product

//  Vector Template

double n, r1, r2, d, D, r, R, res;
Point c1, c2;

double get() {
    double th1, th2, S1, S2;
    th1 = acos((D + r1 * r1 - r2 * r2) / (2 * d * r1));
    th2 = acos((D + r2 * r2 - r1 * r1) / (2 * d * r2));

    S1 = (r1 * r1 * th1) - (r1 * r1 * sin(2 * th1) / 2);
    S2 = (r2 * r2 * th2) - (r2 * r2 * sin(2 * th2) / 2);
    return S1 + S2;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);   
    cin >> c1.x >> c1.y >> r1;
    cin >> c2.x >> c2.y >> r2;
    D = pow((c1.x - c2.x), 2) + pow((c1.y - c2.y), 2); d = sqrt(D); // ^ 2
    R = pow(r1 + r2, 2); r = pow(r1 - r2, 2);

    if (r < D && D < R) res = get();
    else if (r >= D) {
        res = min(r1, r2); res = res * res * M_PI;
    }
    else res = 0;
    cout << fixed; cout.precision(3);
    cout << res;
}