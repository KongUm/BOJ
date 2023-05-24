//코드 테스트 용
#include <bits/stdc++.h>
#define MINF 0x7f7f7f7f
#define INF 1000000000
#define MOD 10007
#define NUM 100010
#define X first
#define Y second
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;
typedef pair<ll, ll> pll;
typedef pair<double, int> pdi;
int N, Q, par[NUM], r[NUM];
set<int> st[NUM];
vector<pii> v;
vector<int> answer;

int find(int start) {
    if (start == r[start]) return start;
    return r[start] = find(r[start]);
}

void merge(int p, int son) {
    p = find(p), son = find(son);
    if (p == son) return;
    if (st[son].size() < st[p].size()) {
        r[son] = p;
        for (int c : st[son]) st[p].insert(c);
        st[son].clear();
    } else {
        r[p] = son;
        for (int c : st[p]) st[son].insert(c);
        st[p].clear();
    }
    
}

void init() {
    cin >> N >> Q;
    par[1] = 1;
    r[1] = 1;
    for (int i=2; i<=N; i++) {
        cin >> par[i];
        r[i] = i;
    }
    for (int i=1; i<=N; i++) {
        int x;
        cin >> x;
        st[i].insert(x);
    }
    for (int i=1; i<=N+Q-1; i++) {
        int x, y;
        cin >> x >> y;
        v.push_back({x, y});
    }
    reverse(v.begin(), v.end());
    for (auto [x, y] : v) {
        if (x == 1) {
            int p = par[y];
            merge(p, y);
        } else {
            int node = find(y);
            answer.push_back(st[node].size());
        }
    }
    reverse(answer.begin(), answer.end());
    for(int a : answer) cout << a << '\n';
} 

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    init();
}
