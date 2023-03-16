#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 2010;
int n, arr[MAX], dp[MAX][MAX], res = 0;
// dp[i][j] = j칸에서 오른쪽으로 + i칸까지 선택되어 있을때의 JOI군이 가져올 수 있는 합의 최대

int mod(int num, int m) {
    if (num < 0) return (num % m) + m;
    else return num % m;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;

    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) dp[0][i] = arr[i];

    for (int i = 1; i < n; i++) {

        if (i % 2 == 0) {
            for (int j = 0; j < n; j++) {
                int l = dp[i - 1][mod(j + 1, n)] + arr[j]; // 왼쪽 조각 선택
                int r = dp[i - 1][j] + arr[mod(j + i, n)]; // 오른쪽 조각 선택

                dp[i][j] = max({ dp[i][j], l, r });
            }
        }
        
        else {
            for (int j = 0; j < n; j++) {
                int l = 0, r = 0;

                if (arr[j] >= arr[mod(j + i + 1, n)]) dp[i][j] = max(dp[i][j], dp[i - 1][mod(j + 1, n)]);
                if (arr[mod(j + i, n)] >= arr[mod(j - 1, n)]) dp[i][j] = max(dp[i][j], dp[i - 1][j]);
            }
        }

        
    }

    for (int i = 0; i < n; i++) res = max(res, dp[n - 1][i]);
    cout << res;
}