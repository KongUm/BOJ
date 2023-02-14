#include <bits/stdc++.h>
#define ll long long
#define int long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'
using namespace std;
const int m = 2, MOD = 1000000007;
ll n;

vector<vector<int>> multi(vector<vector<int>> &a, vector<vector<int>> &b) {
    vector<vector<int>> res(m, vector<int> (m, 0));
    for (int i = 0; i < m ; i++) {
        for (int j = 0; j < m; j++) {
            for (int u = 0; u < m; u++) {
                res[i][j] += (a[i][u] * b[u][j]);
                res[i][j] %= MOD;
            }
        } 
    }
    return res;
}

vector<vector<int>> pow(vector<vector<int>> &a, vector<vector<int>> &v, ll r) {
    if (r == 1) return v;
    vector<vector<int>> temp(m, vector<int> (m, 0));
    if (r % 2 == 0) {
        temp = pow(a, v, r / 2);
        return multi(temp, temp);
    }
    temp = pow(a, v, r - 1);
    return multi(temp, a);
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    if (n <= 1) {
        cout << n;
        return 0;
    }
    vector<vector<int>> A(m, vector<int> (m, 1));
    vector<vector<int>> B(m, vector<int> (m, 1));
    A[1][1] = 0; B[1][1] = 0;
    vector<vector<int>> ans = pow(A, B, n);
    cout << ans[0][1] % MOD;
}