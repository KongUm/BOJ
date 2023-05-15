#include <bits/stdc++.h>
using namespace std;

int n; string s, k;
vector<int> v;
map<string, int> mp;

void sol() {
    cin >> n; mp.clear(); v.clear();
    for (int i = 0; i < n; i++) {
        cin >> s >> k;
        if (mp.find(k) == mp.end()) {
            mp.insert({ k, mp.size() });
            v.push_back(0);
        }
        v[mp[k]]++;
    }

    int ans = 1;
    for (auto i : v) ans *= (i + 1);
    cout << ans - 1 << '\n';
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}