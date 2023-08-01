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
const int MAX = 200010;
int n, m, arr[MAX], id[MAX];
pii crd[MAX];
vector<pii> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, w;
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> a >> b, v.push_back({ b, i + 1 });
    sort(all(v));
    int idx = 1;
    id[v[0].se] = 1;
    for (int i = 1; i < n; i++) {
        if (v[i - 1].fi != v[i].fi) idx++;
        id[v[i].se] = idx;
    }

    for (int i = 0; i < m; i++) {
        cin >> a >> b >> w;
        if (id[a] > id[b]) swap(a, b);
        if (id[a] == id[b]) arr[id[a]] += w, arr[id[a] + 1] -= w;
        else arr[id[a]] += w, arr[id[b] + 1] -= w;
    }

    for (int i = 1; i < n + 5; i++) arr[i] += arr[i - 1];
    cout << *max_element(arr, arr + n + 5);
}