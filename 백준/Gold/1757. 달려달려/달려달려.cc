#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 10010;
int n, m, arr[MAX], dp[MAX][510];
// dp[i][j] = i번째 시간을 고려하고 j 지침지수를 가질 때 최대로 갈 수 있는 거리 

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];

    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < m + 1; j++) {
            if (i - j >= 0) dp[i][0] = max(dp[i][0], dp[i - j][j]); 
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i]); 
        }
        dp[i][0] = max(dp[i][0], dp[i - 1][0]);
    }

    cout << dp[n][0] << "\n";
}