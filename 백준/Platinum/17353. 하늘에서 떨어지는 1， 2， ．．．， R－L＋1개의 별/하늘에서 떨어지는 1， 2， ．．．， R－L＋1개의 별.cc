#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int N = 100010;
int n, m;
ll segTree[N * 4], lazy[N * 4], A[N], arr[N];

ll init(int start, int end, int node) {
    if (start == end) return segTree[node] = arr[start];
    int mid = (start + end) / 2;
    return segTree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

void update_lazy(int start, int end, int node) {
    if (lazy[node] != 0) {
        segTree[node] += (end - start + 1) * lazy[node];
        if (start != end) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int start, int end, int node, int ul, int ur, int value) {
    update_lazy(start, end, node);

    if (ur < start || ul > end) return;
    if (ul <= start && end <= ur) {
        segTree[node] += (end - start + 1) * value;
        if (start != end) {
            lazy[node * 2] += value;
            lazy[node * 2 + 1] += value;
        }
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, ul, ur, value);
    update(mid + 1, end, node * 2 + 1, ul, ur, value);
    segTree[node] = segTree[node * 2] + segTree[node * 2 + 1];
}

ll query(int start, int end, int node, int fl, int fr) {
    update_lazy(start, end, node);

    if (fr < start || fl > end) return 0;
    if (fl <= start && end <= fr) return segTree[node];

    int mid = (start + end) / 2;
    return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> A[i];
    for (int i = 1; i < n + 1; i++) arr[i] = A[i] - A[i - 1];

    init(1, n, 1);
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> q >> a;
        if (q == 1) {
            cin >> b;
            update(1, n, 1, a, b, 1);
            update(1, n, 1, b + 1, b + 1, (b - a + 1) * (-1));
        } else cout << query(1, n, 1, 1, a) << "\n";
    }
}