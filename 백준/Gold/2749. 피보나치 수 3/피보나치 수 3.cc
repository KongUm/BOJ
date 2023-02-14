#include <bits/stdc++.h>
using namespace std;

const int di = 1000000, p = 1500000;
long long n, dp[p];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i < p; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % di;
    cout << dp[n % p] << "\n";
    return 0;
}