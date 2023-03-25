#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;
int m, n, k, arr[MAX], last[MAX];
int lval, rval, s, e;
multiset<int> ms;
vector<int> v;

bool flag = true;

void P() {
    for (int i : v) cout << i << " ";
    cout << "vector v \n";
    for (int i : ms) cout << i << " ";
    cout << " multiset\n";
    cout << "ms sz : " <<  ms.size() << "\n";
    cout << "\n";
}

void erase() {
    vector<int> tmp;
    auto l_it = ms.lower_bound(lval);
    auto r_it = ms.upper_bound(rval);
    for (auto iter = l_it; iter != r_it; iter++) tmp.push_back(*iter);
    
   // for (int i : tmp) cout << i << " erase\n";
    for (int i : tmp) ms.erase(i);
}

bool moveRight() {
    ms.insert(arr[++e]);
    
    if (ms.size() > k) {
        while (ms.find(arr[s]) == ms.end()) s++;
       // P();
       // cout << arr[s] << " "<< s << " " << e << " sibal\n"; 
        ms.erase(arr[s]);
        v.push_back(arr[s]);
        s++;
    }
    erase();
    if (ms.size() > k) flag = false;
    return flag;
}

void twoPointer() {
    lval = 1, rval = k, s = 0, e = -1;

    while (rval <= m) {
        //P();
        while (last[lval] > e) {
            if (moveRight() == false) {
                erase();
                if (ms.size() > k) return;
                else flag = true;
            }
        } 
        lval++; rval++;
        
        erase();
    }
}



void sol() {
    for (int i = 0; i < MAX; i++) last[i] = -1;
    ms.clear(); v.clear();
    flag = true;

    cin >> m >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        last[arr[i]] = i; 
    }
    

    twoPointer();
    
    for (int i : v) if (i < lval - 1) flag = false; 


    if (flag || next_permutation(arr, arr + n) == false) cout << "YES" << "\n";
    else cout << "NO" << "\n";

}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;
    while (T--) sol();
}