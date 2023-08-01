#include <bits/stdc++.h>
using namespace std;
int n, arr[1010], used[1010], now = 0, cnt = 0; vector<int> v;

int check(int idx) {
    for (int i = n - 1; i > -1; i--) if (!used[i] && v[idx] == arr[i]) idx++, used[i] = 1;
    for (int i = 0; i < n; i++) if (!used[i] && v[idx] == arr[i]) idx++, used[i] = 1;   
    return idx;
} 

signed main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i], v.push_back(arr[i]), used[i] = 0;
    sort(v.begin(), v.end());
    while (now < n) now = check(now), cnt++;
    cout << cnt;
}