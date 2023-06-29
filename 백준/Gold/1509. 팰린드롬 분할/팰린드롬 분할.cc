#include <bits/stdc++.h>
using namespace std;
const int MAX = 3010;
int n, dp[MAX];
string s;
vector<int> v[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> s; n = s.size();
    for (int i = 0; i < MAX; i++) dp[i] = (int) 1e9;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int lo = i - j, hi = i + j;
            if (0 <= lo && hi < n && s[lo] == s[hi]) v[lo].push_back(j * 2 + 1);
            else break;
        }
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n; j++) {
            int lo = i - j, hi = i + j + 1;
            if (0 <= lo && hi < n && s[lo] == s[hi]) v[lo].push_back(j * 2 + 2);
            else break;
        }
    }

    dp[0] = 0;
    
    for (int i = 1; i < n + 1; i++) {
        for (int j : v[i - 1]) {
            dp[i + j - 1] = min(dp[i - 1] + 1, dp[i + j - 1]);
        }
    }
    cout << dp[n];
}