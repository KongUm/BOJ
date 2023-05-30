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
int n, m, segTree[MAX * 4], lazy[MAX * 4], in[MAX], out[MAX];
vector<int> g[MAX];

int dfsNum = 0;
void dfs(int cur) {
    in[cur] = ++dfsNum;
    for (int nxt : g[cur]) dfs(nxt);
    out[cur] = dfsNum;
}

void lazyUpdate(int st, int ed, int nd) {
    if (lazy[nd] != 0) {
        segTree[nd] += (ed - st + 1) * lazy[nd];
        if (st != ed) lazy[nd * 2] += lazy[nd], lazy[nd * 2 + 1] += lazy[nd];        
        lazy[nd] = 0;
    }
}

void update(int st, int ed, int nd, int ul, int ur, int val) {
    lazyUpdate(st, ed, nd);
    if (ur < st || ed < ul) return;
    if (ul <= st && ed <= ur) {
        segTree[nd] += (ed - st + 1) * val;
        if (st != ed) lazy[nd * 2] += val, lazy[nd * 2 + 1] += val;        
        return;
    }

    int mid = (st + ed) / 2;
    update(st, mid, nd * 2, ul, ur, val), update(mid + 1, ed, nd * 2 + 1, ul, ur, val);
    segTree[nd] = segTree[nd * 2] + segTree[nd * 2 + 1];
}

int query(int st, int ed, int nd, int ql, int qr) {
    lazyUpdate(st, ed, nd);
    if (qr < st || ed < ql) return 0;
    if (ql <= st && ed <= qr) return segTree[nd];

    int mid = (st + ed) / 2;
    return query(st, mid, nd * 2, ql, qr) + query(mid + 1, ed, nd * 2 + 1, ql, qr);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b;
    cin >> n >> m >> a; 
    for (int i = 2; i < n + 1; i++) cin >> a, g[a].push_back(i);
    dfs(1);

    for (int i = 0; i < m; i++) {
        cin >> q >> a;
        if (q == 1) {
            cin >> b;
            update(1, n, 1, in[a], out[a], b);
        }
        else cout << query(1, n, 1, in[a], in[a]) << "\n";
    }
}