#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n, m, k;
ll A[100][100], B[100][100], arr[100][100];

signed main() {
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
  int temp;
  
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> temp;
      A[i][j] = temp;
    }
  }
  
  cin >> m >> k;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < k; j++) {
      cin >> temp;
      B[i][j] = temp;
    }
  }
  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < k; j ++) {
      for (int u = 0; u < m; u++) arr[i][j] += A[i][u] * B[u][j];
    }
  }
  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < k; j++) cout << arr[i][j] << " ";
    cout << "\n";
  }
  return 0;
}