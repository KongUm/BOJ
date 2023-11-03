#include <bits/stdc++.h>
using namespace std;
using cpx = complex<double>;
const int MAX = 300010;
const double pi = acos(-1);

void FFT(vector<cpx> &v, cpx w){
	int n = v.size();
	if(n == 1) return; 
	vector<cpx> even(n / 2), odd(n / 2);
	for(int i = 0; i < n; i++){
		if(i % 2 == 1) odd[i / 2] = v[i];
		else even[i / 2] = v[i];
	}
	FFT(even, w * w); FFT(odd, w * w);
	cpx wp(1, 0);
	for(int i = 0; i < n / 2; i++){
		v[i] = even[i] + wp * odd[i];
		v[i + n / 2] = even[i] - wp * odd[i];
		wp *= w;
	}
}

vector<cpx> convolution(vector<cpx> a, vector<cpx> b){
	int n = 1;
	while(n <= 2 * a.size() || n <= 2 * b.size()) n *= 2;
	a.resize(n); b.resize(n); vector<cpx> c(n);
	cpx w(cos(2 * pi / n), sin(2 * pi / n));

	FFT(a, w); FFT(b, w);
	for(int i = 0; i < n; i++) c[i] = a[i] * b[i];
	FFT(c, cpx(1, 0) / w);

	for(int i = 0; i < n; i++){
		c[i] /= cpx(n, 0);
		c[i] = cpx(round(c[i].real()), round(c[i].imag()));
	}
	return c;
}

vector<cpx> stringToVec (string s) { 
	int len = s.size();
	vector<cpx> v(len);

	for (int i = 0; i < len; i++){
		int num = s[len - i - 1] - '0';
		v[i] = cpx(num, 0);
	}

	return v;
}

string viToString (vector<int> v, int sz) {
    string ret = "";
    for (int i = 0; i < sz; i++) {
        ret += to_string(v[i] % 10);
        if (i != sz - 1) v[i + 1] += (v[i] / 10);
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

string mul (string a, string b) {
    vector<cpx> va, vb, vc;
    if (a == "0" || b == "0") return "0";
    va = stringToVec(a);
    vb = stringToVec(b);
    vc = convolution(va, vb);

    vector<int> v;
    int sz = 2 * max(a.size(), b.size());
    for (int i = 0; i < sz; i++) v.push_back(vc[i].real());
    
    return viToString(v, sz);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    string sa, sb; cin >> sa >> sb;
    string res = mul(sa, sb);

    int flag = 1;
    for (int i = 0; i < res.size(); i++) {
        if (flag && res[i] == '0' && res.size() > 1) continue;
        if (res[i] != '0') flag = 0;
        cout << res[i];
    }
}   