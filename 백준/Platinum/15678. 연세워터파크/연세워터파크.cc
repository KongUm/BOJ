#include <bits/stdc++.h>

#define int long long
#define ll long long
using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, d, arr[MAX * 2];
deque<pii> deq;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> d;

    for (int i = 0; i < n; i++) cin >> arr[i];
    int res = *max_element(arr, arr + n);

    deq.push_back({ arr[0], 0 });

    for (int i = 1; i < n; i++) { // 목적지
        int dp;

        while (!deq.empty() && deq.front().second < i - d) deq.pop_front();
        dp = max(arr[i], arr[i] + deq.front().first);
        res = max(res, dp);

        while (!deq.empty() && deq.back().first <= dp) deq.pop_back();
        deq.push_back({ dp, i });
    }
    cout << res;
}