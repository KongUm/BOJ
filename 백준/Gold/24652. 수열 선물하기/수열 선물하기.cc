#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 1000010;
int n, k, arr[MAX];

bool f(int x){
    int l = 1, r = n;
    while (l <= r){
        int mid = (l+r) / 2;
        if (arr[mid] == x){ return true; } // 값이 중앙값과 같으면 '찾았음'으로 판정
        if (x < arr[mid]){ r = mid-1; }    // 값이 중앙값보다 작으면 [l, mid) 구간을 탐색
        if (arr[mid] < x){ l = mid+1; }    // 값이 중앙값보다 크면 (mid, r] 구간을 탐색
    }
    return false;                        // [l, r] 구간에 남은 수가 없다면 '찾지 못함'으로 판정
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr); 
    cin >> n >> k;
    int mid = (1 + n) / 2;
    int lcnt = (k - 1) / 2, rcnt = k - lcnt - 1;

    int val = 1;
    for (int i = mid + 1; i < mid + (n - mid - rcnt) + 1; i++) arr[i] = val++;
    for (int i = 1; i < lcnt + 1; i++) arr[i] = val++;
    arr[mid] = val++;
    for (int i = mid + (n - mid - rcnt) + 1; i < n + 1; i++) arr[i] = val++;
    for (int i = lcnt + 1; i < mid; i++) arr[i] = val++; 

    cout << "YES" << "\n";
    for (int i = 1; i < n + 1; i++) cout << arr[i] << " ";
}