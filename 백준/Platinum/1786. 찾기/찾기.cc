#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;

vector<int> getPi(string p) {
    int sz = p.size(), j = 0;
    vector<int> pi(sz, 0); // 0 - indexed
    pi[0] = 0; 
    for (int i = 1; i < sz; i++) { 
        while (j > 0 && p[i] != p[j]) j = pi[j - 1];
        if (p[i] == p[j]) pi[i] = ++j;
        // p[i] != p[j]인 경우에는 pi[i] = 0 (초기화 값)임으로 따로 처리해 주지 않는다.
    } 
    return pi;
}

vector<int> kmp(string s, string p) {
    vector<int> ret;
    int sz1 = s.size(), sz2 = p.size(), j = 0;
    vector<int> pi = getPi(p);

    for (int i = 0; i < sz1; i++) {
        while (j > 0 && s[i] != p[j]) j = pi[j - 1];
        if (s[i] == p[j]) {
            if (j == sz2 - 1) {
                ret.push_back(i - sz2 + 1);
                j = pi[j];
            }
            else j++;
        }
    }
    return ret;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    string s, p;
    getline(cin, s);
    getline(cin, p);
    auto res = kmp(s, p);
    cout << res.size() << "\n";
    for (int i : res) cout << i + 1 << "\n";
}