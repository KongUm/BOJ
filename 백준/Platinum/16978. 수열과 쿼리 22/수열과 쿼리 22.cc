#include <bits/stdc++.h>

#define int long long
#define ll long long
using namespace std;

const int N = 100010;
ll n, m, segTree[N * 4], lazy[N * 4], arr[N], A[N];
pair<ll, ll> Q[N];
vector<tuple<ll, ll, ll>> v[N];

ll init(int start, int end, int node) {
    if (start == end) return segTree[node] = arr[start];
    int mid = (start + end) / 2;
    return segTree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}


void update(int start, int end, int node, int idx, ll value) {
    if (idx < start || idx > end) return;

    segTree[node] += value;
    if (start == end) return;

    int mid = (start + end) / 2;
    update(start, mid, node * 2, idx, value);
    update(mid + 1, end, node * 2 + 1, idx, value);
}

ll query(int start, int end, int node, int fl, int fr) {
    if (fr < start || fl > end) return 0;

    if (fl <= start && end <= fr) return segTree[node];

    int mid = (start + end) / 2;
    return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    ll q, a, b, c, cnt = 1, qc = 1;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;

        if (q == 1) Q[cnt++] = make_pair(a, b);
        else {
            cin >> c;
            v[a].emplace_back(b, c, qc++);
        }
    }
    init(1, n, 1);
    for (auto &j: v[0]) {
        int ans = query(1, n, 1, get<0>(j), get<1>(j));
        A[get<2>(j)] = ans;
    }

    for (int i = 1; i < m + 1; i++) {
        update(1, n, 1, Q[i].first, Q[i].second - arr[Q[i].first]);
        arr[Q[i].first] = Q[i].second;

        for (auto &j: v[i]) {
            int ans = query(1, n, 1, get<0>(j), get<1>(j));
            A[get<2>(j)] = ans;
        }
    }

    for (int i = 1; i < qc; i++) {
        cout << A[i] << "\n";
    }

}