#include <bits/stdc++.h>

#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
const int MAX = 10010;

ll two_pointer(vector<ll> &v, ll n, ll m) {
    ll ans = 0, start = 0, end = 0, sum = 0;

    while (end <= n) {
        if (sum >= m) {
            sum -= v[start];
            start += 1;
        } else if (sum < m) {
            sum += v[end];
            end += 1;
        }
        if (sum == m) ans += 1;
    }
    return ans;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    ll n, m, temp;
    vector<ll> v;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        v.push_back(temp);
    }
    cout << two_pointer(v, n, m);
}