#include <bits/stdc++.h>
using namespace std;
const int MAX = 200010;
int n, arr[MAX], cnt[MAX], chk[MAX], flag;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) if(++cnt[arr[i]] >= 4) flag = 1;

    if (n >= 513 || flag) { cout << "Yes"; return 0; }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) chk[arr[i] ^ arr[j]]++;
    }

    for (int i = 0; i < MAX; i++) if (chk[i] >= 2) flag = 1;

    if (flag) cout << "Yes";
    else cout << "No";
}