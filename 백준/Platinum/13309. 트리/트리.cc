#include <bits/stdc++.h>
#define fi first
#define se second

using namespace std;
using pii = pair<int, int>;
const int MAX = 200010;
int n, m, sz[MAX], dep[MAX], top[MAX], in[MAX], out[MAX], par[MAX], visited[MAX];
vector<int> chd[MAX], graph[MAX];

struct Seg {
    int segTree[MAX * 4];

    void update(int st, int ed, int nd, int idx, int val) {
        if (idx < st || ed < idx) return;
        if (st == ed) { segTree[nd] = val; return; }

        int mid = (st + ed) / 2;
        update(st, mid, nd * 2, idx, val), update(mid + 1, ed, nd * 2 + 1, idx, val);
        segTree[nd] = segTree[nd * 2] + segTree[nd * 2 + 1];
    }
        
    int query(int st, int ed, int nd, int ql, int qr) {

        if (qr < st || ed < ql) return 0;
        if (ql <= st && ed <= qr) return segTree[nd];

        int mid = (st + ed) / 2;
        return query(st, mid, nd * 2, ql, qr) + query(mid + 1, ed, nd * 2 + 1, ql, qr);
    }
} seg;

void dfs(int cur) {
    visited[cur] = true;
    for (int nxt : graph[cur]) {
        if (visited[nxt]) continue;
        chd[cur].push_back(nxt);
        dfs(nxt);
    }
}

void dfs1(int cur) {
    sz[cur] = 1;
    for (int &nxt : chd[cur]) { // & 
        dep[nxt] = dep[cur] + 1; par[nxt] = cur;
        dfs1(nxt);
        sz[cur] += sz[nxt];
        if (sz[nxt] > sz[chd[cur][0]]) swap(nxt, chd[cur][0]);
    } 
}

int dfsNum = 0;
void dfs2(int cur) {
    in[cur] = ++dfsNum;
    for (int nxt : chd[cur]) {
        if (nxt == chd[cur][0]) top[nxt] = top[cur];
        else top[nxt] = nxt;
        dfs2(nxt);
    }
    out[cur] = dfsNum;
}

void update(int a) {
seg.update(1, MAX, 1, in[a], 1);
}

int query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) { 
        if (dep[top[a]] < dep[top[b]]) swap(a, b); 
        ret = max(ret, seg.query(1, MAX, 1, in[top[a]], in[a]));
        a = par[top[a]];
    }
    if (dep[a] > dep[b]) swap(a, b);
    ret = max(ret, seg.query(1, MAX, 1, in[a] + 1, in[b]));
    return ret;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int q, a, b;
    for (int i = 2; i < n + 1; i++) {
        cin >> a;
        graph[i].push_back(a), graph[a].push_back(i);
    }
    dfs(1); dfs1(1); dfs2(1);

    for (int i = 0; i < m; i++) {
        cin >> a >> b >> q;
        int res = query(a, b);

        if (q == 1) {
            if (res == 0) update(a);
            else update(b);
        }
        if (res == 0) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
}