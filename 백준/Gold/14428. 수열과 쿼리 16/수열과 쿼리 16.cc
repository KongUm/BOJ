#include <bits/stdc++.h>

#define MAX 100001
#define int long long
using namespace std;

int arr[MAX];
int tree[MAX * 4];
int idx_tree[MAX * 4];

int init(int start, int end, int node) {
    if (start == end) {
        tree[node] = arr[start];
        idx_tree[node] = start;
        return tree[node];
    }
    int mid = (start + end) / 2;
    int lv, rv;
    lv = init(start, mid, node * 2);
    rv = init(mid + 1, end, node * 2 + 1);

    if (lv <= rv) {
        tree[node] = lv;
        idx_tree[node] = idx_tree[node * 2];
    } else {
        tree[node] = rv;
        idx_tree[node] = idx_tree[node * 2 + 1];
    }

    return tree[node];
}


pair<int, int> find(int start, int end, int node, int fl, int fr) {

    if (fl > end || fr < start) return make_pair((int) 1e9 + 1, end);

    if (fl <= start && end <= fr) return make_pair(tree[node], idx_tree[node]);

    int mid = (start + end) / 2;
    pair<int, int> lp, rp;

    lp = find(start, mid, node * 2, fl, fr);
    rp = find(mid + 1, end, node * 2 + 1, fl, fr);

    if (lp.first <= rp.first) return lp;
    else return rp;
}


void update(int start, int end, int node, int index, int value) {

    if (index < start || index > end) return;

    if (start == end) {
        tree[node] = value;
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, index, value);
    update(mid + 1, end, node * 2 + 1, index, value);

    if (tree[node * 2] <= tree[node * 2 + 1]) {
        tree[node] = tree[node * 2];
        idx_tree[node] = idx_tree[node * 2];
    } else {
        tree[node] = tree[node * 2 + 1];
        idx_tree[node] = idx_tree[node * 2 + 1];
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int n, m;
    cin >> n;
    arr[0] = 0;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    init(1, n, 1);
    cin >> m;

    for (int i = 0; i < m; i++) {
        int q, a, b;
        cin >> q >> a >> b;

        if (q == 1) {
            update(1, n, 1, a, b);
            arr[a] = b;
        } else {
            pair<int, int> p = find(1, n, 1, a, b);
            cout << p.second << "\n";
        }
    }
    return 0;
}