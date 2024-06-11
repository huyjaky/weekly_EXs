def calc_levenshtein_distance_at_location(
    matrix_levenshtein,
    row,
    column,
    chars_source_list,
    chars_target_list,
):
    # NOTE: [row, column]

    # HACK: | replace | insert |
    #       | delete  | U hear |

    compare = []

    # NOTE: insert
    compare.append(matrix_levenshtein[row][column - 1])
    # NOTE: delete
    compare.append(matrix_levenshtein[row - 1][column])
    # NOTE: replace
    compare.append(matrix_levenshtein[row - 1][column - 1])

    # NOTE: if 2 chars equal return minimum against minimum plus 1
    if chars_source_list[row] == chars_target_list[column]:
        return min(compare)
    else:
        return min(compare) + 1


def levenshtein_distance(source_str="", target_str=""):

    source_str = "#" + source_str.strip()
    target_str = "#" + target_str.strip()

    chars_source_list = list(source_str)
    chars_target_list = list(target_str)

    # HACK: crate initial matrix_levenshtein [[0, 1, 2, 3], [1], [2]]
    matrix_levenshtein = [[count] for count, _ in enumerate(chars_source_list)]

    matrix_levenshtein[0] = [count for count, _ in enumerate(chars_target_list)]

    # HACK: count_down_char_source is ROW LOCATION
    #       count_down_char_target is COLUMN LOCATION

    # NOTE: row
    for count_down_char_source, char_source in enumerate(chars_source_list):

        # NOTE: refuse location 0
        if count_down_char_source == 0:
            continue

        # NOTE: column
        for count_down_char_target, char_target in enumerate(chars_target_list):

            if count_down_char_target == 0:
                continue

            matrix_levenshtein[count_down_char_source].append(
                calc_levenshtein_distance_at_location(
                    matrix_levenshtein=matrix_levenshtein,
                    row=count_down_char_source,
                    column=count_down_char_target,
                    chars_source_list=chars_source_list,
                    chars_target_list=chars_target_list,
                )
            )

    print(f'Minimum cost is {matrix_levenshtein[-1][-1]}')


def input_data():
    string1 = input('Enter string 1:')
    string2 = input('Enter string 2:')
    levenshtein_distance("yu", "you")
    levenshtein_distance(string1, string2)
