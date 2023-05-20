#include <bits/stdc++.h>
using namespace std;
const int MAX = 50010;
int n, dp[MAX];

signed main() {
    for (int i = 1; i < MAX; i++) dp[i] = (int) 1e9;
    cin >> n;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < MAX; j++) {
            for (int u = 1; u < 250; u++) {
                if (j - (u * u) >= 0) dp[j] = min(dp[j - (u * u)] + 1, dp[j]);
            }
        }
    }
    cout << dp[n];
}