#include "modelMultinominalNB.h"
#include <string>
using std::string;
int size_classes_ = 6;
string classes_[6] = {"a","b","c","d","e","g"};
int size_class_log_prior_ = 6;
float class_log_prior_[6] = {-2.1972245773362196,-2.1972245773362196,-2.1972245773362196,-2.1972245773362196,-2.1972245773362196,-0.810930216216329};
int size_feature_log_prob_x = 4;
int size_feature_log_prob_y = 6;
float feature_log_prob_[4][6] = {{-1.0986122886681096,-1.0986122886681096,-1.6094379124341003,-1.252762968495368,-1.3862943611198904,-1.3633048428951917},{-1.791759469228055,-1.0986122886681096,-1.6094379124341003,-1.252762968495368,-1.3862943611198904,-1.3044643428722584},{-1.791759469228055,-1.791759469228055,-1.6094379124341003,-1.9459101490553132,-1.3862943611198904,-1.4925165743751978},{-1.0986122886681096,-1.791759469228055,-0.916290731874155,-1.252762968495368,-1.3862943611198904,-1.3940765015619454}};