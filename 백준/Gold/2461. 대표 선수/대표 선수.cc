#include <bits/stdc++.h>
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
int n, m, ty[1000];
vector<pii> v;

int twoPointer(int s) { // (s, e]
    int res = INT_MAX, cnt = 0;

    for (int i = 0; i < n * m; i++) {
        int value = v[i].first, cls = v[i].second;
        if (++ty[cls] == 1) cnt++;

        if (cnt == n) res = min(res, v[i].first - v[s].first);

        while (cnt == n && ty[v[s].second] >= 2) {
            ty[v[s].second] -= 1;
            s += 1;
            res = min(res, v[i].first - v[s].first);
            //cout << i << " " << s << " " << v[i].first - v[s].first << "\n";   
        }
    }
    return res;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int temp;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> temp;
            v.push_back({temp, i}); 
        }
    }
    sort(v.begin(), v.end());
    cout << twoPointer(0);
}