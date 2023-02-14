#include <bits/stdc++.h>
#define ll long long
#define int long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
const int MAX = 100010;
int n, k, b, arr[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int temp, now = 0, mini = (int) 1e10;
    cin >> n >> k >> b;

    for (int i = 0; i < MAX; i++) arr[i] = 1;
    for (int i = 0; i < b; i++) {
        cin >> temp;
        arr[temp] = 0;
    }
    int s = 0, e = k; // (s, e]
    for (int i = 1; i < k + 1; i++) now += arr[i];
    mini = min(mini, k - now);

    while (e < n + 1) {
        now -= arr[++s];
        now += arr[++e];
        mini = min(mini, k - now);
    }
    cout << mini;
}