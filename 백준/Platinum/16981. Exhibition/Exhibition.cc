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
int n, m, a, b, res = 0;
vector<int> frm; vector<pii> pic;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> a >> b, pic.push_back({ b, a });
    for (int i = 0; i < m; i++) cin >> a, frm.push_back(a);

    sort(all(pic), greater<>());
    sort(all(frm), greater<>());

    int idx = 0;
    for (int i = 0; i < m; i++) {
        while (idx < n && frm[i] < pic[idx].se) idx++;
        
        if (idx < n && frm[i] >= pic[idx].se) idx++, res++;
    }
    cout << res;
}