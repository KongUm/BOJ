#include <bits/stdc++.h>
#define int long long
#define all(a) (a).begin(), (a).end()
#define YES cout << "YES" << "\n"
#define NO cout << "NO" << "\n"
using namespace std;
const int MAX = 50;
int n, m, a;
vector<int> v, tmp;

void sol() {
    v.clear();
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        tmp.clear();
        for (int j = 0; j < m; j++) cin >> a, tmp.push_back(a);
        if (i % 2 == 1) reverse(all(tmp));
        v.insert(v.end(), all(tmp));
    }
    
    for (int i = 1; i < n * m; i++) v[i] -= v[i - 1];
    if (v.back() == 0) YES;
    else NO;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}