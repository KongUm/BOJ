#include <bits/stdc++.h>
#include <fstream>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 30010;
int n, m, arr[MAX], parent[MAX];
int sz[MAX], dep[MAX], par[MAX], top[MAX], in[MAX], out[MAX];
vector<int> ans, graph[MAX], chd[MAX];
vector<ti3> inp;

struct Seg{
    int segTree[MAX * 4];
    
    void update(int st, int ed, int nd, int tar, int val) {
        if (tar < st || tar > ed) return;
        if (st == ed) {
            segTree[nd] = val;
            return;
        }
        int mid = (st + ed) / 2;
        update(st, mid, nd * 2, tar, val);
        update(mid + 1, ed, nd * 2 + 1, tar, val);
        segTree[nd] = segTree[nd * 2] + segTree[nd * 2 + 1];
    } 

    int query(int st, int ed, int nd, int fl, int fr) {
        if (fr < st || ed < fl) return 0;
        if (fl <= st && ed <= fr) return segTree[nd];

        int mid = (st + ed) / 2;
        int l = query(st, mid, nd * 2, fl, fr);
        int r = query(mid + 1, ed, nd * 2 + 1, fl, fr);
        return l + r;
    }
}seg;

int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

bool visited[MAX];
void dfs(int s) { // chd
    visited[s] = true;
    for (int i : graph[s]) {
        if (visited[i]) continue;
        chd[s].push_back(i); 
        dfs(i);
    }
}

void dfs1(int s) { // sz, par, dep & chd 정렬
    sz[s] = 1; 
    for (int &i : chd[s]) { // i는 참조자
        dep[i] = dep[s] + 1; par[i] = s;
        dfs1(i); 
        sz[s] += sz[i];
        if (sz[i] > sz[chd[s][0]]) swap(i, chd[s][0]);
    }
}

int dn;
void dfs2(int s) { //top, DFS ordering
    in[s] = ++dn;
    for (int i : chd[s]) {
        if (i == chd[s][0]) top[i] = top[s];
        else top[i] = i;
        dfs2(i);
    }
    out[s] = dn;
}

void update(int a, int x) {
    seg.update(1, MAX, 1, in[a], x);
} 

int query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) {
        if (dep[top[a]] < dep[top[b]]) swap(a, b);
        ret += seg.query(1, MAX, 1, in[top[a]], in[a]);
        a = par[top[a]];
    }
    if (dep[a] > dep[b]) swap(a, b);
    ret += seg.query(1, MAX, 1, in[a], in[b]);
    return ret;
}

void input() {
    string s; int q, a, b;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    cin >> m;
    
    for (int i = 0; i < m; i++) {
        cin >> s >> a >> b;
        if (s == "bridge") {
            q = 0;
            if (find(a) != find(b)) {
                uni(a, b);
                graph[a].push_back(b);
                graph[b].push_back(a);
            }
        }
        else if (s == "penguins") q = 1;
        else q = 2;
        inp.push_back({ q, a, b });
    }

    for (int i = 1; i < n + 1; i++) {
        if (find(i) != 1) {
            uni(1, i);
            graph[1].push_back(i);
            graph[i].push_back(1);
        }
    }
}

void sol() {
    int q, a, b;
    for (int i = 1; i < n + 1; i++) update(i, arr[i]);
    for (int i = 0; i < MAX; i++) parent[i] = i;
    for (int i = 0; i < m; i++) {
        ti3 p = inp[i]; 
        q = get<0>(p), a = get<1>(p), b = get<2>(p);  
        if (q == 0) {
            if (find(a) != find(b)) {
                uni(a, b); 
                cout << "yes" << "\n";
            }
            else cout << "no" << "\n"; 
        }     
        else if (q == 1) update(a, b);
        else {
            if (find(a) != find(b)) cout << "impossible" << "\n";
            else cout << query(a, b) << "\n";
        }
    }
}
 
signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    for (int i = 0; i < MAX; i++) parent[i] = i;
    

    input(); dfs(1); dfs1(1); dfs2(1);
    sol();
}

    