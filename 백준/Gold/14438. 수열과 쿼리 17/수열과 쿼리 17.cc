#include <bits/stdc++.h>

#define int long long
using namespace std;

const int N = 100001;
int n, m, segTree[N * 4], arr[N];

int init(int start, int end, int node) {
    if (start == end) return segTree[node] = arr[start];
    int mid = (start + end) / 2;
    return segTree[node] = min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1));
}

void update(int start, int end, int node, int index, int value) {
    if (index < start || index > end) return;
    if (start == end) {
        segTree[node] = value;
        return;
    }
    int mid = (start + end) / 2;
    update(start, mid, node * 2, index, value);
    update(mid + 1, end, node * 2 + 1, index, value);
    segTree[node] = min(segTree[node * 2], segTree[node * 2 + 1]);
}

int query(int start, int end, int node, int fl, int fr) {
    if (fr < start || fl > end) return (int) 1e10;
    if (fl <= start && end <= fr) return segTree[node];

    int mid = (start + end) / 2;
    int l = query(start, mid, node * 2, fl, fr);
    int r = query(mid + 1, end, node * 2 + 1, fl, fr);
    return min(l, r);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    init(1, n, 1);
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 1) update(1, n, 1, a, b);
        else cout << query(1, n, 1, a, b) << "\n";
    }
    return 0;
}