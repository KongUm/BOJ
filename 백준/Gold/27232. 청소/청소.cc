#include <bits/stdc++.h>
#define int long long
#define ll long long
using namespace std;
using pii = pair<int, int>;

const int MAX = 500010;
int n, k, arr[MAX];
map<int, int> mp;

int moveRight(int idx) {
    int res = 0;
    int l = -1, r = -1;
    auto iter = mp.upper_bound(arr[idx]);

    if (iter != mp.end()) {
        r = iter -> second;
        res += abs(idx - r);
    }

    if (iter != mp.begin()) {
        l = (--iter) -> second;
        res += abs(idx - l);
    }

    if (l >= 0 && r >= 0) res -= abs(l - r);
    mp.insert({ arr[idx], idx });
    return res;
}

int moveLeft(int idx) {
    int res = 0;
    mp.erase(arr[idx]);

    auto iter = mp.upper_bound(arr[idx]);
    int l = -1, r = -1;
    
    if (iter != mp.end()) {
        r = iter -> second;
        res -= abs(idx - r);
    }

    if (iter != mp.begin()) {
        l = (--iter) -> second;
        res -= abs(idx - l);    
    }

    if (l >= 0 && r >= 0) res += abs(l - r);
    return res;
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int s = 0;
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];
    mp.insert({ arr[0], 0 });
    
    for (int i = 1; i < k; i++) s += moveRight(i);
    int res = s;
    
    for (int i = 0; i < n - k; i++) {
        s += moveLeft(i) + moveRight(i + k);
        res = min(res, s);
    }
    cout << res;
}   
