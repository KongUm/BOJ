#include <bits/stdc++.h>
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
using pii = pair<int, int>;
string s[3] = { "Soongsil", "Korea", "Hanyang" };

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, c;
    cin >> a >> b >> c;
    int m = min({ a, b, c });
    if (a + b + c >= 100) cout << "OK";
    else if (a == m) cout << s[0];
    else if (b == m) cout << s[1];
    else cout << s[2];
}