#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 1010, INF = (int) 1e9 + 7;
int n, m;
string arr[MAX][MAX], s;
map<string, int> mp;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> s; arr[i][j] = s;
            if (mp.find(s) == mp.end()) mp.insert({ s, 0 });
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j + 1 < m && arr[i][j] == arr[i][j + 1]) mp[arr[i][j]] = true;
            if (i + 1 < n && arr[i][j] == arr[i + 1][j]) mp[arr[i][j]] = true;
            if (j + 2 < m && arr[i][j] == arr[i][j + 2]) mp[arr[i][j]] = true;
            if (i + 2 < n && arr[i][j] == arr[i + 2][j]) mp[arr[i][j]] = true;
        }
    }
    vector<string> v;
    bool flag = true;
    for (auto p : mp) if (p.se) v.push_back(p.fi);
    
    if (v.empty()) cout << "MANIPULATED" << "\n";
    else {
        sort(all(v));
        for (auto p : v) cout << p << "\n";
    }
}