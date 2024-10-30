#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

double Correlation(vector<int>& x, vector<int>& y){
    int N = x.size();
    double corr = 0;

    for (int i = 0; i < N; i++){
        corr += x[i] * y[i];
    }
    
    return corr;
}

double NormalizedCorrelation(vector<int>& x, vector<int>& y){
    int N = x.size();
    double corr = 0;

    double sumXY = 0;
    double sumX2 = 0;
    double sumY2 = 0;

    for (int i = 0; i < N; i++){
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
        sumY2 += y[i] * y[i];
    }

    corr = sumXY / sqrt(sumX2 * sumY2);
    return corr;
}


int main(){
    vector <int> a = {1, 3, 5, -1, -4, -5, 1, 4};
    vector <int> b = {2, 4, 7, 0, -3, -4, 2, 5};
    vector <int> c = {-5, -1, 3, -4, 2, -6, 4, -1};

    cout << "Корреляция между a, b и c:" << endl;
    cout << "" << setw(11) << "a" << setw(10) << "b" << setw(10) << "c" << endl;
    cout << "a" << setw(10) << "-" << setw(10) << Correlation(a, b) << setw(10) << Correlation(a, c) << endl;
    cout << "b" << setw(10) << Correlation(b, a) << setw(10) << "-" << setw(10) << Correlation(b, c) << endl;
    cout << "c" << setw(10) << Correlation(c, a) << setw(10) << Correlation(c, b) << setw(10) << "-" << endl;

    cout << endl;

    cout << fixed << setprecision(4);
    cout << "Нормализованная корреляция между a, b и c:" << endl;
    cout << "" << setw(11) << "a" << setw(10) << "b" << setw(10) << "c" << endl;
    cout << "a" << setw(10) << "-" << setw(10) << NormalizedCorrelation(a, b) << setw(10) << NormalizedCorrelation(a, c) << endl;
    cout << "b" << setw(10) << NormalizedCorrelation(b, a) << setw(10) << "-" << setw(10) << NormalizedCorrelation(b, c) << endl;
    cout << "c" << setw(10) << NormalizedCorrelation(c, a) << setw(10) << NormalizedCorrelation(c, b) << setw(10) << "-" << endl;

}