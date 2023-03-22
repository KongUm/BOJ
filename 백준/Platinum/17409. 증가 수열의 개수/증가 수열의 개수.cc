#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010, DIV = (int) 1e9 + 7;
int n, k, ans, arr[MAX], segTree[12][MAX], dp[MAX][12];
// dp[i][j] = 마지막으로 i번째 수를 선택 했고 j개의 수열로 이루어져있고, 

void update(int t, int i, int value) {
    while (i <= MAX) {
        segTree[t][i] += value;
        segTree[t][i] %= DIV;
        i += (i & -i);
    }
}

int query(int t, int i) {
    int res = 0;
    while (i > 0) {
        res += segTree[t][i];
        res %= DIV;
        i -= (i & -i);
    }
    return res;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> k;
    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i]; arr[i]++;
    }
    update(0, 1, 1);

    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < k + 1; j++) {
            int q = query(j - 1, arr[i] - 1);
            dp[i][j] = ((dp[i][j] + DIV) + (q % DIV)) % DIV;
            update(j, arr[i], dp[i][j] % DIV);
        }
    }
    for (int i = 0; i < n + 1; i++) ans = ((ans % DIV) + (dp[i][k] % DIV)) % DIV;
    cout << ans;
}