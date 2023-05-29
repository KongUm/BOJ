#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, d, res = 0;
vector<pii> v;
priority_queue<int, vector<int>, greater<int>> pq;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b; cin >> n;
    for (int i = 0; i < n; i++) cin >> a >> b, v.push_back({ max(a, b), min(a, b) });
    cin >> d;
    sort(all(v));

    int idx = 0;
    while (idx < n) {
        int tar = v[idx].fi;
        while (idx < n && v[idx].fi == tar) pq.push(v[idx++].se);
    
        while (!pq.empty() && pq.top() < tar - d) pq.pop();
        res = max(res, (int) pq.size());
    }
    cout << res;
}