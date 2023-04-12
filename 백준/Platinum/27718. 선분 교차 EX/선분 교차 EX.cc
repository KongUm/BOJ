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
const int MAX = 2010;
int n;

struct Point {
    int x, y;
};
Point u[MAX], v[MAX];

Point operator + (Point a, Point b) { return { a.x + b.x, a.y + b.y }; } 
Point operator - (Point a, Point b) { return { a.x - b.x, a.y - b.y }; }
ll operator * (Point a, Point b) { return { (ll) a.x * b.x + (ll) a.y * b.y }; } // dot product
ll operator ^ (Point a, Point b) { return { (ll) a.x * b.y - (ll) a.y * b.x }; } // cross product

int checker(int i, int j) {
    int l1 = (u[i] - u[j]) ^ v[i], l2 = v[j] ^ v[i]; 
    if (l2 < 0) { l2 *= -1; l1 *= -1; } // 분모를 양수로 유지시켜줌
    int k1 = (u[j] - u[i]) ^ v[j], k2 = v[i] ^ v[j];
    if (k2 < 0) { k2 *= -1; k1 *= -1; }

    //  cout << l1 << " " << l2 << " " << k1 << " " << k2 << " ";
    
    
    if ((l1 >= 0 && l1 <= l2) && (k1 >= 0 && k1 <= k2) && (l2 != 0 && k2 != 0)) {
        if (l1 == l2 || k1 == k2 || l1 == 0 || k1 == 0) return 1;
        else return 2;
    }
    // i) 두 선분이 평행하지 않고, 교점이 있는 경우
    // l2 == 0 or k2 == 0 인 경우는 평행한 경우임으로 예외처리

    else if (l1 == 0 && k1 == 0){
        pii rg1 = { 0, v[i] * v[i] };
        if (rg1.fi > rg1.se) swap(rg1.fi, rg1.se);
        pii rg2 = { (u[j] - u[i]) * v[i] , (u[j] + v[j] - u[i]) * v[i] };
        if (rg2.fi > rg2.se) swap(rg2.fi, rg2.se);

        if (rg1.se == rg2.fi || rg2.se == rg1.fi) return 1;
        if ((rg1.fi <= rg2.fi && rg2.fi <= rg1.se) || (rg2.fi <= rg1.fi && rg1.fi <= rg2.se)) return 3; 
        // ii) 두 선분이 평행하고 일직선 상에서 겹치는 경우
    }

    return 0; // 교차 x
}

// l = 0 or l == 1 -> 끝 점에서 교차
// l = l1 / l2 -> l1 == l2 or (l1 == 0 and l2 != 0

void makeVector(int idx) {
    int a, b; 
    cin >> a >> b; u[idx] = { a, b }; // 위치 벡터 
    cin >> a >> b; v[idx] = { a, b }; v[idx] = v[idx] - u[idx]; // 방향 벡터
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) makeVector(i);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << checker(i, j);
        cout << "\n";
    }
}