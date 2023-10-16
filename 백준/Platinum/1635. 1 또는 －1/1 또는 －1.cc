#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 100005;
int n, m;

void print(int a) {
    for (int i = 0; i < n; i++) {
        if (i <= a) cout << -1 << " ";
        else cout << 1 << " ";
    }
    cout << "\n";
}

void sol(vector<int> &v, int s) {
    int now = 0;
    for (int i = 0; i < n; i++) {
        now += v[i];
        if (now * 2 == s) return print(i);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;

    for (int i = 0; i < m; i ++) {
        int tmp, s = 0; vector<int> v;
        for (int j = 0; j < n; j++) {
            cin >> tmp; s += tmp;
            v.push_back(tmp);
        }
        sol(v, s);
    }
}