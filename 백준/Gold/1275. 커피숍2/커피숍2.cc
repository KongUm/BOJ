#include <bits/stdc++.h>

#define ll long long
using namespace std;

int n, m;
ll arr[100001], tree[400001];

void update(int i, ll value) {
    // 원소 업데이트를 처리 해주는 함수
    while (i <= n) {
        // 전 범위 합을 가지고 있는 index n 까지 값을 업데이트 한 후 종료.
        tree[i] += value;
        i += (i & -i);
        // L[i] = i & -i, 즉 마지막 1의 값을 더해 주면서 i를 담당 하고 있는 구간을 찾는다.
    }
}

ll query(int i) {
    // A[1] ~ A[i] 까지의 구간 합을 구하는 함수.
    ll ans = 0;
    while (i > 0) {
        ans += tree[i];
        i -= (i & -i);
    }
    return ans;
}


int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int x, y, a;
    ll b;
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i];
        update(i, arr[i]);
    }

    for (int i = 0; i < m; i++) {
        cin >> x >> y >> a >> b;
        cout << query(max(x, y)) - query(min(x, y) - 1) << "\n";
        update(a, b - arr[a]);
        arr[a] = b;
    }
}