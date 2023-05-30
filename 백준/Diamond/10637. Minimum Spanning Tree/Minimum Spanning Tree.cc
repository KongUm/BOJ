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
const int MAX = 200010, INF = (int) 1e10;
int n, m, dsu[MAX], mstW = 0;
int sz[MAX], dep[MAX], top[MAX], in[MAX], out[MAX], par[MAX], tIdx[MAX];
bool visited[MAX], isMST[MAX];
vector<pii> graph[MAX], chd[MAX];
vector<pii> v; vector<ti3> edge;

struct Ls { // Lazy Segment Tree
    int segTree[MAX * 4], lazy[MAX * 4];

    void init() {
        for (int i = 0; i < MAX * 4; i++) {
            segTree[i] = INF, lazy[i] = INF;
        }
    }

    void lazyUpdate(int st, int ed, int nd) {
        if (lazy[nd] != INF) {
            segTree[nd] = min(lazy[nd], segTree[nd]);
            if (st != ed) {
                lazy[nd * 2] = min(lazy[nd * 2], lazy[nd]);
                lazy[nd * 2 + 1] = min(lazy[nd * 2 + 1], lazy[nd]); 
            }
            lazy[nd] = INF;
        }
    }

    void update(int st, int ed, int nd, int ul, int ur, int val) {
        lazyUpdate(st, ed, nd);

        if (ur < st || ed < ul) return;

        if (ul <= st && ed <= ur) {
            segTree[nd] = min(segTree[nd], val);
            if (st != ed) {
                lazy[nd * 2] = min(lazy[nd * 2], val);
                lazy[nd * 2 + 1] = min(lazy[nd * 2 + 1], val);
            }
            return;
        }
        int mid = (st + ed) / 2;
        update(st, mid, nd * 2, ul, ur, val);
        update(mid + 1, ed, nd * 2 + 1, ul, ur, val);
        segTree[nd] = min(segTree[nd * 2], segTree[nd * 2 + 1]);
    }
        
    int query(int st, int ed, int nd, int ql, int qr) {
        lazyUpdate(st, ed, nd);

        if (qr < st || ed < ql) return INF;
        if (ql <= st && ed <= qr) return segTree[nd];

        int mid = (st + ed) / 2;
        int l = query(st, mid, nd * 2, ql, qr);
        int r = query(mid + 1, ed, nd * 2 + 1, ql, qr);
        return min(l, r);
    }
} Ls;

// Union-Find

int find(int x) {
    if (dsu[x] != x) dsu[x] = find(dsu[x]);
    return dsu[x];
}

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) dsu[b] = a;
    else dsu[a] = b;
}

// Heavy-Light Decomposition

void dfs0(int cur) {
    visited[cur] = true;
    for (auto nxt : graph[cur]) {
        if (visited[nxt.fi]) continue;
        chd[cur].push_back(nxt);
        dfs0(nxt.fi);
    }
}

void dfs1(int cur) {
    sz[cur] = 1;
    for (pii &nxt : chd[cur]) { // & 
        dep[nxt.fi] = dep[cur] + 1; par[nxt.fi] = cur;
        tIdx[nxt.fi] = nxt.se;
        dfs1(nxt.fi);
        sz[cur] += sz[nxt.fi];
        if (sz[nxt.fi] > sz[chd[cur][0].fi]) swap(nxt, chd[cur][0]);
    } 
}

int dfsNum = 0;
void dfs2(int cur) {
    in[cur] = ++dfsNum;
    for (pii nxt : chd[cur]) {
        if (nxt.fi == chd[cur][0].fi) top[nxt.fi] = top[cur];
        else top[nxt.fi] = nxt.fi;
        dfs2(nxt.fi);
    }
    out[cur] = dfsNum;
}

void update(int a, int b, int w) {
    while (top[a] != top[b]) {
        if (dep[top[a]] < dep[top[b]]) swap(a, b);
        Ls.update(1, MAX, 1, in[top[a]], in[a], w);
        a = par[top[a]];
    } 
    // 같은 체인이라면 dfs ordering이 연속 됨.
    if (dep[a] > dep[b]) swap(a, b);
    Ls.update(1, MAX, 1, in[a] + 1, in[b], w);
}

int query(int a) {
    return Ls.query(1, MAX, 1, in[a], in[a]);
}

// Main

void input() {
    int a, b, w;
    cin >> n >> m;
    for (int i = 0; i < m; i++) { // idx = 0부터
        cin >> a >> b >> w;
        edge.push_back({ a, b, w });
        v.push_back({ w, i });
    }
    sort(all(v));
}

bool buildSpnningTree() {
    for (int i = 0; i < MAX; i++) dsu[i] = i;

    for (auto p : v) {
        int w = p.fi, idx = p.se;
        int a = get<0>(edge[idx]), b = get<1>(edge[idx]);
        if (find(a) != find(b)) {
            uni(a, b);
            mstW += w; isMST[idx] = true;
            graph[a].push_back({ b, idx });
            graph[b].push_back({ a, idx });
        }
    }
    bool flag = true;
    for (int i = 0; i < n + 1; i++) find(i);

    for (int i = 1; i < n + 1; i++) if (dsu[1] != dsu[i]) flag = false;
    if (!flag) for (int i = 0; i < m; i++) cout << -1 << "\n";
    return flag;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    input();
    if (!buildSpnningTree()) return 0;
    dfs0(1), dfs1(1), dfs2(1);
    Ls.init();

    for (int i = 0; i < m; i++) {
        int a = get<0>(edge[i]), b = get<1>(edge[i]), w = get<2>(edge[i]);
        if (isMST[i] == false) update(a, b, w);
    }

    for (int i = 0; i < m; i++) {
        int a = get<0>(edge[i]), b = get<1>(edge[i]), w = get<2>(edge[i]);
        if (isMST[i]) {
            if (dep[a] < dep[b]) swap(a, b); // a가 무조건 더 깊음
            int res = query(a), bf = get<2>(edge[tIdx[a]]);
            if (res >= INF) cout << -1 << "\n";
            else cout << mstW - bf + res << "\n";
        }
        else cout << mstW << "\n";
    }
}