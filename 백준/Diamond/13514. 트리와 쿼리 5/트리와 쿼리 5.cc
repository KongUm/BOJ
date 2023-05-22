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
const int MAX = 100010, INF = (int) 1e9 + 7;
int n, m;
int treeSz[MAX], cPar[MAX], visited[MAX], color[MAX], dep[MAX], ty[MAX];
int spTable[MAX][22];
vector<int> graph[MAX], cTree[MAX]; 
priority_queue<pii, vector<pii>, greater<pii>> pq[MAX];

void buildSparseTable() {
    for (int j = 1; j < 22; j++) {
        for (int i = 1; i < n + 1; i++) spTable[i][j] = spTable[spTable[i][j - 1]][j - 1];
    }
}

int getLca(int a, int b) {
    if (dep[a] > dep[b]) swap(a, b);
    int diff = abs(dep[b] - dep[a]);
    for (int i = 0; diff; i++) {
        if (diff & 1) b = spTable[b][i];
        diff >>= 1;
    }
    if (a == b) return a;
    for (int i = 21; i > -1; i--) {
        if (spTable[a][i] != spTable[b][i]) a = spTable[a][i], b = spTable[b][i];
    }
    return spTable[a][0];
}

int getDist(int a, int b) {
    return dep[a] + dep[b] - 2 * dep[getLca(a, b)];
}

void dfs(int cur, int pr, int d) {
    treeSz[cur] = 1; dep[cur] = d;
    for (int nxt : graph[cur]) {
        if (nxt != pr) spTable[nxt][0] = cur, dfs(nxt, cur, d + 1);
    }
}


int getSize(int cur, int pr) {
    treeSz[cur] = 1;
    for (int nxt : graph[cur]) {
        if (nxt != pr && !visited[nxt]) treeSz[cur] += getSize(nxt, cur);
    }
    return treeSz[cur];
}

int getCentroid(int cur, int pr, int cap) {
    for (int nxt : graph[cur]) {
        if (nxt != pr && !visited[nxt] && treeSz[nxt] * 2 > cap) {
            return getCentroid(nxt, cur, cap);
        }
    }
    return cur;
}

int buildTree(int cur, int pr) {
    int ctr = getCentroid(cur, -1, getSize(cur, -1));
    cPar[ctr] = pr, visited[ctr] = true; 
    for (int nxt : graph[ctr]) {
        if (!visited[nxt]) {
            int to = buildTree(nxt, ctr);
            cTree[to].push_back(ctr); cTree[ctr].push_back(to);
        }
    }
    return ctr;
}

void update(int cur, int s) {
    pq[cur].push({ getDist(cur, s), s }); 
    if (cPar[cur] > 0) return update(cPar[cur], s);
}

void query(int cur, int s, int &res) {
    while (pq[cur].size() > 0) {
        if (color[pq[cur].top().se]) break;
        pq[cur].pop();
    }

    if (pq[cur].size() > 0) res = min(res, getDist(cur, s) + pq[cur].top().fi);
    
    if (cPar[cur] > 0) return query(cPar[cur], s, res);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, a, b; cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(1, -1, 1);
    buildTree(1, -1); spTable[1][0] = 1; buildSparseTable();
    
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> q >> a;
        if (q == 1) color[a] ^= 1, update(a, a);
        else {
            int res = INF; query(a, a, res);
            if (res == INF) res = -1;
            cout << res << "\n";
        }
    }
}