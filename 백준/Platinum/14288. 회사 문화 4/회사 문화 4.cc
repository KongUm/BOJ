#include <bits/stdc++.h>

using namespace std;

const int N = 100010;
int n, m, cnt, segTree[2][N]; // t = 0 부하직원 방향; t == 1 상사 방향
vector<int> graph[N];
pair<int, int> ett[N];

void dfs(int s) {
    ett[s].first = ++cnt;
    for (int node: graph[s]) dfs(node);
    ett[s].second = cnt;
}

void update(int i, int value, int t) {
    while (i < N) {
        segTree[t][i] += value;
        i += (i & -i);
    }
}

int query(int i, int t) {
    int ans = 0;
    while (i > 0) {
        ans += segTree[t][i];
        i -= (i & -i);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b, temp, t;
    t = 0;

    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) {
        cin >> temp;
        graph[temp].push_back(i);
    }
    dfs(1);

    for (int i = 0; i < m; i++) {
        cin >> q;
        if (q == 1) {
            cin >> a >> b;
            if (t == 0) {
                update(ett[a].first, b, t);
                update(ett[a].second + 1, -b, t);
            } else update(ett[a].first, b, t);

        } else if (q == 2) {
            cin >> a;
            cout << query(ett[a].first, 0) + query(ett[a].second, 1) - query(ett[a].first - 1, 1) << "\n";
        } else t = 1 - t;
    }
}