#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int MAX = 1010;
int n, s, tree[51];
bool dp[51][MAX];

void makeTree() {
    for (int i = 1; i < 51; i++) {
        tree[i] = i * (i + 1) / 2;
        //cout << i << " i " << tree[i] << "\n";
    }
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> s;
    dp[2][0] = true;
    makeTree();

    for (int i = 2; i < n; i++) {
        for (int j = 0; j <= s; j++) {
            for (int u = 1; u < 51; u++) {
                if (i + u <= n && j + tree[u] <= s && dp[i][j]) {
                    dp[i + u][j + tree[u]] = true; 
                }
            }
        }
    }

    if (dp[n][s]) cout << 1;
    else cout << 0;
}   
