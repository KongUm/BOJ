#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;
const int MAX = 100010, INF = (int) 1e9 + 7;
int n, arr[3], maxi = 0, mini = INF;
pii dp[2][3] ;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int j = 0; j < 3; j++) dp[1][j] = { 0, INF };

    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < 3; j++) cin >> arr[j];

        for (int j = 0; j < 3; j++) {
            for (int u = -1; u < 2; u++) {
                if (0 <= j + u && j + u < 3) {
                    dp[1][j + u].fi = max(dp[1][j + u].fi, dp[0][j].fi + arr[j + u]);
                    dp[1][j + u].se = min(dp[1][j + u].se, dp[0][j].se + arr[j + u]);
                }
            }
        }
        
        for (int j = 0; j < 3; j++) dp[0][j] = dp[1][j], dp[1][j] = { 0, INF };
    }    
    for (int i = 0; i < 3; i++) maxi = max(maxi, dp[0][i].fi), mini = min(mini, dp[0][i].se);
    cout << maxi << " " << mini;
}