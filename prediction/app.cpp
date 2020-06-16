#include <iostream>
#include <string>
#include "predict.h"
#include "modelMultinominalNB.h"
#include "testdata.h"

using namespace std;

int main(){
    for (int i=0; i<37; i++){
        cout << classes_[predict(x_test[i])];
        cout << endl;
    }
    return 0;
}