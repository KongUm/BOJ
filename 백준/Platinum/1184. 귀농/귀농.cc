#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 51;
int n, nn, arr[MAX][MAX], cnt;
vector<int> ps[4][MAX][MAX];
int dx[4] = {-1, -1, 1, 1}, dy[4] = {-1, 1, -1, 1};
// 0 = 왼쪽 위, 1 = 오른쪽 위, 2 = 왼쪽 아래, 3 = 오른쪽 아래

int get(int y1, int x1, int y2, int x2) {
    int res = arr[y2][x2] - arr[y1 - 1][x2] - arr[y2][x1 - 1] + arr[y1 - 1][x1 - 1];
    return res;
}

void count(int num, int y, int x, int s) {
    int tmp = upper_bound(all(ps[num][y][x]), s) - lower_bound(all(ps[num][y][x]), s);
    cnt += tmp;
}

void prefixSum() {
    for (int y = 1; y < n + 1; y++) {
        for (int x = 1; x < n + 1; x++) arr[y][x] += arr[y][x - 1];
    }

    for (int x = 1; x < n + 1; x++) {
        for (int y = 1; y < n + 1; y++) arr[y][x] += arr[y - 1][x];
    }
}

void makeArray() {
    for (int i = 0; i < nn; i++) {
        for (int j = i; j < nn; j++) {
            int y1 = i / n + 1, x1 = i % n + 1, y2 = j / n + 1, x2 = j % n + 1;
            int s = get(y1, x1, y2, x2);

            if (x1 > x2 || y1 > y2) continue;

            if (y2 < n && x2 < n) ps[0][y2 + 1][x2 + 1].push_back(s); // y2 + 1, x2 + 1 왼쪽 위에 s인 크기의 사각형이 인접해 있음
            if (y2 < n && x1 > 1) ps[1][y2 + 1][x1 - 1].push_back(s); // y2 + 1, x1 - 1 오른쪽 위에 s인 크기의 사각형이 인접해 있음
        }
    }

    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            sort(all(ps[0][i][j]));
            sort(all(ps[1][i][j]));
        }
    }
}

void sol() {
    for (int i = 0; i < nn; i++) {
        for (int j = i; j < nn; j++) {
            int y1 = i / n + 1, x1 = i % n + 1, y2 = j / n + 1, x2 = j % n + 1;
            int s = get(y1, x1, y2, x2);

            if (x1 > x2 || y1 > y2) continue;
            
            count(0, y1, x1, s); // 0 = 왼쪽 위
            count(1, y1, x2, s); // 1 = 오른쪽 위
        }
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n; nn = n * n;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < n + 1; j++) cin >> arr[i][j];
    }
    prefixSum(); makeArray(); sol();
  
    cout << cnt << "\n";
}