#include <bits/stdc++.h>
#define all(a) (a).begin(), (a).end()
using namespace std;
using pii = pair<int, int>;
int n, a, arr[100010];
vector<pii> v;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a, v.push_back({ a, i });
    sort(all(v));
    
    int num = n;
    for (auto p : v) arr[p.second] = num--;
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
}