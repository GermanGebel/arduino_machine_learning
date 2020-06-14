def c_array(data) -> str:
    """
    Возвращает тело N-мерного массива как в языке С++
    :param data: str, int, float - массив с переменными
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
    """
    Возвращает строку объявления переменной как в С++ для файла .h
    :param data: str, int, float - массив с переменными
    :param name: название массива для С++
    :return:
    extern int size;
    extern float array[10];
    """
    type_ = ''
    if type(data) == float:
        return 'extern float %s;' % (name)
    elif type(data) == int:
        return 'extern int %s;' % (name)
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
    """
    Возвращает строку инициализации переменной как в С++ для файла .cpp
    :param data: str, int, float - массив с переменными
    :param name: название массива для С++
    :return:
    int size = 5;
    int array[5] = {1, 2, 3, 4, 5};
    """
    type_ = ''
    if type(data) == float:
        return 'float %s = %d;' % (name, data)
    elif type(data) == int:
        return 'int %s = %d;' % (name, data)
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


def export_model_to_cpp(sklearn_model, h_filename='c++/modelMultinominalNB.h', cpp_filename='c++/modelMultinominalNB.cpp'):
    new_data = {
        'size_classes_': len(sklearn_model.classes_),
        'classes_': sklearn_model.classes_.tolist(),
        'size_class_log_prior_': len(sklearn_model.class_log_prior_),
        'class_log_prior_': sklearn_model.class_log_prior_.tolist(),
        'size_feature_log_prob_x': len(sklearn_model.feature_log_prob_.T),
        'size_feature_log_prob_y': len(sklearn_model.feature_log_prob_.T[0]),
        'feature_log_prob_': sklearn_model.feature_log_prob_.T.tolist()
    }

    with open(h_filename, 'w') as h_file:
        h_file.write('#include <string>\nusing std::string;\n')
        for key in new_data.keys():
            h_file.write(c_code_line_declaration(new_data[key], key))
            h_file.write('\n')
        h_file.close()

    with open(cpp_filename, 'w') as cpp_file:
        h = h_filename
        if '/' in h:
            h = h.split('/')
            h = h[len(h)-1]

        cpp_file.write('#include "{}"\n#include <string>\nusing std::string;\n'.format(h))
        for key in new_data.keys():
            cpp_file.write(c_code_line_init(new_data[key], key))
            cpp_file.write('\n')
        cpp_file.close()

