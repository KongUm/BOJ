#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;
int n, segTree[MAX * 4], ans[MAX];
vector<pii> v;

void update(int st, int ed, int nd, int idx, int val) {   
    if (idx < st || ed < idx) return;
    if (st == ed) { segTree[nd] = val; return; }

    int mid = (st + ed) / 2;
    update(st, mid, nd * 2, idx, val);
    update(mid + 1, ed, nd * 2 + 1, idx, val);
    segTree[nd] = segTree[nd * 2] + segTree[nd * 2 + 1];
}

int query(int st, int ed, int nd, int ql, int qr) {
    if (qr < st || ed < ql) return 0;
    if (ql <= st && ed <= qr) return segTree[nd];

    int mid = (st + ed) / 2;
    int l = query(st, mid, nd * 2, ql, qr);
    int r = query(mid + 1, ed, nd * 2 + 1, ql, qr);
    return l + r;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, bf = 0, cnt = 1, t = 0;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a, v.push_back({ a, i + 1 });
    for (int i = 1; i < n + 1; i++) update(1, n, 1, i, 1); 
    sort(all(v));

    for (auto p : v) {
        if (p.se > bf) t += query(1, n, 1, bf, p.se);
        else {
            t += query(1, n, 1, bf, n) + query(1, n, 1, 1, p.se);
            cnt++;
        }
        int r = p.fi - cnt;
        t += query(1, n, 1, 1, n) * r;
        cnt += r;
        ans[p.se] = t;
        update(1, n, 1, p.se, 0);
        bf = p.se;
    }
    
    for (int i = 1; i < n + 1; i++) cout << ans[i] << "\n";
}