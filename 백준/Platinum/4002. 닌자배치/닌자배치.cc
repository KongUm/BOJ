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
int n, m, res = 0, par[MAX], cost[MAX], v[MAX], id[MAX], sum[MAX]; 
priority_queue<int> pq[MAX];

void merge(int a, int b) {
    if (pq[id[a]].size() < pq[id[b]].size()) swap(a, b);
    
    while (pq[id[b]].size()) {
        int tmp = pq[id[b]].top(); pq[id[b]].pop();
        pq[id[a]].push(tmp), sum[id[a]] += tmp, sum[id[b]] -= tmp;
    }

    while (sum[id[a]] > m) sum[id[a]] -= pq[id[a]].top(), pq[id[a]].pop();

    id[b] = id[a];
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) cin >> par[i] >> cost[i] >> v[i];
    for (int i = 1; i < n + 1; i++) pq[i].push(cost[i]), id[i] = i, sum[i] = cost[i];

    for (int i = n; i > 0; i--) {
        res = max(res, (int) pq[id[i]].size() * v[i]);
        merge(i, par[i]);
    }   
    cout << res;
}