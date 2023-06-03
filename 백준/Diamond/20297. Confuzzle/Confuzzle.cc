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
const int MAX = 100010, INF = (int) 1e9 + 7;
int n, ty[MAX], id[MAX], dep[MAX], ans = INF;
vector<int> g[MAX];
map<int, int> mp[MAX]; 

void uni(int a, int b) {   
    if (mp[id[a]].size() < mp[id[b]].size()) swap(a, b); // 무조건 b가 더 작음
    for (auto p : mp[id[b]]) {
        if (mp[id[a]].find(p.fi) != mp[id[a]].end()) {
            if (mp[id[a]][p.fi] + p.se > 0) ans = min(ans, mp[id[a]][p.fi] + p.se - min(dep[a], dep[b]) * 2);
        }
        else mp[id[a]].insert({ p.fi, p.se });
        mp[id[a]][p.fi] = min(mp[id[a]][p.fi], p.se);
    }
    
    mp[id[b]].clear();
    id[b] = id[a];
}

void dfs(int cur, int par) {
    mp[id[cur]].insert({ ty[cur], dep[cur] });
    for (int nxt : g[cur]) {
        if (nxt == par) continue;
        dep[nxt] = dep[cur] + 1;
        dfs(nxt, cur);
        uni(nxt, cur);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n; int a, b;
    for (int i = 1; i < n + 1; i++) cin >> ty[i];
    for (int i = 1; i < n + 1; i++) id[i] = i;
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        g[a].push_back(b), g[b].push_back(a);
    }
    
    dfs(1, -1);
    cout << ans;
}