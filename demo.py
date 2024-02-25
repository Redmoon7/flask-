def DictUrl(s):
    s = s[1:-1]
    pairs = s.split(',')
    my_dict = {}

    for i in pairs:
        key, value =  i[:1], i[2:]
        my_dict.update({
            key: value
        })

    return my_dict


zifu_json = '{1:https://这是他的外部链接1,2:https://这是他的外部链接2}'

print(DictUrl(zifu_json))
