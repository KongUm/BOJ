#include <bits/stdc++.h>
using namespace std;
const int MAX = 100010, INF = (int) 2e9;
int n, x, arr[MAX], res = INF;

signed main() {
    cin >> n >> x;
    for (int i = 0; i < n; i++) cin >> arr[i];

    for (int i = 1; i < n; i++) {
        res = min(res, (arr[i - 1] + arr[i]) * x);
    }
    cout << res;
}