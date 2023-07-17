#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
int n, c, a;
vector<int> on, off;
set<string> st;

string op1(string &s) {
    string tmp = "";
    for (char i : s) tmp += ((i == '0') ? '1' : '0');
    return tmp;
}

string op2(string &s) {
    string tmp = "";
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) tmp += ((s[i] == '0') ? '1' : '0');
        else tmp += s[i];
    }
    return tmp;
}

string op3(string &s) {
    string tmp = "";
    for (int i = 0; i < n; i++) {
        if (i % 2 == 1) tmp += ((s[i] == '0') ? '1' : '0');
        else tmp += s[i];
    }
    return tmp;
}

string op4(string &s) {
    string tmp = "";
    for (int i = 0; i < n; i++) {
        if (i % 3 == 0) tmp += ((s[i] == '0') ? '1' : '0');
        else tmp += s[i];
    }
    return tmp;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n >> c;  
    cin >> a;
    while (a != -1) on.push_back(a), cin >> a;
    cin >> a;
    while (a != -1) off.push_back(a), cin >> a;

    
    for (int i = 0; i < 16; i++) {
        string s = ""; int cnt = 0;
        for (int j = 0; j < n; j++) s += '1';
    
        if (i & 1) s = op1(s), cnt++;
        if (i & 2) s = op2(s), cnt++;
        if (i & 4) s = op3(s), cnt++;
        if (i & 8) s = op4(s), cnt++;

        for (int j : on) if (s[j - 1] != '1') cnt = -1;
        for (int j : off) if (s[j - 1] != '0') cnt = -1;

        if (cnt == -1) continue;
        if ((cnt % 2) == (c % 2) && cnt <= c) {
            if (st.find(s) == st.end()) st.insert(s);
        }
    }  

    for (string p : st) cout << p << "\n";  
    

}