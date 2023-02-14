#include <bits/stdc++.h>

using namespace std;

int n, tree[100002], flower[100002];

void update(int i, int value) {
    while (i <= 100001) {
        tree[i] += value;
        i += (i & -i);
    }
}

int query(int i) {
    int ans = 0;
    while (i > 0) {
        ans += tree[i];
        i -= (i & -i);
    }
    return ans;
}


int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int l, r, lsum, rsum;
    cin >> n;
    for (int i = 0; i < 100002; i++) {
        tree[i] = 0;
        flower[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        cin >> l >> r;
        lsum = query(l);
        rsum = query(r);
        cout << lsum + rsum - flower[l] - flower[r] << "\n";
        flower[l] = lsum;
        flower[r] = rsum;

        update(l + 1, 1);
        update(r, -1);
    }
    return 0;
}