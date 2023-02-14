#include <bits/stdc++.h>
#define MAX 500000
using namespace std;

int n, m;
long long arr[MAX], tree[MAX * 4], lazy[MAX * 4];


long long init(int start, int end, int node) {
  if (start == end) return tree[node] = arr[start];
  int mid = (start + end) / 2;
  return tree[node] = init(start, mid, node * 2) ^ init(mid + 1, end, node * 2 + 1);
}

void update_lazy(int start, int end, int node) {
  if (lazy[node] != 0) {
    if ((end - start + 1) % 2 == 1) tree[node] ^= lazy[node];

    if (start != end) {
      lazy[node * 2] ^= lazy[node];
      lazy[node * 2 + 1] ^= lazy[node];
    }
    lazy[node] = 0;
  }
}

void update(int start, int end, int node, int rl, int rr, long long value) {
  update_lazy(start, end, node);
  
  if (rr < start || rl > end) return;
  
  if (rl <= start && rr >= end) {
    if ((end - start + 1) % 2 == 1) tree[node] ^= value;
    if (start != end) {
      lazy[node * 2] ^= value;
      lazy[node * 2 + 1] ^= value;
    }
    return;
  }
  
  int mid = (start + end) / 2;
  update(start, mid, node * 2, rl, rr, value);
  update(mid + 1, end, node * 2 + 1, rl, rr, value);
  tree[node] = tree[node * 2] ^ tree[node * 2 + 1];
}

long long query(int start, int end, int node, int fl, int fr) {
  update_lazy(start, end, node);

  if (fr < start || fl > end) return 0;
  if (fl <= start && fr >= end) return tree[node];
  
  int mid = (start + end) / 2;
  long long l = query(start, mid, node * 2, fl, fr);
  long long r = query(mid + 1, end, node * 2 + 1, fl, fr);
  return l ^ r;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0); 
  
  long long q, a, b, c;
  
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
 
  for (int i = 0; i < MAX * 4; i++) lazy[i] = 0;
  cin >> m;
  init(0, n - 1, 1);
  
  for (int i = 0; i < m; i++) {
    cin >> q >> a >> b;
    if (q == 1) {
      cin >> c;
      update(0, n - 1, 1, a, b, c);
    }
    else {
      cout << query(0, n - 1, 1, a, b) << "\n";
    }
  }
  return 0;
}