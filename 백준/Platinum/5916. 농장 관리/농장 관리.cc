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
int n, m, sz[MAX], dep[MAX], top[MAX], in[MAX], out[MAX], par[MAX], visited[MAX];
vector<int> chd[MAX], graph[MAX];

struct Ls { // Lazy Segment Tree
    int segTree[MAX * 4], lazy[MAX * 4];
    // dfs ordering 기준 + 각 정점의 부모와 연결하는 간선의 가중치를 의미

    void lazyUpdate(int st, int ed, int nd) {
        if (lazy[nd] != 0) {
            segTree[nd] += (ed - st + 1) * lazy[nd];
            if (st != ed) {
                lazy[nd * 2] += lazy[nd];
                lazy[nd * 2 + 1] += lazy[nd]; 
            }
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
} Ls;

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

void update(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) {
        if (dep[top[a]] < dep[top[b]]) swap(a, b);
        Ls.update(1, MAX, 1, in[top[a]], in[a], 1);
        a = par[top[a]];
    } 
    // 같은 체인이라면 dfs ordering이 연속 됨.
    if (dep[a] > dep[b]) swap(a, b);
    Ls.update(1, MAX, 1, in[a] + 1, in[b], 1);
}

int query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) { // a와 b가 같은 체인이 될때까지 반복
        if (dep[top[a]] < dep[top[b]]) swap(a, b); // dep[top[a]] > dep[top[b]]가 되도록 바꿔줌
        ret = max(ret, Ls.query(1, MAX, 1, in[top[a]], in[a]));
        // 정점 a가 속해있는 체인의 top부터 a까지 쿼리 처리
        a = par[top[a]]; // a가 속해있는 체인의 top의 부모로 올려줌 (Light-Edge를 타고 감) 
    }
    if (dep[a] > dep[b]) swap(a, b);
    // dep[a] <= dep[b]가 되도록 변경 (즉 a노드가 더 상위 노드가 되도록)
    ret = max(ret, Ls.query(1, MAX, 1, in[a] + 1, in[b]));
    return ret;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int a, b; char q;
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        graph[a].push_back(b), graph[b].push_back(a);
    }
    dfs(1); dfs1(1); dfs2(1);

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 'P') update(a, b);
        else cout << query(a, b) << "\n";
    }
}