#include <bits/stdc++.h>
#define int long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 1010;
int n, res;
pii arr[MAX];
vector<int> vy = {0, 1, 100000}, vx = {0, 1, 100000};
vector<pii> vp[MAX];
 
void compress() {
    sort(all(vx)); sort(all(vy));
    vx.erase(unique(all(vx)), vx.end());
    vy.erase(unique(all(vy)), vy.end());

    for (int i = 0; i < n; i++) {
        int a = arr[i].fi, b = arr[i].se;
        int y = lower_bound(all(vy), a + b) - vy.begin(); 
        int x = lower_bound(all(vx), max(a, b)) - vx.begin();
        //cout << a + b << " " << max(a, b) << " " << y << " " << x << "\n";
        vp[x].push_back({ y, i });
    }    

    // for (int i : vx) cout << i << " ";
    // cout << "\n";
    // for (int i : vy) cout << i << " ";
    // cout << "\n";
}



void count(int yi, int xi) {
    int dy = vy[yi] - vy[yi - 1];
    int dx = vx[xi] - vx[xi - 1];
    res += dy * dx;
    //cout << yi << " " << xi << "\n";
    //cout << vy[yi] << " " << vy[yi - 1] << " " << vx[xi] << " " << vx[xi - 1] << "\n";
}

void sol() {
    //cout << vx.size() << " " << vy.size() << "\n";
    for (int y = 0; y < vy.size(); y++) { // y 이상 = 무효
        int a = 0, b = 0;
        for (int x = 1; x < vx.size(); x++) { // x 이상 = 무효
            for (auto p : vp[x - 1]) {
                if (p.fi < y) {
                    //cout << p.fi << " " << y << " y\n";
                    a += arr[p.se].fi;
                    b += arr[p.se].se;
                }
            }
            //cout << a << " " << b << "ab \n";
            if (a > b) count(y, x);
        }

    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        arr[i] = { a, b };
        vy.push_back(a + b);
        vx.push_back(max(a, b));
    }
    compress(); sol();
    cout << res;
}