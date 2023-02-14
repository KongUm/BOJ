#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
const int MAX = 2010;
ll n, arr[MAX];

int tp(ll target, int s, int e, int idx) {
    if (s == idx) s++;
    if(e == idx) e--;
    while (s < e) {
        if (arr[s] + arr[e] < target) s++;
        else if (arr[s] + arr[e] > target) e--;
        else return 1;
        if (s == idx) s++;
        if(e == idx) e--;
    }
    return 0;
}


signed main() {
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
  int ans = 0;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> arr[i]; 
  sort(arr, arr + n);
  
  for (int i = 0; i < n; i++) ans += tp(arr[i], 0, n - 1, i);
  cout << ans;
    
}