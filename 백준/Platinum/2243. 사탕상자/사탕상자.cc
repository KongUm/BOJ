#include <bits/stdc++.h>
#define MAX 1000001
using namespace std;

int n, arr[MAX], tree[MAX * 4];
int num = 1000000;

void update(int start, int end, int node, int idx, int value) {
  if (idx < start || idx > end) return;
  tree[node] += value;
  if (start == end) return;
  
  int mid = (start + end) / 2;
  update(start, mid, node * 2, idx, value);
  update(mid + 1, end, node * 2 + 1, idx, value);
}

int query(int start, int end, int node, int fl, int fr) {
  if (fr < start || fl > end) return 0;
  
  if (fl <= start && end <= fr) return tree[node];
  
  int mid = (start + end) / 2;
  return query(start, mid, node * 2, fl, fr) + query(mid + 1, end, node * 2 + 1, fl, fr);
}

int lower_bound(int left, int right, int target) {
  int mid, sum;
  while (right - left) {
    mid = (left + right) / 2;
    sum = query(1, 1000000, 1, 1, mid); 
    
    if (sum < target) left = mid + 1;
    else right = mid;
  }
  return right;
}

int main() {

  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
  int q, a, b;
  cin >> n;
    for (int i = 0; i < MAX * 4; i++) tree[i] = 0;
    for (int i = 0; i < MAX; i++) arr[i] = 0;
    
    for (int i = 0; i < n; i++) {
       cin >> q >> a;
       
       if (q == 1) {
         b = lower_bound(1, num, a);
         cout << b << "\n";
         update(1, num, 1, b, -1);
       }
       else {
         cin >> b;
         update(1, num, 1, a, b);
       }
    }
}
