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
const int MAX = 100010;
int n, m, r, vis[MAX], cnt;
vector<int> graph[MAX];
queue<int> que;

void dfs(int cur) {
    vis[cur] = ++cnt;
    for (int nxt : graph[cur]) {
        if (vis[nxt]) continue;
        dfs(nxt);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n >> m >> r;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a].push_back(b), graph[b].push_back(a);
    }

    for (int i = 1; i < n + 1; i++) sort(all(graph[i]));
    dfs(r);
    for (int i = 1; i < n + 1; i++) cout << vis[i] << " ";
}