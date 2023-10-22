#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, cnt, arr[MAX];
vector<pii> g[MAX]; 

void dfs(int cur, int par, int d, int chk) {
    if (d > arr[cur] || chk == 1) cnt++, chk = 1;
    
    for (pii nxt : g[cur]) {
        if (nxt.fi == par) continue;
        dfs(nxt.fi, cur, d + nxt.se, chk);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];

    for (int i = 2; i < n + 1; i++) {
        cin >> a >> b;
        g[i].push_back({ a, b }), g[a].push_back({ i, b });
    }
    dfs(1, -1, 0, 0);
    cout << cnt;
}