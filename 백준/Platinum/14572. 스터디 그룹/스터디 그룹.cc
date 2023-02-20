#include <bits/stdc++.h>
#define int long long
#define ll long long

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010;
int n, k, d, algo[31];
vector<int> st[MAX];
vector<pii> po;
set<int> set1,setAll;

int twoPointer() {
    int s = 0, e = -1, ans = 0;
    
    while (e < n - 1) {
        for (int al : st[po[++e].second]) {
            if (++algo[al] == 1) set1.insert(al);
        }

        while (po[e].first - po[s].first > d) {
            for (int al : st[po[s].second]) {
                if (--algo[al] == 0) set1.erase(al);
            }
            s++;
        }
        
        vector<int> era_v, pus_v;
        for (int i = 1; i < 31; i++) {
            if (algo[i] != e - s + 1 && setAll.find(i) != setAll.end()) era_v.push_back(i);
            if (algo[i] == e - s + 1 && setAll.find(i) == setAll.end()) pus_v.push_back(i);
        }
        for (int i : pus_v) setAll.insert(i);
        for (int i : era_v) setAll.erase(i);

        int sz = set1.size() - setAll.size();
        ans = max(ans,  sz * (e - s + 1)); 
    }
    return ans;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int m, a, tmp;
    cin >> n >> k >> d;    

    for (int i = 0; i < n; i++) {
        cin >> m >> a;
        for (int j = 0; j < m; j++) {
            cin >> tmp;
            st[i].push_back(tmp);
        }
        po.push_back({ a, i });
    }
    sort(po.begin(), po.end());
    if (k == 1) cout << 0;
    else cout << twoPointer();
}   