#include <bits/stdc++.h>
using namespace std;

signed main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        if (n % 2 == 0) n = (n / 2) ^ 6;
        else n = (n * 2) ^ 6;
    }
    
    cout << n;
}