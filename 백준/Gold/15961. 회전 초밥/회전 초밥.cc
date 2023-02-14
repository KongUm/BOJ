#include <bits/stdc++.h>
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
const int MAX = 4000000;
int n, d, k, c, arr[MAX], ty[3010], now;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int temp, ans = 0;
    cin >> n >> d >> k >> c;

    now = 1;
    ty[c] = 1;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        arr[i] = temp;
    }
    for (int i = 0; i < k; i++) arr[i + n] = arr[i];
    
    for (int i = 0; i < k; i++) {
        if (ty[arr[i]] == 0) now += 1;
        ty[arr[i]] += 1;
    }
    ans = now;
    for (int i = 0; i < n; i++) { // i = 빠지는, i + k = 추가되는
        if (ty[arr[i + k]] == 0) now += 1;
        ty[arr[i + k]] += 1;
        
        if (ty[arr[i]] == 1) now -= 1;
        ty[arr[i]] -= 1;
        ans = max(ans, now);
    }
    cout << ans;
    
}