#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 200010;
int n, hy[MAX], dp[MAX];
vector<int> graph[MAX];
vector<ti3> v;


void P() {
    for (int i = 1; i < n + 1; i++) cout << hy[i] << " ";
    cout << "\n";
    for (int i = 1; i < n + 1; i++) cout << dp[i] << " ";
    cout << "\n";
}
 
int dpDfs(int cur, int par) {
    dp[cur] = hy[cur];

    for (int node : graph[cur]) {
        if (node != par) {
            dp[cur] += dpDfs(node, cur);
        }
    }
    return dp[cur];
}

void dfsUp(int cur, int par) {

    for (int node : graph[cur]) {
        if (node != par) dfsUp(node, cur);
    }

    int diff = dp[cur];
    
    if (diff > 0) {
        hy[par] += diff; // 부모한테 주는거 말고는 다른 방법이 없다.
        dp[cur] -= diff; hy[cur] -= diff; // 부모한테 줬으므로 서브트리에서도 지워야한다.

        v.push_back({ cur, par, diff });
    }
}

void dfsDown(int cur, int par) {

    for (int node : graph[cur]) {
        if (node != par && dp[node] < 0) {
            int diff = -dp[node];
            hy[node] += diff; dp[node] += diff;
            hy[cur] -= diff;
                
            v.push_back({ cur, node, diff });
        }
    }
    

    for (int node : graph[cur]) {
        if (node != par) dfsDown(node, cur);
    }
    
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    for (int i = 1; i < n + 1; i++) cin >> hy[i];
    for (int i = 0; i < n - 1; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int s = accumulate(hy + 1, hy + n + 1, 0LL);
    int c = s / n;
    for (int i = 1; i < n + 1; i++) hy[i] -= c;
    dpDfs(1, 0);
    dfsUp(1, 0);
    dfsDown(1, 0);

    cout << v.size() << "\n";
    for (auto t : v) {
        cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << "\n";
    }
}