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
const int MAX = 100010;
int n, q, arr[MAX], p[MAX], b[MAX], p2[MAX];


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> q;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    for (int i = 1; i < n + 1; i++) p[i] = p[i - 1] + arr[i];
    for (int i = 1; i < n + 1; i++) b[i] = arr[i] * arr[i];
    for (int i = 1; i < n + 1; i++) p2[i] = p2[i - 1] + b[i];
    

    int a, b;
    for (int i = 0; i < q; i++) {
        cin >> a >> b;
        int tmp = p[b] - p[a - 1];
        int tmp2 = p2[b] - p2[a - 1];
        cout << (tmp * tmp - tmp2) / 2  << "\n";
    }
}