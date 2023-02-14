#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 3010;
int n;
int Lsum[MAX], Rsum[MAX], Asum[MAX], maxi[MAX];
vector<int> vx, vy;
vector<tuple<int, int, int>> v;
vector<pii> crd[MAX]; 


void update(int start, int end, int node, int idx, int value) {
    if (idx < start || idx > end) return;

    if (start == end) {
        Lsum[node] += value;
        Rsum[node] += value;
        Asum[node] += value;
        maxi[node] += value;
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, idx, value);
    update(mid + 1, end, node * 2 + 1, idx, value);

    Lsum[node] = max(Lsum[node * 2], Asum[node * 2] + Lsum[node * 2 + 1]);
    Rsum[node] = max(Rsum[node * 2 + 1], Asum[node * 2 + 1] + Rsum[node * 2]);
    Asum[node] = Asum[node * 2] + Asum[node * 2 + 1];
    maxi[node] = max({ maxi[node * 2], maxi[node * 2 + 1], Lsum[node], Rsum[node], Asum[node], Lsum[node * 2 + 1] + Rsum[node * 2] });
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int x, y, w, ans = 0;
    pii p;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x >> y >> w;
        ans += w;
        vx.push_back(x); vy.push_back(y);
        v.push_back({ x, y, w });
    }
    sort(vx.begin(), vx.end());
    sort(vy.begin(), vy.end());
    vx.erase(unique(vx.begin(), vx.end()), vx.end());
    vy.erase(unique(vy.begin(), vy.end()), vy.end());

    for (int i = 0; i < n; i++) {
        x = get<0>(v[i]); y = get<1>(v[i]); w = get<2>(v[i]);
        int nx = lower_bound(vx.begin(), vx.end(), x) - vx.begin();
        int ny = lower_bound(vy.begin(), vy.end(), y) - vy.begin();
        crd[nx].push_back({ ny, w });
    }
    int sz_x = vx.size(), sz_y = vy.size();

    for (int s = 0; s < sz_x; s++) {
        for (int i = s; i < sz_x; i++) {
            for (pii tmp : crd[i]) update(0, sz_y, 1, tmp.first, tmp.second);
            ans = max(ans, maxi[1]);
        }

        for (int i = s; i < sz_x; i++) {
            for (pii tmp : crd[i]) update(0, sz_y, 1, tmp.first, - tmp.second);
        }
    } 
    cout << ans;
}