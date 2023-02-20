#include <bits/stdc++.h>
#define int long long
#define ll long long

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, x;
vector<int> v;

int twoPointer() {
    int s = 0, e = v.size() - 1, d = x / 2, cnt = 0;
    if (x % 2 == 1) d++;

    while (s < e) {
        if (v[s] + v[e] >= d) {
            s++; e--; cnt++;
            continue;
        }
        s++;
    }
    return cnt;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int tmp, full = 0;
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (tmp == x) {
            full++;
            continue;
        }
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());

    int tp = twoPointer();
    cout << full + tp + (n - tp * 2 - full) / 3;
}   

// 만약 3개를 합친다면 무조건 0 0 0이더라도 꽉찬 병이 생긴다
// 즉 2개를 한번에 만들 수 있는 경우를 찾아야한다.