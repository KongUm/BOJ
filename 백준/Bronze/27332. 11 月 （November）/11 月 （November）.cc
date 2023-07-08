#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int d = a + 7 * b;

  if (d >= 1 && d <= 30) cout << "1";
  else cout << "0";
}