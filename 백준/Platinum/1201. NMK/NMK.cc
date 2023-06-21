#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 510;
int n, m, k, dp[MAX], dp2[MAX];
vector<int> v, sz;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m >> k;
    int num = k, cnt = n - k;
  
    if (cnt < 0 || m + k > n + 1) { cout << -1; return 0; }
    if (m + k == 2) {
        if (n == 1) { cout << 1; return 0; }
        else { cout << -1; return 0; }
    }

    for (int i = k; i > 0; i--) v.push_back(i);

    if (m > 1) {
        for (int i = 0; i < m - 1; i++) sz.push_back(cnt / (m - 1));
        for (int i = 0; i < cnt % (m - 1); i++) sz[i]++;
        for (int i : sz) {
            num = num + i;
            for (int j = 0; j < i; j++) v.push_back(num - j);
        }
    }

    for (int i = 0; i < n; i++) dp[i] = 1, dp2[i] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (v[i] > v[j]) dp[i] = max(dp[j] + 1, dp[i]);
            if (v[i] < v[j]) dp2[i] = max(dp2[j] + 1, dp2[i]);
        }
    }

    int maxiM = *max_element(dp, dp + n);
    int maxiK = *max_element(dp2, dp2 + n);
    if (maxiM == m && maxiK == k) for (int i : v) cout << i << " ";
    else cout << -1;
}