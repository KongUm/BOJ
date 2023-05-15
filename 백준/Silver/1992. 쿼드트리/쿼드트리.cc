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
const int MAX = 70;
int n, arr[MAX][MAX];
string s, ans;

string f(int sz, int y, int x) {
    int ret = 0; string tmp;
    for (int i = 0; i < sz; i++) {
        for (int j = 0; j < sz; j++) ret += arr[y + i][x + j];
    }

    if (ret == sz * sz) tmp += '1';
    else if (ret == 0) tmp += '0';
    else {
        tmp += "(";
        tmp += f(sz / 2, y, x);
        tmp += f(sz / 2, y, x + sz / 2);
        tmp += f(sz / 2, y + sz / 2, x);
        tmp += f(sz / 2, y + sz / 2, x + sz / 2);
        tmp += ")";
    }
    return tmp;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < n; j++) arr[i][j] = (int) s[j] - '0';
    }
    cout << f(n, 0, 0);
}