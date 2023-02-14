#include <bits/stdc++.h>
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;

int tp(string &str, int s, int e, int cnt) {
  while (s <= e) {
      if (str[s++] != str[e--]) {
          if (cnt == 0) {
              if (tp(str, s - 1, e, 1) == 0 || tp(str, s, e + 1, 1) == 0) return 1; 
              else return 2;
          }
          else return 1;
      }
  }
  return 0;
}

signed main() {
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
  int t; cin >> t;
  for (int _ = 0; _ < t; _++) {
    string str;
    cin >> str;
    cout << tp(str, 0, str.size() - 1, 0) << "\n";
    
  }
}