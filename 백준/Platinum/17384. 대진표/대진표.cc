#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = (1 << 20);
int n, arr[MAX], s;

int get(int num) {
    for (int i = 0; i < 21; i++) {
        int m = 1 << i;
        if (abs(num - m) <= (1 << (i - 1))) {
            return m / 2;
        }
    }
    return - 1;
}

void divide (int l, int r, int num) {
    int sz = (r - l + 1), mid = (l + r) / 2;

    if (num == 0) return;
    
    else if (num == sz) {
        for (int i = l; i < r + 1; i++) arr[i] = 1;
        return;
    }

    else if (num <= sz / 2) { // 왼쪽으로 전부 몰아 넣을 수 있다면
        return divide(l, mid, num); // 왼쪽으로 몰아주기 
    }

    // 이 아래는 num > (sz / 2) 만 있음
    int res = get(num);
    
    divide(l, mid, max(res, num - res));
    divide(mid + 1, r, min(res, num - res));
    return;

}  

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;

    for (int i = 0; i < 21; i++) {
        if (n <= (1 << i)) {
            s = (1 << i); break;
        }
    }

    divide(0, s - 1, n);
    for (int i = 0; i < s; i++) {
        if (arr[i] == 1) cout << "#";
        else cout << ".";
    }     
}