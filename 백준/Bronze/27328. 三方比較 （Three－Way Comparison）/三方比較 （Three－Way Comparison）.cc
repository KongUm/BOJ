#include <bits/stdc++.h>
using namespace std;
signed main() {
    int a, b; cin >> a >> b;
    int res = 0;
    if (a > b) res = 1;
    else if (a < b) res = -1;
    cout << res; 
}