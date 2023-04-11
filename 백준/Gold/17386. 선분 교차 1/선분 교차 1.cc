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
Point u1, v1, u2, v2;

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; }
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y };}
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; }

bool checker() {
    int l1 = (u1 - u2) ^ v1, l2 = v2 ^ v1; 
    if (l2 < 0) { l2 *= -1; l1 *= -1; }
    int k1 = (u2 - u1) ^ v2, k2 = v1 ^ v2;
    if (k2 < 0) { k2 *= -1; k1 *= -1; }

    if ((l1 >= 0 && l1 <= l2) && (k1 >= 0 && k1 <= k2)) return true;
    else return false;

}

void makeVector() {
    int a, b; 
    cin >> a >> b; u1 = { a, b }; // 위치 벡터 
    cin >> a >> b; v1 = { a, b }; v1 = v1 - u1; // 방향 벡터

    cin >> a >> b; u2 = { a, b };
    cin >> a >> b; v2 = { a, b }; v2 = v2 - u2;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    makeVector();
    cout << checker() << "\n";    
}