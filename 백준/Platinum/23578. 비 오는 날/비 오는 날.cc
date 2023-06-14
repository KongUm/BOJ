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
const int MAX = 300010;
int n, s, arr[MAX], cnt[MAX];
priority_queue<pii, vector<pii>, greater<pii>> pq;

int get(int idx) {
    return arr[idx] * (cnt[idx] * 2 + 1);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i], cnt[i] = 1, s += arr[i];
        pq.push({ get(i), i });
    }

    for (int i = 0; i < n - 2; i++) { // n - 2번 반복
        while (!pq.empty() && pq.top().fi != get(pq.top().se)) pq.pop();
        auto p = pq.top(); pq.pop();
        s += p.fi, cnt[p.se]++;
        pq.push({ get(p.se), p.se });
    }
    if (n == 1) s = 0;
    cout << s << "\n";
}