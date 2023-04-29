#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
using pii = pair<int, int>;
const int MAX = 50010, INF = (int) 1e9 + 7;
int n, m, a, b, u[MAX], l[MAX];
queue<pii> uq, lq;
vector<int> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    cin >> l[0]; for (int i = 0; i < n; i++) { cin >> a >> b; lq.push({ a + 1, b }); }
    cin >> u[0]; for (int i = 0; i < m; i++) { cin >> a >> b; uq.push({ a + 1, b }); }

    for (int i = 1; i < MAX; i++) {
        if (!lq.empty() && lq.front().fi == i) {
            l[i] = lq.front().se; lq.pop();
        }
        else l[i] = l[i - 1]; 
    }

    for (int i = 1; i < MAX; i++) {
        if (!uq.empty() && uq.front().fi == i) {
            u[i] = uq.front().se; uq.pop();
        }   
        else u[i] = u[i - 1];
        
        if ((u[i - 1] < l[i - 1]) ^ (u[i] >= l[i]) == 0) v.push_back(i);
    }

    int res = 0, cnt = 0;
    for (int i = 1; i < v.size(); i++) {
        int tmp = 0;
        for (int j = v[i - 1]; j < v[i]; j++) tmp += u[j] - l[j];
        if (tmp > 0) { res += tmp; cnt++; }
    }
    cout << cnt << " " << res;
}