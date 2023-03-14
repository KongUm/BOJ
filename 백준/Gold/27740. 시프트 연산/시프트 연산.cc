#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 300010;
int n, arr[MAX];
pii p;

int twoPointer() {
    int e = 0, res = n + 1;

    for (int s = 0; s < n + 1; s++) {
        if (s == e) e++;
        while (arr[e] == 0 && e < n + 1) e++;

        int lcnt = s, rcnt = n - e + 1;
        int tmp = min(lcnt, rcnt) * 2 + max(lcnt, rcnt);
        
        if (tmp < res) p = { lcnt, rcnt };
        res = min(tmp, res);
    }

    return res;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    string s;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    cout << twoPointer() << "\n";
    if (p.fi <= p.se) {
        for (int i = 0; i < p.fi; i++) s += "L";
        for (int i = 0; i < p.se + p.fi; i++) s += "R";
    }
    else {
        for (int i = 0; i < p.se; i++) s += "R";
        for (int i = 0; i < p.se + p.fi; i++) s += "L";
    }
    cout << s;
}