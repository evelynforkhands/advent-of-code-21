def get_display_represented_by(n, digits):
    representation = [x for x in digits if len(list(set(x))) == n]
    return representation if len(representation) > 1 else representation[0]


def get_number_by_representation(representation, mapping):
    for key, value in mapping.items():
         if set(representation) == set(value):
             return key


def expand_str(str):
    return list(set(str))


def is_contained_in(representation, container):
    return set(representation).issubset(set(container))


def get_difference(a, b):
    difference = list(set(a).difference(set(b)))
    return difference if len(difference) > 1 else difference[0]


def mapping_for(segments):
    return [segments_mapping[x] for x in segments]


def decode_digits(digits):
    one = get_display_represented_by(2, digits)
    seven = get_display_represented_by(3, digits)
    eight = get_display_represented_by(7, digits)
    four = get_display_represented_by(4, digits)
    global segments_mapping
    segments_mapping = {'a': get_difference(seven, one), 'c': get_difference(eight, [dig for dig in
                                                                                     get_display_represented_by(6,
                                                                                                                digits)
                                                                                     if
                                                                                     not is_contained_in(seven, dig)][
        0])}

    zero_and_nine = [dig for dig in get_display_represented_by(6, digits) if is_contained_in(seven, dig)]
    zero = [dig for dig in zero_and_nine if not is_contained_in(get_display_represented_by(4, digits), dig)]
    nine = get_difference(zero_and_nine, zero)
    segments_mapping['d'] = get_difference(eight, zero[0])
    segments_mapping['e'] = get_difference(eight, nine)
    segments_mapping['f'] = get_difference(seven, set.union(set(segments_mapping['a']), set(segments_mapping['c'])))
    segments_mapping['g'] = get_difference(nine, set.union(set(four), segments_mapping['a']))
    segments_mapping['b'] = get_difference(eight, list(segments_mapping.values()))

    mapping = {0: expand_str(zero[0]), 1: expand_str(one), 2: mapping_for(['a', 'c', 'd', 'e', 'g']),
               3: mapping_for(['a', 'c', 'd', 'f', 'g']), 4: expand_str(four),
               5: mapping_for(['a', 'b', 'd', 'f', 'g']), 6: get_difference(eight, segments_mapping['c']),
               7: expand_str(seven), 8: expand_str(eight), 9: expand_str(nine)}
    return mapping


def read_input():
    f = open('inputs/input 8.txt', 'r')
    return f.read().split('\n')[:-1]


occurrence = 0

for line in read_input():
    map = decode_digits(line.split(' | ')[0].split(' '))
    occurrence += int(''.join([str(get_number_by_representation(x, map)) for x in line.split(' | ')[1].split(' ')]))


print(occurrence)
