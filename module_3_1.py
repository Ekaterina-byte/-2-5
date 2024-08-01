def string_info (string):
    string_ = ()
    string_ = (len(string), string.upper(), string.lower())
    try:
        string_info.calls_count += 1
    except AttributeError:
        string_info.calls_count = 1

    return string_

print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contans(string, list_to_search):
    string = string.lower()
    new_list = []
    for i in list_to_search:
        new_list.append(i.lower())
    if string in new_list:
        a = 'True'
    else:
        a = 'False'
    try:
        is_contans.calls_count += 1
    except AttributeError:
        is_contans.calls_count = 1
    return(print(a))

is_contans('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contans('cycle', ['recycling', 'cyclic' ])

print(string_info.calls_count + is_contans.calls_count)


