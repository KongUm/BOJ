#include <bits/stdc++.h>

using namespace std;

const int N = 100001;
int n, m, segTree[N * 4], lazy[N * 4];

void update_lazy(int start, int end, int node) {
    if (lazy[node] != 0) {
        if (lazy[node] % 2 == 1) segTree[node] = (end - start + 1) - segTree[node];
        if (start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int start, int end, int node, int ul, int ur) {
    update_lazy(start, end, node);

    if (ur < start || ul > end) return;

    if (ul <= start && end <= ur) {
        segTree[node] = (end - start + 1) - segTree[node];
        if (start != end) {
            lazy[node * 2] += 1;
            lazy[node * 2 + 1] += 1;
        }
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, ul, ur);
    update(mid + 1, end, node * 2 + 1, ul, ur);
    segTree[node] = segTree[node * 2] + segTree[node * 2 + 1];
}

int query(int start, int end, int node, int fl, int fr) {
    update_lazy(start, end, node);

    if (fr < start || fl > end) return 0;
    if (fl <= start && fr >= end) return segTree[node];

    int mid = (start + end) / 2;
    return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 0) update(1, n, 1, a, b);
        else cout << query(1, n, 1, a, b) << "\n";
    }
}