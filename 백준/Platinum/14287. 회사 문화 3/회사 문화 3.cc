#include <bits/stdc++.h>

using namespace std;
int n, m, segTree[100002], dfs_num[100001];
int cnt = 0;
vector<int> graph[100001]; // 부모 > 자식 그래프
pair<int, int> ett[100001]; // 각 정점을 루트로 하는 서브 트리를 나타 내는 구간을 나타 낸다.

void dfs(int s) {
    dfs_num[s] = ++cnt; // 즉 idx cnt = 정점 s를 나타 낸다.
    ett[s].first = cnt;
    for (int node: graph[s]) {
        dfs(node);
    }
    ett[s].second = cnt;
}

void update(int i, int value) {
    while (i <= 100001) {
        segTree[i] += value;
        i += (i & -i);
    }
}

int query(int i) {
    int ans = 0;
    while (i > 0) {
        ans += segTree[i];
        i -= (i & -i);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b, temp;
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) {
        cin >> temp;
        graph[temp].push_back(i);
    }
    dfs(1);
    for (int &i: segTree) i = 0;

    for (int i = 0; i < m; i++) {
        cin >> q >> a;
        if (q == 1) {
            cin >> b;
            update(dfs_num[a], b);
        } else {
            cout << query(ett[a].second) - query(ett[a].first - 1) << "\n";
        }
    }
}