#include <bits/stdc++.h>
using namespace std;
double a, b, c;

void sol() {
    cin >> a >> b >> c;
    cout << "$";
    cout << fixed; cout.precision(2);
    cout << a * b * c << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}