#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int N = 100001;
int n, m;
ll arr[N];
pair<ll, int> segTree[N * 4];

pair<ll, int> init(int start, int end, int node) {
    if (start == end) {
        segTree[node] = make_pair(arr[start], start);
        return segTree[node];
    }
    int mid = (start + end) / 2;
    pair<ll, int> l = init(start, mid, node * 2);
    pair<ll, int> r = init(mid + 1, end, node * 2 + 1);
    if (l.first >= r.first) segTree[node] = l;
    else segTree[node] = segTree[node] = r;

    return segTree[node];
}

void update(int start, int end, int node, int idx, ll value) {
    if (idx < start || idx > end) return;
    if (start == end) {
        segTree[node].first = value;
        return;
    }
    int mid = (start + end) / 2;
    update(start, mid, node * 2, idx, value);
    update(mid + 1, end, node * 2 + 1, idx, value);

    if (segTree[node * 2].first >= segTree[node * 2 + 1].first) segTree[node] = segTree[node * 2];
    else segTree[node] = segTree[node * 2 + 1];

}

pair<ll, int> query(int start, int end, int node, int fl, int fr) {
    if (fr < start || fl > end) return make_pair(0, 0);
    if (fl <= start && end <= fr) {
        return segTree[node];
    }

    int mid = (start + end) / 2;
    pair<ll, int> l = query(start, mid, node * 2, fl, fr);
    pair<ll, int> r = query(mid + 1, end, node * 2 + 1, fl, fr);
    if (l.first >= r.first) return l;
    else return r;
}


int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a;
    ll b;
    pair<ll, int> m1, m2, m3;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    cin >> m;
    init(1, n, 1);

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 1) update(1, n, 1, a, b);
        else {
            m1 = query(1, n, 1, a, (int) b);
            m2 = query(1, n, 1, a, m1.second - 1);
            m3 = query(1, n, 1, m1.second + 1, (int) b);

            cout << m1.first + max(m2.first, m3.first) << "\n";
        }
    }
}