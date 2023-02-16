#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 1010, INF = (int) 1e9 + 7;
vector<pii> graph[MAX]; // 인접 리스트
int dist[MAX], path[MAX]; // 최단 거리 테이블, 경로 테이블 
int n, m;

void dijkstra(int start) {
    for (int i = 0; i < MAX; i++) {
        dist[i] = INF;
        path[i] = -1;
    } // 테이블 초기화 

    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({ 0, start }); dist[start] = 0;

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (cost > dist[now]) continue;
        // 이미 구한 거리가 더 짧으면 무시 

        for (auto i : graph[now]) {
            int nxt = i.first; // 다음 노드 
            int nxtCost = cost +  i.second; // 현재까지의 거리 + 간선의 가중치 
            if (nxtCost < dist[nxt]) {
                dist[nxt] = nxtCost;
                pq.push({ nxtCost, nxt });
                path[nxt] = now;
            }
        }
    }
}

void getRoute(vector<int> &route, int start, int end) {
    int idx = end;
    while (idx != start) {
        route.push_back(idx);
        idx = path[idx];
    }
    route.push_back(start); // 경로에 출발지까지 포함 
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b, w, start, end;
    vector<int> route;

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> w;
        graph[a].push_back({ b, w });
    }
    cin >> start >> end;
    dijkstra(start);
    getRoute(route, start, end);

    cout << dist[end] << "\n";
    int sz = route.size();
    cout << sz << "\n";
    for (int i = sz - 1; i > -1; i--) cout << route[i] << " ";
}