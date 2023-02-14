#include <bits/stdc++.h>

#define ll long long
#define int long long
using namespace std;

const int N = 65538;
int n, k;
ll segTree[N * 4], arr[N];

ll init(int start, int end, int node) {
    if (start == end) return segTree[node] = arr[start];
    int mid = (start + end) / 2;
    return segTree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

void update(int start, int end, int node, int idx, ll value) {
    if (idx < start || idx > end) return;
    segTree[node] += value;

    if (start == end) return;

    int mid = (start + end) / 2;
    update(start, mid, node * 2, idx, value);
    update(mid + 1, end, node * 2 + 1, idx, value);
}

ll query(int start, int end, int node, int fl, int fr) {
    if (fr < start || fl > end) return 0;
    if (fl <= start && end <= fr) return segTree[node];

    int mid = (start + end) / 2;
    return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}

int lower_bound(int target) {
    int start = 0, end = N; // [start, end)
    while (start < end) {
        int mid = (start + end) / 2;
        ll sum = query(0, N, 1, 0, mid);
        if (target <= sum) end = mid;
        else start = mid + 1;
    }
    return start;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int temp, p, ans = 0;
    queue<int> Q;
    cin >> n >> k;
    for (int i = 0; i < k; i++) {
        cin >> temp;
        Q.push(temp);
        arr[temp] += 1;
    }
    init(0, N, 1);
    ans += lower_bound((k + 1) / 2);
    for (int i = 0; i < n - k; i++) {
        update(0, N, 1, Q.front(), -1);
        Q.pop();
        cin >> temp;
        update(0, N, 1, temp, 1);
        Q.push(temp);
        ans += lower_bound((k + 1) / 2);
    }
    cout << ans;
}