#include <bits/stdc++.h>

using namespace std;
const int MAX = 10010;
int n, m, arr[MAX], dp[MAX][510];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i];
        for (int j = 1; j < m + 1; j++) {
            if (i - j >= 0) dp[i][0] = max(dp[i][0], dp[i - j][j]); 
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i]); 
        }
        dp[i][0] = max(dp[i][0], dp[i - 1][0]);
    }
    cout << dp[n][0] << "\n";
}