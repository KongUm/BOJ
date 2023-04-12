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
    int x, y;
};
Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; } 
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y }; } // dot product
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; } // cross product

const int MAX = 10010;
int n, res = 0;
Point cord[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> cord[i].x >> cord[i].y;
    
    for (int i = 2; i < n; i++) res += ((cord[i - 1] - cord[0]) ^ (cord[i] - cord[0]));
    res = abs(res);
    cout << fixed; cout.precision(1);
    cout << (double) round(res * 5) / 10;
}