#include <bits/stdc++.h>
#define ll long long
using namespace std;

long long a, b, c, k;

long long multi(long long b) {
    if (b == 0) return 1;
    if (b == 1) return a % c;
    
    if (b % 2 == 0) return (multi(b / 2) % c) * (multi(b / 2) % c) % c;
    else {
        return ((multi(b / 2) % c) * (multi(b / 2) % c)) % c  * (a % c) % c;
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> a >> b >> c;
    cout << multi(b);
}