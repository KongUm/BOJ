#include <bits/stdc++.h>
#define int long long
using namespace std;
using pii = pair<int, int>;
const int MAX = 110;
int n, m, k, dsu[MAX], cnt;
vector<int> lie, query[MAX];

int find(int x) {
    if (dsu[x] != x) return (dsu[x] = find(dsu[x]));
    return dsu[x];
} 

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) dsu[b] = a;
    else dsu[a] = b;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a;
    for (int i = 0; i < MAX; i++) dsu[i] = i;
    cin >> n >> m >> k;
    for (int i = 0; i < k; i++) cin >> a, lie.push_back(a + 1);
    for (int i = 1; i < k; i++) uni(lie[i - 1], lie[i]);
    if (!lie.empty()) uni(lie[0], 0);

    for (int i = 0; i < m; i++) {
        cin >> k;
        for (int j = 0; j < k; j++) cin >> a, query[i].push_back(a + 1);
        for (int j = 1; j < k; j++) uni(query[i][j - 1], query[i][j]);
    } 

    for (int i = 0; i < m; i++) if (find(query[i][0]) != 0) cnt++;
    cout << cnt;
}