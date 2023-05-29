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
using ti4 = tuple<int, int, int, int>;
const int MAX = 100010;
int n, m;
int sz[MAX], in[MAX], out[MAX], par[MAX], top[MAX], dep[MAX];
vector<int> graph[MAX], chd[MAX];
vector<pii> ty;
vector<ti4> qry; 

struct Seg { // Segment Tree
    int segTree[MAX * 4];

    void update(int st, int ed, int nd, int idx, int val) {   
        if (idx < st || ed < idx) return;
        
        if (st == ed) { segTree[nd] = val; return; }
        int mid = (st + ed) / 2;
        update(st, mid, nd * 2, idx, val), update(mid + 1, ed, nd * 2 + 1, idx, val);
        segTree[nd] = max(segTree[nd * 2], segTree[nd * 2 + 1]);
    }
        
    int query(int st, int ed, int nd, int ql, int qr) {
        if (qr < st || ed < ql) return 0;
        if (ql <= st && ed <= qr) return segTree[nd];

        int mid = (st + ed) / 2;
        return max(query(st, mid, nd * 2, ql, qr), query(mid + 1, ed, nd * 2 + 1, ql, qr));
    }
} seg;

bool visited[MAX];
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

void update(int a, int val) {
    seg.update(1, MAX, 1, in[a], val);
}

int query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) {
        if (dep[top[a]] < dep[top[b]]) swap(a, b);
        // 1. a와 b는 서로 다른 Chain에 위치 
        // 2. 깊이가 낮은 쪽에서 위로 올라가야함 -> 올라가는 걸 a로 고정하기 위해 swap

        ret = max(ret, seg.query(1, MAX, 1, in[top[a]], in[a]));
        a = par[top[a]];
        // a가 위치한 Chain의 값을 처리하고 올라감 (a ~ top[a])
    }
    if (dep[a] > dep[b]) swap(a, b);
    ret = max(ret, seg.query(1, MAX, 1, in[a], in[b]));
    return ret;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, c, qi, ans[MAX];
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) cin >> a, ty.push_back({ a, i });    
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        graph[a].push_back(b), graph[b].push_back(a);
    }

    for (int i = 0; i < m; i++) cin >> a >> b >> c, qry.push_back({ c, a, b, i });
    sort(all(ty)); sort(all(qry));
    
    dfs(1), dfs1(1), dfs2(1);
    int idx = 0;
    for (int i = 0; i < m; i++) {
        a = get<1>(qry[i]), b = get<2>(qry[i]), c = get<0>(qry[i]), qi = get<3>(qry[i]);
        while (idx < n && ty[idx].fi <= c) update(ty[idx].se, ty[idx].fi), idx++;
        int res = query(a, b);
        ans[qi] = (c == res);
    }
    for (int i = 0; i < m; i++) cout << ans[i];
}