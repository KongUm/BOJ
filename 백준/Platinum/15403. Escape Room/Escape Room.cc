#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, arr[MAX];
vector<pii> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        v.push_back({ a, i });
    }
    sort(all(v));
    
    int num = n;
    for (auto p : v) arr[p.se] = num--;
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
}