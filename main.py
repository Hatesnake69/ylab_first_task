import math


def distance_between_two(a: tuple[int, int], b: tuple[int, int]) -> float:
    # this function takes two coorditates and returns the distance between them
    return math.sqrt(math.pow(a[0]-b[0], 2) + math.pow(a[1]-b[1], 2))


list_of_path = []


def shortest_path_getter(example_dict: dict[str: tuple[int, int]], start: str) -> list:
    # this function searches for the shortest possible way of bypassing
    # all of the points and returns list of this points
    min_val = math.inf
    next_start = ''
    list_of_shit = [start]
    if len(example_dict) == 1:
        return list_of_shit
    for i_key in example_dict:
        if i_key != start:
            dist = distance_between_two(example_dict[i_key], example_dict[start])
            if dist < min_val:
                next_start = i_key
                min_val = dist
    example_dict.pop(start)
    return list_of_shit + shortest_path_getter(example_dict, next_start)


def string_former(example_list: list[str], example_dict: dict[str: tuple[int, int]]) -> str:
    # this function forms string with result
    string = f'{example_list[0]} {example_dict[example_list[0]]}'
    distance = 0
    for j in range(len(example_list) - 1):
        a = example_dict[example_list[j]]
        b = example_dict[example_list[j + 1]]
        distance += distance_between_two(a, b)
        string += f' ->  {example_list[j+1]} {b}[{distance}] '
    return string


if __name__ == '__main__':
    dest_dict = {
            "Почтовое отделение": (0, 2),
            "Ул.Грибоедова, 104 / 25": (2, 5),
            "Ул.Бейкер стрит, 221 б": (5, 2),
            "Ул.Большая Садовая, 302 - бис": (6, 6),
            "Вечнозелёная Аллея, 742": (8, 3)
        }
    list_of_path = shortest_path_getter(dest_dict.copy(), "Почтовое отделение")
    list_of_path += ['Почтовое отделение']
    print(string_former(list_of_path, dest_dict))
