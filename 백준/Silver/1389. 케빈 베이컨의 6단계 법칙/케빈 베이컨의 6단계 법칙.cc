#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;
const int MAX = 110, INF = (int) 1e6;
int n, m, dp[MAX][MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b; cin >> n >> m;
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) dp[i][j] = INF;
    }
    for (int i = 1; i < n + 1; i++) dp[i][i] = 0;

    for (int i = 0; i < m; i++) cin >> a >> b, dp[a][b] = 1, dp[b][a] = 1;

    for (int i = 1; i < n + 1; i++) {
        for (int s = 0; s < n + 1; s++) {
            for (int e = 1; e < n + 1; e++) dp[s][e] = min(dp[s][e], dp[s][i] + dp[i][e]); 
        }
    }
    pii res = { 0, INF };
    for (int i = 1; i < n + 1; i++) {
        int tmp = 0;
        for (int j = 1; j < n + 1; j++) tmp += dp[i][j];
        if (res.se > tmp || (res.se == tmp && res.fi > i)) res = { i, tmp };
    }
    cout << res.fi;
}