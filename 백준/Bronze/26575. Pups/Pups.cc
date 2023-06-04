#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'
#define YES cout << "YES" << "\n"
#define NO cout << "NO" << "\n"

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;
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