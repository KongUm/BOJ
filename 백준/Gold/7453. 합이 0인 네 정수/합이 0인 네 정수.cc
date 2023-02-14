#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
ll n, arr[4000][4];
vector<ll> A, B;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    ll cnt = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) cin >> arr[i][j];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A.push_back(arr[i][0] + arr[j][1]);
            B.push_back(arr[i][2] + arr[j][3]);
        }
    }
    sort(B.begin(), B.end());

    for (int i: A) {
        cnt += upper_bound(B.begin(), B.end(), - i) - lower_bound(B.begin(), B.end(), - i);
    }
    cout << cnt;
}