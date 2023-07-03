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
const int MAX = 2510;
int n, a, dsu[MAX];
vector<pii> g;

struct ds { int d, a, b; };
vector<ds> v;

bool cmp (ds a, ds b) {
    return (a.d < b.d);
}

int find(int x) {
    if (dsu[x] != x) return dsu[x] = find(dsu[x]);
    return dsu[x];
}

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) dsu[b] = a;
    else dsu[a] = b;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    for (int i = 0; i < MAX; i++) dsu[i] = i;
    cin >> n;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            cin >> a;
            if (i < j) v.push_back({ a, i, j });
        }
    }

    sort(all(v), cmp);
    
    for (auto p : v) {
        if (find(p.a) == find(p.b)) continue;
        uni(p.a, p.b);
        g.push_back({ p.a, p.b });
    }

    for (auto p : g) cout << p.fi << " " << p.se << "\n";
}