#include <bits/stdc++.h>
#define int long long
#define ll long long
using namespace std;
using pii = pair<int, int>; 

const int MAX = 100010;
int n, m, arr[MAX], prefix[MAX], dp[MAX];
// dp[i] = i ~ MAX까지의 prefix sum중 최댓갑

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int res = 0;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 1; i < n + 1; i++) prefix[i] = prefix[i - 1] + arr[i - 1];

    dp[n] = prefix[n];
    for (int i = n - 1; i > 0; i--) {
        dp[i] = max(dp[i + 1], prefix[i]);
    }   

    for (int i = 0; i < n - m + 1; i++) {
        res = max(dp[i + m] - prefix[i], res);
    }
    cout << res;
}   