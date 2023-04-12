#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;

struct Point {
    int x, y;
};

const int MAX = 2010;
int n;
Point u[MAX], v[MAX];
pair<double, double> res;


Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; } 
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y }; } // dot product
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; } // cross product
bool operator < (Point a, Point b) {
    if (a.x == b.x) return (a.y < b.y);
    return a.x < b.x;
}


multiset<Point> msP;

int checker(int i, int j) {
    int l1 = (u[i] - u[j]) ^ v[i], l2 = v[j] ^ v[i]; 
    if (l2 < 0) { l2 *= -1; l1 *= -1; } // 분모를 양수로 유지시켜줌
    int k1 = (u[j] - u[i]) ^ v[j], k2 = v[i] ^ v[j];
    if (k2 < 0) { k2 *= -1; k1 *= -1; }

    if ((l1 >= 0 && l1 <= l2) && (k1 >= 0 && k1 <= k2) && (l2 != 0 && k2 != 0)) { 
        // i) 두 선분이 평행하지 않고, 교점이 있는 경우
        // l2 == 0 or k2 == 0 인 경우는 평행한 경우임으로 예외처리 (두 방향 벡터의 cross product 값이 0)
        //cout << l1 << " " << l2 << "\n";
        //cout << (double) u[i].x + ( (double) k1 / k2) * v[i].x << " " << (double) u[i].y + ( (double)k1 / k2) * v[i].y << "\n";
        res = { u[i].x + ((double) k1 / k2) * v[i].x,  u[i].y + ( (double) k1 / k2) * v[i].y };
        return 1;
    }

    else if (l1 == 0 && k1 == 0) {
        // ii) 두 선분이 평행한 경우
        pii rg1 = { 0, v[i] * v[i] };
        if (rg1.fi > rg1.se) swap(rg1.fi, rg1.se);
        pii rg2 = { (u[j] - u[i]) * v[i] , (u[j] + v[j] - u[i]) * v[i] };
        if (rg2.fi > rg2.se) swap(rg2.fi, rg2.se);

        if (rg1.se == rg2.fi || rg2.se == rg1.fi) return 1; 
        // 끝 점에서 만나는 경우 
        if ((rg1.fi <= rg2.fi && rg2.fi <= rg1.se) || (rg2.fi <= rg1.fi && rg1.fi <= rg2.se)) return 2; 
        // 구간이 겹치는 경우 (교점이 무한함)
    }

    return 0; // 교차 x
}

void makeVector(int idx) {
    int a, b; 
    cin >> a >> b; u[idx] = { a, b }; msP.insert(u[idx]);
    cin >> a >> b; v[idx] = { a, b }; msP.insert(v[idx]);
    v[idx] = v[idx] - u[idx];    

   // cout << u[idx].x << " " << u[idx].y << " " << v[idx].x << " " << v[idx].y << "\n";

    for (auto iter = msP.begin(); iter != msP.end(); iter++) {
        if (msP.count(*iter) == 2) res = { (*iter).x, (*iter).y };
    }

}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    for (int i = 0; i < 2; i++) makeVector(i);

    int flag = checker(0, 1);
    if (flag) cout << 1 << "\n";
    else cout << 0 << "\n";
    
    cout << fixed;
    cout.precision(12);
    if (flag == 1) cout << res.fi << " " << res.se << "\n";
}