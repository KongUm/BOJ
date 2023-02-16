#include <bits/stdc++.h>
#define int long long
#define ll long long
using namespace std;

const int MAX = 100010;
int n, arr[MAX];
multiset<int> ms;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    int s = -1, e = 0, cnt = 0;
    
    while (e < n) {
        int target = arr[e];
        ms.insert(target);

        while (ms.count(target) > 1) ms.erase(ms.find(arr[++s]));
        
        cnt += e - s;
        e++;
    }
    cout << cnt;
}   