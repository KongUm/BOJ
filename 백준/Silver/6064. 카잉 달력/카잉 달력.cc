#include <bits/stdc++.h>
using namespace std;
const int MAX = 100010;
int m, n, x, y;

void sol() {
    cin >> m >> n >> x >> y;
    int maxi = ((m * n) / __gcd(m, n)), res = -1;  
    for (int i = x; i < maxi + 1; i += m) {
        int tmp = i % n;
        if (tmp == 0) tmp = n;
        if (tmp == y) { res = i; break; }
    }
    cout << res << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}