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
const int MAX = 100010;
int n, m, spTable[MAX][22], dep[MAX];
vector<int> g[MAX];

void buildSparseTable() {
    for (int j = 1; j < 22; j++) {
        for (int i = 1; i < n + 1; i++) {
            spTable[i][j] = spTable[spTable[i][j - 1]][j - 1];
        }
    }
}

int lca(int a, int b) {
    if (dep[a] > dep[b]) swap(a, b);
    int diff = abs(dep[b] - dep[a]);
    for (int i = 0; diff; i++) {
        if (diff & 1) b = spTable[b][i];
        diff >>= 1;
    }
    if (a == b) return a;
    for (int i = 21; i > -1; i--) {
        if (spTable[a][i] != spTable[b][i]) a = spTable[a][i], b = spTable[b][i];
    }
    return spTable[a][0];
}

int getDist(int a, int b) {
    return dep[a] + dep[b] - 2 * dep[lca(a, b)];
}

void dfs(int cur, int pr, int d) {
    dep[cur] = d;
    for (int nxt : g[cur]) {
        if (nxt != pr) spTable[nxt][0] = cur, dfs(nxt, cur, d + 1);
    }
}

void sol() {
    int x, y, a, b, k;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        g[a].push_back(b), g[b].push_back(a);
    }
    dfs(1, -1, 1), buildSparseTable();
    
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> a >> b >> k;
        vector<int> v; int flag = 0;
        v.push_back(getDist(a, b));
        v.push_back(getDist(a, x) + 1 + getDist(y, b));
        v.push_back(getDist(a, y) + 1 + getDist(x, b));

        for (int j : v) {
            if (j > k) continue;
            int df = abs(j - k);
            if (df % 2 == 0) flag = 1;
        }
        if (flag) YES;
        else NO;
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    sol();
}