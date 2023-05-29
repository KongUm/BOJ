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
const int MAX = 20010;
int n, k, unused = 1;
string tmp, s[MAX];
vector<int> g[MAX];
vector<string> tar;

void dfs(int cur, int p, int ti) {
    if (ti == tar.size()) return;

    for (int nxt : g[cur]) {
        if (nxt == p) continue;
        if (s[nxt] == tar[ti]) {
            return dfs(nxt, cur, ++ti);
        }
    }
    
    g[cur].push_back(unused);
    s[unused] = tar[ti];
    return dfs(unused++, cur, ++ti);
}

void print(int cur, int p, int dep) {
    vector<pair<string, int>> v;
    for (int i : g[cur]) v.push_back({ s[i], i });
    sort(all(v));
    
    for (auto p : v) {
        for (int i = 0; i < dep; i++) cout << "--";
        cout << p.fi << "\n";
        print(p.se, cur, dep + 1);
    }
}
signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        tar.clear(), cin >> k;
        for (int j = 0; j < k; j++) cin >> tmp, tar.push_back(tmp);
        dfs(0, -1, 0);
    }

    print(0, -1, 0);
}