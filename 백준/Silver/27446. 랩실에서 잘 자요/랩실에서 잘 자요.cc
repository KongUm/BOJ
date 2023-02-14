#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 110;
int n, m;
bool ty[MAX] = { false };
vector<int> v;


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int tmp, cnt = 0, res = 0;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        ty[tmp] = true;
    }
    cnt = 10;
    for (int i = 1; i < n + 1; i++) {
        if (!ty[i]) {
            if (cnt <= 2) res += 2 * (cnt + 1);
            else res += 7;
            cnt = 0;
        }
        else cnt++;
    }
    cout << res;

}