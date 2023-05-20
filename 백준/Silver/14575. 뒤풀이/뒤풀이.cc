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
const int MAX = 100010;
int n, t, mini, maxi;
vector<pii> v;

bool check(int x) {
    int r = 0;
    for (int i = 0; i < n; i++) {
        if (v[i].fi > x) return false;
        r += min(v[i].se, x) - v[i].fi;
    }
    if (t - mini <= r) return true;
    return false;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> t;
    int a, b;
    int lo = 0, hi = 0;
    for (int i = 0; i < n; i++) {
        cin >> a >> b, v.push_back({ a, b });
        mini += a; maxi += b;
        hi = max(hi, b);
    }

    if (t < mini || maxi < t) {
        cout << -1;
        return 0;
    }
    
    while (lo + 1 < hi) {
        int mid = (lo + hi) / 2;
        if (check(mid)) hi = mid;
        else lo = mid;
    }
    
    if (check(hi)) cout << hi;
    else cout << -1;
}