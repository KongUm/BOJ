#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int MAX = 2510;
int n, clk[MAX], visited[MAX];
vector<int> graph[MAX];

void init(int n) {
    for (int i = 0; i < n + 1; i++) visited[i] = -1;
}

int dfs(int node, int root) {
    visited[node] = clk[node] % 12;

    for (int nxt : graph[node]) {
        if (visited[nxt] == -1) {
            clk[node] += dfs(nxt, root);
        }
    }
    clk[node] %= 12;
    int diff = 12 - clk[node];
    if (node != root) clk[node] = 0;

    return diff;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, cnt = 0;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> clk[i];

    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i < n + 1; i++) {
        init(n); dfs(i, i);
        if (clk[i] <= 1) cnt++;
    } 
    cout << cnt;
}   