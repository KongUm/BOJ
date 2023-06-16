#include <bits/stdc++.h>
using namespace std;
const int MAX = 110;
int n, m, arr[MAX];

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    for (int i = 0; i < MAX; i++) arr[i] = i;
    cin >> n >> m;
    for (int i = 0; i < m; i++) cin >> a >> b, swap(arr[a], arr[b]);
    for (int i = 1; i < n + 1; i++) cout << arr[i] << " ";
}