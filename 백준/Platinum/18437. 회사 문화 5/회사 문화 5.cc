#include <bits/stdc++.h>

using namespace std;

const int N = 100001;
int n, m, cnt, segTree[N * 4], lazy[N * 4];
pair<int, int> ett[N];
vector<int> graph[N];

void dfs(int s) {
    ett[s].first = ++cnt;
    for (int node: graph[s]) dfs(node);
    ett[s].second = cnt;
}

int init(int start, int end, int node) {
    if (start == end) return segTree[node] = 1;
    int mid = (start + end) / 2;
    segTree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
    return segTree[node];
}

void update_lazy(int start, int end, int node) {
    if (lazy[node] != 0) {
        if (lazy[node] == 1) segTree[node] = (end - start + 1);
        else segTree[node] = 0;

        if (start != end) {
            lazy[node * 2] = lazy[node];
            lazy[node * 2 + 1] = lazy[node];
        }
        lazy[node] = 0;
    }
}
// 0 = 현상 유지, 1 = 켜기, 2 = 끄기

void update(int start, int end, int node, int ul, int ur, int value) {
    update_lazy(start, end, node);

    if (ur < start || ul > end) return;
    if (ul <= start && end <= ur) {
        if (value == 1) segTree[node] = (end - start + 1);
        else segTree[node] = 0;

        if (start != end) {
            lazy[node * 2] = value;
            lazy[node * 2 + 1] = value;
        }
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, ul, ur, value);
    update(mid + 1, end, node * 2 + 1, ul, ur, value);
    segTree[node] = segTree[node * 2] + segTree[node * 2 + 1];
}

int query(int start, int end, int node, int fl, int fr) {
    update_lazy(start, end, node);

    if (fr < start || fl > end) return 0;
    if (fl <= start && end <= fr) return segTree[node];

    int mid = (start + end) / 2;
    return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, temp;
    cin >> n;
    for (int i = 1; i < n + 1; i++) {
        cin >> temp;
        graph[temp].push_back(i);
    }
    dfs(1);
    init(1, n, 1);
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> q >> a;
        if (q != 3) update(1, n, 1, ett[a].first + 1, ett[a].second, q);
        else cout << query(1, n, 1, ett[a].first + 1, ett[a].second) << "\n";
    }
}