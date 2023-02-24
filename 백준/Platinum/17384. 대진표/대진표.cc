#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = (1 << 20);
int n, arr[MAX], s;

int get(int num) {
    int res = 0;
    for (int i = 0; i < 21; i++) {
        if (num <= (1 << i)) {
            res = (1 << i); break;
        }
    }
    return res / 2;
}

void divide (int l, int r, int num) {
    int sz = (r - l + 1), mid = (l + r) / 2;

  //  cout << l << " " << r << " " << num << "\n";
    if (num == 0) return;
    
    else if (num == sz) {
        for (int i = l; i < r + 1; i++) arr[i] = 1;
        return;
    }

    else if (num <= sz / 2) { // 만약 2의 거듭제곱이라면 
        return divide(l, mid, num); // 왼쪽으로 몰아주기 
    }

    // 이 아래는 num > (sz / 2) 만 있음

    else if (num - (sz / 2) > sz / 4) {
        divide(l, mid, sz / 2);
        divide(mid + 1, r, num - (sz / 2));
        return;
    }
    // 이 아래는 sz / 2로 나눌 수 없음

    int lnum = num / 2, rnum = num / 2;
    if (num % 2 == 1) lnum += 1;
    int tmp = get(lnum);

    divide(l, mid, max(num - tmp, tmp));
    divide(mid + 1, r, min(num - tmp, tmp));
}  

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
   // cout << get(41) << "81\n";
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