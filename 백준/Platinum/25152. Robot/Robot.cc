#include <bits/stdc++.h>
using namespace std;
int n, arr[35][65], sy, sx, my = 35, mx = 65;

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    
    for (int i = 0; i < 32; i++) {
        if ((n & (1 << i)) != 0) {
            for (int j = sy; j < my; j++) arr[j][sx] = 1;
        }
        arr[sy][sx] = 1, arr[sy + 1][sx] = 1, arr[sy][sx + 1] = 1;
        arr[sy + 1][sx + 1] = 1, arr[sy + 1][sx + 2] = 1; 
        sy += 1, sx += 2;
    }
    for (int i = 0; i < mx; i++) arr[my - 1][i] = 1;
    
    cout << my << " " << mx << "\n";
    for (int i = 0; i < my; i++) {
        for (int j = 0; j < mx; j++) cout << 1 - arr[i][j];
        cout << "\n";
    }
}