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
const int MAX = 500010;
int n;
pii pol, crd[MAX];
bool c[4];


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> crd[i].fi >> crd[i].se;
    cin >> pol.fi >> pol.se;

    for (int i = 0; i < n; i++) { crd[i].fi -= pol.fi; crd[i].se -= pol.se; }

    for (int i = 0; i < n; i++) {
        int x = crd[i].fi, y = crd[i].se;

        if (abs(x) <= abs(y)) {
            if (y >= 0) c[0] = true;
            else c[2] = true;
        }

        if (abs(x) >= abs(y)) {
            if (x >= 0) c[1] = true;
            else c[3] = true;
        }  
    }
    
   
    if (c[0] && c[1] && c[2] && c[3] == true) cout << "NO";
    else cout << "YES";
}