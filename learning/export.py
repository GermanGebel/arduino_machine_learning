import json


def c_array(data) -> str:
    """
    :param data: str, int, float, array
    :return: {1, 2} or {"1", "2"}
    """
    s = '{'
    for i in range(len(data)):
        if type(data[i]) == str:
            s += '"{}"'.format(data[i])
        else:
            if type(data[i]) == list:
                s += c_array(data[i])
            else:
                s += str(data[i])
        if i != len(data) - 1:
            s += ','
    s += '}'
    return s

def c_code_line_declaration(data, name):
    
    type_ = ''
    if type(data) == float:
        return 'extern float %s;' % (name)
    if type(data[0]) == str:
        type_ = 'string'
    elif type(data[0]) == int:
        type_ = 'int'
    elif type(data[0]) == float:
        type_ = 'float'
    elif type(data[0]) == list:
        type_ = 'float'
        return 'extern %s %s[%d][%d];' % (type_, name, len(data), len(data[0]))
    return 'extern %s %s[%d];' % (type_, name, len(data))

def c_code_line_init(data, name):
    type_ = ''
    if type(data) == float:
        return 'float %s = %d;' % (name, data)
    if type(data[0]) == str:
        type_ = 'string'
    elif type(data[0]) == int:
        type_ = 'int'
    elif type(data[0]) == float:
        type_ = 'float'
    elif type(data[0]) == list:
        type_ = 'float'
        return '%s %s[%d][%d] = %s;' % (type_, name, len(data), len(data[0]), c_array(data))
    return '%s %s[%d] = %s;' % (type_, name, len(data), c_array(data))



def export(json_='model.json', h_filename = 'modelMultinominalNB.h',cpp_filename='modelMultinominalNB.cpp'):
    with open(json_, "r") as read_file:
        data = json.load(read_file)
        read_file.close()

    new_data = {
        'classes_': data['classes_'],
        'class_count_': data['class_count_'],
        'class_log_prior_': data['class_log_prior_'],
        'alpha' : data['params']['alpha'],
        'feature_count_': data['feature_count_'],
        'feature_log_prob_': data['feature_log_prob_']
    }

    with open(h_filename, 'w') as h_file:
        h_file.write('#include <string>\nusing std::string;\n')
        for key in new_data.keys():
            h_file.write(c_code_line_declaration(new_data[key], key))
            h_file.write('\n')
        h_file.close()

    with open(cpp_filename, 'w') as cpp_file:
        cpp_file.write('#include "{}"\n#include <string>\nusing std::string;\n'.format(h_filename))
        for key in new_data.keys():
            cpp_file.write(c_code_line_init(new_data[key], key))
            cpp_file.write('\n')
        cpp_file.close()
