#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()

using namespace std;
using pii = pair<int, int>;
const int MAX = 1010;
int n, m, vis[MAX][MAX];
char arr[MAX][MAX];
pii st;

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

int bfs(int sy, int sx) {
    queue<pii> que; int ret = 0;
    vis[sy][sx] = 1, que.push({ sy, sx });

    while (!que.empty()) {
        auto p = que.front(); que.pop();
        if (arr[p.fi][p.se] == 'P') ret++;

        for (int i = 0; i < 4; i++) {
            int ny = p.fi + dy[i], nx = p.se + dx[i];
            if (ny < 0 || ny >= n || nx < 0 || nx >= m || vis[ny][nx] != 0 || arr[ny][nx] == 'X') continue;
            vis[ny][nx] = 1;
            que.push({ ny, nx });
        }
    }
    return ret;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 'I') st = { i, j };
        }
    }

    int ans = bfs(st.fi, st.se);
    if (ans == 0) cout << "TT" << "\n";
    else cout << ans << "\n";
} 