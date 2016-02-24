def read_and_remove_duplicates(filename):
    f = open(filename, 'r')

    lines = []
    for line in f:
        lines.append(line[0:10])

    set_lines = set(lines)
    print set_lines
    print len(set_lines)
    return set_lines

filename="valid_dates.js"
valid_dates = read_and_remove_duplicates(filename)

filename="all_dates.js"
all_dates = read_and_remove_duplicates(filename)

print list(all_dates - valid_dates)
