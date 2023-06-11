#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'
#define YES cout << "YES" << "\n"
#define NO cout << "NO" << "\n"

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010, INF = (int) 1e9 + 7;
int n, ans; string s;
map<string, int> mp;
vector<string> v;

int get(int a, int b) {
    int ret = 0;
    for (int i = 0; i < 4; i++) ret += (v[a][i] != v[b][i]);
    return ret;
}

void sol() {
    mp.clear(), v.clear(), ans = INF;
    cin >> n; 
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (mp.find(s) == mp.end()) mp.insert({ s, 0 });
        if (mp[s] < 3) mp[s]++;
    }

    for (auto p : mp) {
        for (int i = 0; i < p.se; i++) v.push_back(p.fi);
    }

    int sz = v.size();
    for (int i = 0; i < sz; i++) {
        for (int j = 0; j < sz; j++) {
            for (int u = 0; u < sz; u++) {
                if (i == j || j == u || u == i) continue;
                ans = min(ans, get(i, j) + get(j, u) + get(u, i));
            }
        }
    }
    cout << ans << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}