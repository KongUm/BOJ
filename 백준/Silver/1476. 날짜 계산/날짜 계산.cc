#include <bits/stdc++.h>

#define ll long long
using namespace std;
int E, S, M, e, s, m;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> E >> S >> M;
    for (int cnt = 1; cnt < 7980 * 2; cnt++) {
        if (E == e + 1 && S == s + 1 && M == m + 1) {
            cout << cnt;
            return 0;
        }
        e++;
        s++;
        m++;
        e %= 15;
        s %= 28;
        m %= 19;
    }
}