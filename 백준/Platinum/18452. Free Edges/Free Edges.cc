#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, m, dsu[MAX], sz[MAX], edgeCnt[MAX], res;
vector<pii> edge;

int find(int x) { 
    if (dsu[x] != x) return dsu[x] = find(dsu[x]);
    return dsu[x];
}

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) dsu[b] = a, sz[a] += sz[b];
    else dsu[a] = b, sz[b] += sz[a];
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int a, b;
    for (int i = 0; i < MAX; i++) sz[i] = 1, dsu[i] = i;
    for (int i = 0; i < m; i++) {
        cin >> a >> b; 
        edge.push_back({ a, b });
        if (find(a) != find(b)) uni(a, b);
    }

    for (pii p : edge) edgeCnt[find(p.fi)]++;
    for (int i = 1; i < n + 1; i++) res += max(edgeCnt[i] - (sz[i] - 1), 0LL);
    cout << res;
}