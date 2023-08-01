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
const int MAX = 1010;
int n, m, arr[MAX][MAX], chk[MAX * MAX * 4];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    int locnt = 1, hicnt = n * (m - 1) + 1;
    arr[0][0] = 1;
    for (int x = 1; x < m; x++) arr[0][x] = arr[0][x - 1] + locnt, locnt += n;

    for (int y = 1; y < n; y++) {
        for (int x = 0; x < m; x++) {
            arr[y][x] = arr[y - 1][x] + hicnt, hicnt++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << arr[i][j] << " ";
        cout << "\n";
    }

    // int sz = 2 * n * m - n - m;

    // for (int y = 0; y < n; y++) {
    //     for (int x = 1; x < m; x++) {
    //         int tmp = abs(arr[y][x] - arr[y][x - 1]);
    //         if (tmp > sz) cout << tmp << "?\n";
    //         else chk[tmp]++;
    //     }
    // }

    // for (int x = 0; x < m; x++) {
    //     for (int y = 1; y < n; y++) {
    //         int tmp = abs(arr[y][x] - arr[y - 1][x]);
    //         if (tmp > sz) cout << tmp << "?\n";
    //         else chk[tmp]++;
    //     }
    // }

    // int flag = 1;
    // for (int i = 1; i < sz + 1; i++) if (chk[i] != 1) flag = 0;

    // if (flag) cout << "YES";
    // else cout << "NO";

}