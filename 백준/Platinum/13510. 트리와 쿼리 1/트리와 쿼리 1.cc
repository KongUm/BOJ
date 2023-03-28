#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 200010;

int sz[MAX], dep[MAX], par[MAX], top[MAX], in[MAX], out[MAX];
vector<int> chd[MAX];
vector<pii> graph[MAX];
vector<ti3> edge;

struct Seg {
    int segTree[MAX * 4];
    // dfs ordering 기준

    void update(int st, int ed, int nd, int idx, int val) {
        if (idx < st || idx > ed) return;
        if (st == ed) {
            segTree[nd] = val;
            return;
        }
        int mid = (st + ed) / 2;
        update(st, mid, nd * 2, idx, val);
        update(mid + 1, ed, nd * 2 + 1, idx, val);
        segTree[nd] = max(segTree[nd * 2], segTree[nd * 2 + 1]);
    }

    int query(int st, int ed, int nd, int fl, int fr) {
        if (fr < st || ed < fl) return 0;
        if (fl <= st && ed <= fr) return segTree[nd];
        int mid = (st + ed) / 2;
        int l = query(st, mid, nd * 2, fl, fr);
        int r = query(mid + 1, ed, nd * 2 + 1, fl, fr);
        return max(l, r);
    }
}seg;


// sz[i] = i를 루트로 하는 서브트리 크기, dep[i] = i의 깊이
// par[i] = i의 부모 정점, chd[i] = i의 자식 정점들
// top[i] = i가 속한 체인의 가장 위에 있는 정점
// in[i], out[i] = DFS Ordering

bool visited[MAX];
void dfs(int s) { // 자식 노드들 채우기.
    visited[s] = true;
    for (auto p : graph[s]) {
        int i = p.fi;
        if (visited[i]) continue;
        visited[i] = true;
        chd[s].push_back(i);
        dfs(i);
    }
}

void dfs1(int s) {
    sz[s] = 1; // 서브트리는 자기 자신을 포함함
    for (int &i : chd[s]) {
        dep[i] = dep[s] + 1; par[i] = s;
        dfs1(i);
        sz[s] += sz[i];  
        if (sz[i] > sz[chd[s][0]]) swap(i, chd[s][0]); 
        // Heavy-Edge 노드를 chd의 맨처음이 되도록 swap
    }
}

int dfsNum; // DFS ordering number
void dfs2(int s) {
    in[s] = ++dfsNum;
    for (int i : chd[s]) {
        if (i == chd[s][0]) top[i] = top[s];
        // 만약 i가 s의 0번째 자식이라면 같은 체인에 속하므로 top[s]를 물려 받는다.
        else top[i] = i; // 그게 아니라면 i부터 새로 시작하는 체인이다.
        // 루트를 포함하는 체인의 top은 0이다.
        dfs2(i);
    }
    out[s] = dfsNum; 
}

void update(int idx, int w) {
    auto p = edge[idx];
    int a = get<0>(p), b = get<1>(p); 
    if (par[b] == a) swap(a, b); // a가 b의 자식이도록 변경
    seg.update(1, MAX, 1, in[a], w);
}

int query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) { // a와 b가 같은 체인이 될때까지 반복
        if (dep[top[a]] < dep[top[b]]) swap(a, b); // dep[top[a]] > dep[top[b]]가 되도록 바꿔줌 
        ret = max(ret, seg.query(1, MAX, 1, in[top[a]], in[a]));
        // 정점 a가 속해있는 체인의 top부터 a까지 쿼리 처리
        a = par[top[a]]; // a가 속해있는 체인의 top의 부모로 올려줌 (Light-Edge를 타고 감) 
    }
    if (dep[a] > dep[b]) swap(a, b);
    // dep[a] <= dep[b]가 되도록 변경 (즉 a노드가 더 상위 노드가 되도록)
    ret = max(ret, seg.query(1, MAX, 1, in[a] + 1, in[b]));
    return ret;
}

int n, m;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, w, q;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b >> w; // a <-> b (w)
        graph[a].push_back({ b, w });
        graph[b].push_back({ a, w });
        edge.push_back({ a, b, w });
    }
    dfs(1), dfs1(1); dfs2(1);
    cin >> m;
    for (int i = 0; i < n - 1; i++) update(i, get<2>(edge[i])); // segTree init

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 1) update(a - 1, b);
        else cout << query(a, b) << "\n";
    }
}
