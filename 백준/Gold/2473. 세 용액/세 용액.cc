#include <bits/stdc++.h>
#define ll long long
#define int long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
const int MAX = 5010;
int n, arr[MAX], ans = (int) 1e12;
tuple<ll, ll, ll> t;

void tp(int s, int e, int idx) {
    ll target = -arr[idx];
    if (idx == s) s++;
    if (idx == e) e--;

    while (s < e) {
        ll now = abs(arr[s] + arr[idx] + arr[e]);
        if (now < ans) {
            ans = now;
            t = make_tuple(arr[s], arr[idx], arr[e]);
        }
        if (arr[s] + arr[e] >= target) e--;
        else if (arr[s] + arr[e] < target) s++;

        if (idx == s) s++;
        if (idx == e) e--;
    }
}  

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n);
    for (int i = 0; i < n; i++) tp(0, n - 1, i);
    ll A[3] = {get<0>(t), get<1>(t), get<2>(t)};
    sort(A, A + 3);
    cout << A[0] << " " << A[1] << " " << A[2];
}