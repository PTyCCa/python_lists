"""Implement enlarge (), which takes an image as a two-dimensional list of strings and doubles it, that is, doubles each character horizontally and vertically."""  # noqa E301


def enlarge(image):
    output = []
    for line in image:
        row = []
        for pixel in line:
            # expand horizontally
            row.extend([pixel, pixel])
        row = ''.join(row)
        # expand verticaly
        output.extend([
            row,
            row,
        ])
    return output

# Version 1
# def enlarge(image):
#    result = []
#    for line in image:
#        enlarged_row = []
#        for pixel in line:
#            enlarged_row.append(pixel * 2)
#        result.append(''.join(enlarged_row))
#        result.append(''.join(enlarged_row))
#    return result
