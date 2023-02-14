#include <bits/stdc++.h>
#define MAX 1000001
using namespace std;

int n, m, k;
long long arr[MAX], tree[MAX * 4], lazy[MAX * 4];
int num = 1000000;

long long init(int start, int end, int node) {
  if (start == end) return tree[node] = arr[start];
  int mid = (start + end) / 2;
  return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

void update_lazy(int start, int end, int node) {
  if (lazy[node] != 0) {
    tree[node] += (end - start + 1) * lazy[node];
    if (start != end) {
      lazy[node * 2] += lazy[node];
      lazy[node * 2 + 1] += lazy[node];
    }
    lazy[node] = 0;
  }
}

void update(int start, int end, int node, int rl, int rr, long long value) {
  update_lazy(start, end, node);
  
  if (rr < start || rl > end) return;
  
  if (rl <= start && rr >= end) {
    tree[node] += (end - start + 1) * value;
    if (start != end) {
      lazy[node * 2] += value;
      lazy[node * 2 + 1] += value;
    }
    return;
  }
  
  int mid = (start + end) / 2;
  update(start, mid, node * 2, rl, rr, value);
  update(mid + 1, end, node * 2 + 1, rl, rr, value);
  tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long query(int start, int end, int node, int fl, int fr) {
  update_lazy(start, end, node);

  if (fr < start || fl > end) return 0;
  if (fl <= start && fr >= end) return tree[node];
  
  int mid = (start + end) / 2;
  long long lsum = query(start, mid, node * 2, fl, fr);
  long long rsum = query(mid + 1, end, node * 2 + 1, fl, fr);
  return lsum + rsum;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0); 
  
  long long q, a, b, c;
  cin >> n >> m >> k;
  for (int i = 1; i < n + 1; i++) {
    cin >> arr[i];
    lazy[i] = 0;
  }
  init(1, num, 1);
  
  for (int i = 0; i < m + k; i++) {
    cin >> q >> a >> b;
    if (q == 1) {
      cin >> c;
      update(1, num, 1, a, b, c);
    }
    else {
      cout << query(1, num, 1, a, b) << "\n";
    }
  }
  return 0;
}
