#include <bits/stdc++.h>

using namespace std;

int ans = 0;
int cnt = 0;

void Z(int n, int y, int x, int r, int c) {
    if (n == 2) {
        for (int i = y; i < y + 2; i++) {
            for (int j = x; j < x + 2; j++) {
                if (i == r && j == c) {
                    ans = cnt;
                }
                cnt += 1;
            }
        }
        return;
    }
    int d = n / 2;
    if (c >= x + d) {
        x += d;
        cnt += d * d;
    }
    
    if (r >= y + d) {
        y += d;
        cnt += d * d * 2;
    }
    Z(n / 2, y, x, r, c);
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int N, r, c;
    cin >> N >> r >> c;
    int p = (int) pow(2, N);
    Z(p, 0, 0, r, c);
    cout << ans;
}