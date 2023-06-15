#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;
int n, ans;
vector<pii> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a >> b, v.push_back({ a, b });
    for (int i = 1; i < n; i++) {
        if (v[i - 1].fi == v[i].fi && v[i - 1].se < v[i].se) ans += (v[i].se - v[i - 1].se) * 2;
        if (v[i - 1].se == v[i].se && v[i - 1].fi > v[i].fi) ans += (v[i - 1].fi - v[i].fi) * 2;
    }
    cout << ans;
}