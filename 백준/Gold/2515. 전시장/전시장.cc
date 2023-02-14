#include <bits/stdc++.h>
using namespace std;

const int MAX = 20000010;
int n, s;
int arr[MAX];
int dp[MAX]; // dp[i] = i 높이 이하 까지 그림을 샀을때 가격의 최댓값

signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  
  int h, price;
  cin >> n >> s;
  
  for (int i = 0; i < n; i++) {
    cin >> h >> price;
    arr[h] = max(arr[h], price);
  }
  
  for (int i = 1; i < MAX; i++) { // i 원짜리 살거임
    if (i - s >= 0 && arr[i] > 0) {
      dp[i] = max(dp[i - s] + arr[i], dp[i - 1]);
    } else dp[i] = dp[i - 1];
  }
  cout << dp[MAX - 1] << "\n";
}