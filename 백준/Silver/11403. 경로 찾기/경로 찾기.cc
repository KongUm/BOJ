#include <bits/stdc++.h>
using namespace std;
const int MAX = 110;
int n, dp[MAX][MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> dp[i][j];
    }

    for (int i = 0; i < n; i++) {
        for (int s = 0; s < n; s++) {
            for (int e = 0; e < n; e++) dp[s][e] |= (dp[s][i] & dp[i][e]);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << dp[i][j] << " ";
        cout << "\n";
    }
}