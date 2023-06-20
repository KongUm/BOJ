#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    vector<pii> v;
    int s, cnt = 1, n = 2;
    cin >> s;

    while (n * (n + 1) <= s) n++;

    for (int i = 1; i < n + 1; i++) {
        v.push_back({ 0, cnt });
        v.push_back({ cnt, cnt + 1 });
        cnt += 2;
    }
    cnt--;
    for (int i = 0; i < s - (n * (n - 1)); i++) {
        v.push_back({ cnt, cnt + 1 }); cnt++;
    }

    if (s == 1) v.pop_back();

    cout << v.size() + 1 << "\n";
    for (pii p : v) {
        cout << p.fi << " " << p.se << "\n";
    }


}