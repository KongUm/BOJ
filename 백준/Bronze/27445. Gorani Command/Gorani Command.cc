#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
int n, m;
vector<pii> X, Y;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int tmp;
    cin >> n >> m;
    for (int i = 1; i < n; i++) {
        cin >> tmp;
        Y.push_back({ tmp, i });

    }
    cin >> tmp;
    Y.push_back({ tmp, n });
    X.push_back({ tmp, 1 });

    for (int i = 2; i < m + 1; i++) {
        cin >> tmp;
        X.push_back({ tmp, i });
    }
    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    cout << Y[0].second << " " << X[0].second;
}