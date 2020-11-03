import argparse
import numpy as np
from PIL import Image

# 70 levels of gray
grey_scale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
grey_scale10 = '@%#*+=-:. '


def get_average_luminescence(image):
    img = np.array(image)
    width, height = img.shape
    return np.average(img.reshape(width * height))


def convert_image(file_name, columns, scale, wider_scale, reverse_luminescence):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    global grey_scale70, grey_scale10
    image = Image.open(file_name).convert('L')
    width, height = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (width, height))
    w = width / columns
    h = w / scale
    rows = int(height / h)

    print("cols: %d, rows: %d" % (columns, rows))
    print("tile dims: %d x %d" % (w, h))

    if columns > width or rows > height:
        print("Image too small for specified cols!")
        exit(0)

    ascii_image = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = height
        ascii_image.append("")
        for i in range(columns):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == columns - 1:
                x2 = width
            img = image.crop((x1, y1, x2, y2))
            if reverse_luminescence:
                average = abs(255 - int(get_average_luminescence(img)))
            else:
                average = int(get_average_luminescence(img))
            if wider_scale:
                grey_scale_value = grey_scale70[int((average * 69) / 255)]
            else:
                grey_scale_value = grey_scale10[int((average * 9) / 255)]
            ascii_image[j] += grey_scale_value

    return ascii_image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='image_file', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--cols', dest='columns', required=False)
    parser.add_argument('--deeper', dest='wider_scale', action='store_true')
    parser.add_argument('--rev', dest='reverse_luminescence', action='store_true')
    args = parser.parse_args()

    image_file = args.image_file
    output_file = '%s.txt' % (str(image_file)[:-4])
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    columns = 80
    if args.columns:
        columns = int(args.columns)

    print('generating ASCII art...')
    ascii_image = convert_image(image_file, columns, scale, args.wider_scale, args.reverse_luminescence)

    file = open(output_file, 'w')
    for row in ascii_image:
        file.write(row + '\n')
    file.close()
    print("ASCII art written to %s" % output_file)


if __name__ == '__main__':
    main()
