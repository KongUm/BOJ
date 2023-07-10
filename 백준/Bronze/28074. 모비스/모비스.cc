#include <bits/stdc++.h>
#define int long long
using namespace std;

string s, chk = "MOBIS";
int flag[5];

signed main() {
    cin >> s;
    for (auto i : s) {
        for (int j = 0; j < 5; j++) flag[j] = max(flag[j], (int) (i == chk[j]));
    }
    int res = accumulate(flag, flag + 5, 0LL);
    if (res == 5) cout << "YES";
    else cout << "NO";
}