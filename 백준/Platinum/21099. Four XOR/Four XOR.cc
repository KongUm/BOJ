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
int n, arr[MAX], cnt[MAX], chk[MAX], flag;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) if(++cnt[arr[i]] >= 4) flag = 1;

    if (n > 10000 || flag) { cout << "Yes"; return 0; }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) chk[arr[i] ^ arr[j]]++;
    }

    for (int i = 0; i < MAX; i++) if (chk[i] >= 2) flag = 1;
    
    if (flag) cout << "Yes";
    else cout << "No";
}