#include <bits/stdc++.h>
using namespace std;
const int MAX = 2010;
int n, m, vis[MAX], flag;
vector<int> g[MAX];

void dfs(int cur, int c) {
    vis[cur] = c;
    for (int nxt : g[cur]) {
        if (vis[nxt] == 0) dfs(nxt, ((c - 1) ^ 1) + 1);
        else if (vis[cur] == vis[nxt]) flag = true;
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int a, b;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    for (int i = 1; i < n + 1; i++) if (!vis[i]) vis[i] = 1, dfs(i, 1);
    cout << (1 ^ flag) << "\n";
}