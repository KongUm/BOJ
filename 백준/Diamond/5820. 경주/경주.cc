#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 200010, INF = (int) 1e9 + 7;
int n, k, sz[MAX], cPar[MAX], visited[MAX], ans = INF;
vector<pii> g[MAX];
map<int, int> mp, tmp;

void input() {
    int a, b, w; cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a >> b >> w;
        g[a].push_back({ b, w }); g[b].push_back({ a, w });
    }
}

int getSize(int cur, int p) {
    sz[cur] = 1;
    for (pii nxt: g[cur]) {
        if (nxt.fi != p && !visited[nxt.fi]) sz[cur] += getSize(nxt.fi, cur);
    }
    return sz[cur];
}

int getCentroid(int cur, int p, int cap) {
    for (pii nxt: g[cur]) {
        if (nxt.fi != p && !visited[nxt.fi] && sz[nxt.fi] * 2 > cap) {
            return getCentroid(nxt.fi, cur, cap);
        }
    }   
    return cur;
}

void dfs(int cur, int p, int length, int edgeCnt) {
    if (tmp.find(length) == tmp.end()) tmp.insert({ length, edgeCnt });
    tmp[length] = min(tmp[length], edgeCnt);

    for (pii nxt: g[cur]) {
        if (nxt.fi != p && !visited[nxt.fi]) {
            dfs(nxt.fi, cur, length + nxt.se, edgeCnt + 1);
        }
    }
}

void buildTree(int cur, int p) {
    int ctr = getCentroid(cur, -1, getSize(cur, -1));
    
    mp.clear(); mp.insert({ 0, 0 });
    for (pii i: g[ctr]) {
        tmp.clear();
        if (!visited[i.fi]) dfs(i.fi, ctr, i.se, 1);
        for (pii j : tmp) {
            if (mp.find(k - j.fi) != mp.end()) ans = min(ans, mp[k - j.fi] + j.se);
        }
        for (pii j : tmp) {
            if (mp.find(j.fi) == mp.end()) mp.insert(j);
            mp[j.fi] = min(mp[j.fi], j.se);
        }
    }

    cPar[ctr] = p, visited[ctr] = true;
    for (pii nxt: g[ctr]) {
        if (!visited[nxt.fi]) buildTree(nxt.fi, ctr);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    input();
    buildTree(0, -1);
    if (ans == INF) ans = -1;
    cout << ans;
}
