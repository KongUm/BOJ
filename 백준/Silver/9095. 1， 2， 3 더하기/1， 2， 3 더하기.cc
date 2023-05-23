#include <bits/stdc++.h>
using namespace std;
const int MAX = 100;
int n, dp[MAX];

void sol() {
    cin >> n;
    for (int i = 0; i < MAX; i++) dp[i] = 0;
    dp[0] = 1;

    for (int i = 0; i < MAX; i++) {
        for (int j = 1; j < 4; j++) if (i - j >= 0) dp[i] += dp[i - j];
    }
    cout << dp[n] << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}