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