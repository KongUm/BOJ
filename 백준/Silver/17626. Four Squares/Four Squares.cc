#include <bits/stdc++.h>
#define int long long

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 50010;
int n, dp[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
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