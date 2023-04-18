#include <bits/stdc++.h>
using namespace std;

const int MAX = 100010, INF = (int) 1e9 + 7;
int x, y, d, t, cnt = 0;
double res = INF, dist;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> x >> y >> d >> t;
    dist = sqrt((x * x + y * y));
    for (int i = 0; i < MAX; i++) {
        res = min(res, abs(dist) + cnt * t);
        if (abs(dist) <= d * 2) res = min(res, (double) (cnt + 2) * t);
        dist -= d; cnt++;
    }
    cout << fixed; cout.precision(12);
    cout << res << "\n";
}