#include <bits/stdc++.h>
using namespace std;

const int MAX = 100010;
int gate, n, parent[MAX], flag[MAX];

int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}

void uni(int a, int b) {
    a = find(a);
    b = find(b);

    if (a < b) parent[b] = a;
    else parent[a] = b;
}

signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int a, ans = 0;
  cin >> gate >> n;
  flag[0] = 1;
  for (int i = 0; i < MAX; i++) parent[i] = i;

  for (int i = 0; i < n; i++) {
    cin >> a;
    while (flag[find(a)] == 1 && find(a) != 0) {
     
      uni(a, a - 1);
      a = find(a);
    }
    if (find(a) == 0) break;
    else {
      flag[find(a)] = 1;
      uni(a, a - 1);
      ans ++;
    }
    
  }
  cout << ans;
}