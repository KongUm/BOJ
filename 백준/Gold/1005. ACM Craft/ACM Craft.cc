#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MAX = 1010;
int n, m, w, dst[MAX], idg[MAX], dp[MAX];
vector<int> g[MAX], rg[MAX];

void topologicalSort() {
    queue<int> que;
    for (int i = 1; i < n + 1; i++) if (idg[i] == 0) que.push(i);
    
    while (!que.empty()) {
        int cur = que.front(); que.pop();
        dp[cur] = dst[cur];
        for (int i : rg[cur]) dp[cur] = max(dp[cur], dp[i] + dst[cur]);
        for (int i : g[cur]) if (--idg[i] == 0) que.push(i);
    }
}


void sol() {
    for (int i = 0; i < MAX; i++) {
        g[i].clear(), rg[i].clear(); dst[i] = 0, idg[i] = 0, dp[i] = 0;
    }
    int a, b;
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) cin >> dst[i];
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        g[a].push_back(b), rg[b].push_back(a), idg[b]++;
    }
    cin >> w;
    topologicalSort();
    cout << dp[w] << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}
