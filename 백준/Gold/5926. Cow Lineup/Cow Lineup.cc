#include <bits/stdc++.h>
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
int n, ty[100000];
vector<pii> v;
map<int, int> m;

int twoPointer(int s, int c) { // (s, e]
    int res = INT_MAX, cnt = 0;

    for (int i = 0; i < n; i++) {
        int value = v[i].first, cls = v[i].second;
        if (++ty[cls] == 1) cnt++;

        if (cnt == c) res = min(res, v[i].first - v[s].first);

        while (cnt == c && ty[v[s].second] >= 2) {
            ty[v[s].second] -= 1;
            s += 1;
            res = min(res, v[i].first - v[s].first);
        }
    }
    return res;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, ID = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        if (m.find(b) == m.end()) m.insert({b, ID++});
        v.push_back({a, m[b]});
    }

    sort(v.begin(), v.end());
    cout << twoPointer(0, ID);
}