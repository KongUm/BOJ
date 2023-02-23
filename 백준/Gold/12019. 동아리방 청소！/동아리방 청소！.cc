#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int INF = (int) 1e12;
int n, m, arr[110];
int dp[110][2010][11];
pair<int, int> path[110][2010][11];
vector<vector<int>> route;

// dp[i][j][u] = i일에 u번 청소 할 수 있고, 사람 j

void init() {
    for (int i = 0; i < 110; i++) {
        for (int j = 0; j < 2010; j++) {
            for (int u = 0; u < 11; u++) dp[i][j][u] = INF;
        }
    }
}

void getMini(int n) {
    int res = INF;
    vector<pii> mini;
    

    for (int j = 0; j < 2010; j++) {
       // cout << j << " : " << dp[n][j][0] << "\n";
        if (res > dp[n][j][0]) {
            res = dp[n][j][0];
            mini.clear();
        }
        if (res == dp[n][j][0]) mini.push_back({j, 0});
    } 
    
    int sz = mini.size();
 

    for (int i = 0; i < sz; i++) {
        route.push_back({});
        for (int j = n; j > 0; j--) {
            pii tmp = path[j][mini[i].first][mini[i].second];
            if (tmp.second > mini[i].second) route[i].push_back(j); 
            mini[i] = tmp;
        }
        sort(route[i].begin(), route[i].end());
    }
    
    sort(route.begin(), route.end());
    cout << res << "\n";
    for (int j : route[0]) cout << j << " ";
    
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];

    init();
    dp[0][0][m] = 0;

    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < 2010; j++) { // 사람 
            for (int u = 0; u < m + 1; u++) { // 청ㅅ
                int tmp = dp[i - 1][j - arr[i]][u] + (j - arr[i]) * arr[i];
                if (j - arr[i] >= 0 && dp[i][j][u] > tmp) {
                    dp[i][j][u] = tmp;
                    path[i][j][u] = { j - arr[i], u };
                }
                if (u != 0 && dp[i][0][u - 1] > dp[i][j][u]) {
                    dp[i][0][u - 1] = dp[i][j][u];
                    path[i][0][u - 1] = path[i][j][u];
                }
            }
        }
    }
    getMini(n);
}