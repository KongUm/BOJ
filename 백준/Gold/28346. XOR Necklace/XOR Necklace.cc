#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'
#define YES cout << "YES" << "\n"
#define NO cout << "NO" << "\n"

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 510;
int n, arr[MAX], dp[MAX][MAX];

void sol() {
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    for (int i = 0; i < n + 5; i++) {
        for (int j = 0; j < n + 5; j++) dp[i][j] = 0;
    }

    for (int u = 1; u < n; u++) { // 1 ~ n - 1
        for (int i = u + 1; i < n + 1; i++) { // u + 1 ~ n + 1
            for (int j = u; j < i; j++) { // u ~ i - 1
                dp[u][i] = max(dp[u][i], dp[u][j] + (arr[i] ^ arr[j]));
            }
        }
    }

    int res = 0;
    for (int i = 1; i < n; i++) {
        for (int j = i + 1; j < n + 1; j++) {
            res = max(res, dp[i][j] + (arr[i] ^ arr[j]));
        }
    }
    cout << res << "\n";

}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}