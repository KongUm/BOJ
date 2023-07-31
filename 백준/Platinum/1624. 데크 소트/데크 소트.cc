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
const int MAX = 1010;
int n, arr[MAX], used[MAX];
vector<int> v;

int check(int idx) {
    for (int i = n - 1; i > -1; i--) {
        if (!used[i] && v[idx] == arr[i]) idx++, used[i] = 1;
    }
    for (int i = 0; i < n; i++) {
        if (!used[i] && v[idx] == arr[i]) idx++, used[i] = 1;
    }
    return idx;
} 

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i], v.push_back(arr[i]), used[i] = 0;
    sort(all(v));

    int now = 0, cnt = 0;
    while (now < n) {
        now = check(now);
        cnt++;
    }
    cout << cnt;
}