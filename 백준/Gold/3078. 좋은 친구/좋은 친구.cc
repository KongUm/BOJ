#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
int n, k, cnt[21], ans = 0;
vector<int> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    string s;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        cin >> s;
        v.push_back(s.size());
    }
    for (int i = 0; i < k; i++) cnt[v[i]]++;

    for (int i = 0; i < n - 1; i++) {
        cnt[v[i]]--;
        if (i + k < n) cnt[v[i + k]]++;
        ans += cnt[v[i]];
    }
    cout << ans;
}