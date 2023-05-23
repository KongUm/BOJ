#include <bits/stdc++.h>
#define int long long
#define ll long long
#define all(a) (a).begin(), (a).end()

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, m, sq, arr[MAX];
vector<int> bucket[1010];

void init() {
    for (int i = 1; i < n + 1; i++) {
        bucket[i / sq].push_back(arr[i]);
    }
    for (int i = 0; i < 1010; i++) {
        if (bucket[i].size() > 0) sort(all(bucket[i]));
    }
}

void update(int idx, int val) {
    bool flag = true;
    vector<int> tmp;
    for (int i : bucket[idx / sq]) {
        if (i != arr[idx] || !flag) tmp.push_back(i);
        if (i == arr[idx] && flag) flag = false;
    }
    bucket[idx / sq].clear();

    int i = 0;
    while (i < tmp.size() && tmp[i] < val) bucket[idx / sq].push_back(tmp[i++]);
    bucket[idx / sq].push_back(val);
    while (i < tmp.size()) bucket[idx / sq].push_back(tmp[i++]);
    arr[idx] = val;
}   

int query(int l, int r, int k) {
    int res = 0;

    while (l % sq != 0 && l <= r) {
        if (arr[l] > k) res++;
        l++;
    }

    while ((r + 1) % sq != 0 && l <= r) {
        if (arr[r] > k) res++;
        r--;
    }

    while (l <= r) res += bucket[l / sq].end() - upper_bound(all(bucket[l / sq]), k), l += sq;
    return res;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n; sq = sqrt(n);
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    init();

    cin >> m;
    int q, a, b, c;

    for (int i = 0; i < m; i++) {
        cin >> q >> a >> b;
        if (q == 1) cin >> c, cout << query(a, b, c) << "\n";
        else update(a, b);
    }  
}