#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 1; i < n + 1; i++) v.push_back(i);
    for (int i = 1; i < n; i += 2) if ((i / 2) % 2 == 0) swap(v[i - 1], v[i]);
    cout << "YES\n";
    for (int i : v) cout << i << " ";
}