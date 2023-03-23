#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 500010;
int n, k, d, dp[MAX], arr[MAX], segTree[MAX * 4], md[MAX];
// dp[i] = i번째 커피 콩을 마지막으로 선택 했을 때의 좋은 수열 중 최대 길이

void update(int st, int ed, int nd, int idx, int val) {
    if (idx < st || idx > ed) return;

    if (st == ed) {
        segTree[nd] = val;
        return;
    }
    
    int mid = (st + ed) / 2;
    update(st, mid, nd * 2, idx, val);
    update(mid + 1, ed, nd * 2 + 1, idx, val);
    segTree[nd] = max(segTree[nd * 2], segTree[nd * 2 + 1]);
}

int query(int st, int ed, int nd, int fl, int fr) {
    if (fr < st || ed < fl) return 0;
    if (fl <= st && ed <= fr) return segTree[nd];

    int mid = (st + ed) / 2;
    int l = query(st, mid, nd * 2, fl, fr);
    int r = query(mid + 1, ed, nd * 2 + 1, fl, fr);
    return max(l, r);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> k >> d;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];

    for (int i = 1; i < n + 1; i++) {
        int tmp = query(1, MAX, 1, max(arr[i] - d, 1LL), min(arr[i] + d, 500000LL));
        dp[i] = max({ dp[i], tmp + 1, md[arr[i] % k] + 1 });
        update(1, MAX, 1, arr[i], dp[i]);
        md[arr[i] % k] = max(md[arr[i] % k], dp[i]);
    }
    cout << *max_element(dp, dp + MAX) << "\n";
}