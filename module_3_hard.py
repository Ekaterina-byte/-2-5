data_structure = [[1,2,3], {'a':4,'b':5},
(6, {'cube':7, 'drum':8}), "Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data) -> int:
    result = 0
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            result += calculate_structure_sum(item)
    if isinstance(data, dict):
        for key, value in data.items():
            result += (calculate_structure_sum(value) + calculate_structure_sum(key))
    if isinstance(data, str):
        result += len(data)
    if isinstance(data, int):
        result += data
    return result


result = calculate_structure_sum(data_structure)
print(result)

