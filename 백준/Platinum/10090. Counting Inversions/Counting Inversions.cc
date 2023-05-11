#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'
#define YES cout << "YES" << "\n"
#define NO cout << "NO" << "\n"

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 1000010;
int n, a, res = 0, segTree[MAX * 4];
vector<pii> v;

void update(int st, int ed, int nd, int idx, int df) {
    if (idx < st || idx > ed) return;
    segTree[nd] += df;
    if (st == ed) return;

    int mid = (st + ed) / 2;
    update(st, mid, nd * 2, idx, df);
    update(mid + 1, ed, nd * 2 + 1, idx, df);
}

int query(int st, int ed, int nd, int ql, int qr) {
    if (qr < st || ql > ed) return 0;
    if (ql <= st && ed <= qr) return segTree[nd];

    int mid = (st + ed) / 2;
    int l = query(st, mid, nd * 2, ql, qr);
    int r = query(mid + 1, ed, nd * 2 + 1, ql, qr);
    return l + r;
}

void sol() {
    cin >> n;
    for (int i = 1; i < n + 1; i++) { cin >> a; v.push_back({ a, i }); }
    for (int i = 1; i < n + 1; i++) update(1, n, 1, i, 1);
    sort(all(v));

    for (int i = 0; i < n; i++) {
        update(1, n, 1, v[i].se, -1);
        res += query(1, n, 1, 1, v[i].se);
    }
    cout << res;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    sol();
}