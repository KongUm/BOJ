#include <bits/stdc++.h>
using namespace std;

signed main() {
    string s; cin >> s;
    if (s == "fdsajkl;" || s == "jkl;fdsa") cout << "in-out";
    else if (s == "asdf;lkj" || s == ";lkjasdf") cout << "out-in";
    else if (s == ";lkjfdsa") cout << "reverse";
    else if (s == "asdfjkl;") cout << "stairs";
    else cout << "molu";
}