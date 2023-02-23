#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int MAX = 100010;
int n, m, elvV[101], flrV[MAX];
int elvPath[101], flrPath[MAX];
vector<int> flr[MAX], route;
pii elv[MAX];

void makeEdge() {
    for (int i = 0; i < m; i++) {
        int a = elv[i].first, d = elv[i].second;
        for (int j = a; j <= n; j += d) flr[j].push_back(i);
    }
}

void bfs(int start, int end) {
    queue<pii> q;
    for (int i = 0; i < 101; i++) elvV[i] = -1;
    for (int i = 0; i < MAX; i++) flrV[i] = -1;
    
    for (int i : flr[start]) {
        q.push({ start, i });
        int a = elv[i].first, d = elv[i].second;
        for (int j = a ; j <= n; j += d) {
            q.push({ j, i });
        }
        elvV[i] = 1; elvPath[i] = start;
    }
    flrV[start] = 0;

    while (!q.empty()) {
        int f = q.front().first, e = q.front().second; q.pop();
        if (flrV[end] != -1 ) return;

        if (flrV[f] == -1) {
            flrV[f] = elvV[e]; 
            
            flrPath[f] = e;
            for (int i : flr[f]) {
                if (elvV[i] == -1) {
                    int a = elv[i].first, d = elv[i].second;
                    for (int j = a ; j <= n; j += d) q.push({ j, i });
                    elvV[i] = flrV[f] + 1; 
                    elvPath[i] = f;
                }
            }
        }
    }
}

void getRoute(int start, int end) {
    int now = end; 
    
    while (now != start) {
        route.push_back(flrPath[now]);
        now = elvPath[flrPath[now]];   
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, d, start, end, ans = (int) 1e9;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> d; // a = 첫째항, b = 공차 
        elv[i]  = { a, d };
    }
    cin >> start >> end;
    makeEdge(); bfs(start, end); getRoute(start, end);
    
    cout << flrV[end] << "\n";
    for (int i = route.size() - 1; i >= 0; i--) cout << route[i] + 1 << "\n";

}   
