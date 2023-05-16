#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;
int n, m, cnt, res;
string s;
vector<int> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m >> s;

    for (int i = 1; i < m; i++) {
        if (cnt % 2 == 0 && s[i - 1] == 'I' && s[i] == 'O') cnt++;
        else if (cnt % 2 == 1 && s[i - 1] == 'O' && s[i] == 'I') cnt++;
        else {
            if (cnt / 2 > 0) v.push_back(cnt / 2);
            cnt = 0;
            if (s[i - 1] == 'I' && s[i] == 'O') cnt++;
        }
    }
    if (cnt / 2 > 0) v.push_back(cnt / 2);

    for (int i : v) {
        if (i >= n) res += (i - n + 1);
    }
    cout << res;

}