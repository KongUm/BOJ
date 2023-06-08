#include <bits/stdc++.h>
#define int long long
using namespace std;
const int MAX = 50;
int n, arr[MAX][MAX], dp[MAX][MAX][3];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) cin >> arr[i][j];
    }
    dp[1][2][0] = 1;

    for (int y = 1; y < n + 1; y++) {
        for (int x = 2; x < n + 1; x++) {
            for (int t = 0; t < 3; t++) {
                if ((t == 0 || t == 2) && !arr[y][x]) dp[y][x][0] += dp[y][x - 1][t]; // 오른쪽
                if ((t == 1 || t == 2) && !arr[y][x]) dp[y][x][1] += dp[y - 1][x][t];
                if (arr[y][x] + arr[y - 1][x] + arr[y][x - 1] == 0) {
                    dp[y][x][2] += dp[y - 1][x - 1][t];
                } 
            }
        }
    }
    int s = 0;
    for (int i = 0; i < 3; i++) s += dp[n][n][i];
    cout << s;
}
