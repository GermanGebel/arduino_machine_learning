#include "predict.h"
#include "modelMultinominalNB.h"

float *MxM(int* matr){
    float* newMatr = new float[size_feature_log_prob_x];
    for(int i = 0;i < size_feature_log_prob_y; i++){
        newMatr[i] = 0;
        for(int t = 0; t<size_feature_log_prob_x; t++){
            newMatr[i] += matr[t] * feature_log_prob_[t][i];
        }
    }
    return newMatr;
}

void *MplusM(float* matr){
    for(int i=0; i<size_class_log_prior_; i++){
        matr[i] += class_log_prior_[i];
    }
}

int argmax(float* matr){
    int flag = 0;
    float max = matr[0];
    for (int i=1; i<size_class_log_prior_; i++){
        if (matr[i]>max){
            max = matr[i];
            flag = i;
        }
    }
    return flag;
}

int predict(int* img){
    float* predictMatr = MxM(img);
    MplusM(predictMatr);
    return argmax(predictMatr);
}