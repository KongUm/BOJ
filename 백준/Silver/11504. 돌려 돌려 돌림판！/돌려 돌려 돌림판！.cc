#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 200;
int n, m, lo, hi, arr[MAX];

void sol() {
    int res = 0;
    string s, tmp;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> tmp;
        s += tmp;
    }
    lo = stoll(s);
    s = "";

    for (int i = 0; i < m; i++) {
        cin >> tmp;
        s += tmp;
    }
    hi = stoll(s);

    for (int i = 0; i < n; i++) {
        cin >> arr[i]; arr[i + n] = arr[i];        
    }

    for (int i = 0; i < n; i++) {
        string tmp;
        for (int j = 0; j < m; j++) tmp += to_string(arr[i + j]);
        int val = stoll(tmp);
        if (lo <= val && val <= hi) res++;
    }
    cout << res << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol(); 
}