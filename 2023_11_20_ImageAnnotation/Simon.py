import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_positions(rows, cols):

    # Divide image into different boxes
    x = np.linspace(0, 1, cols + 1)
    y = np.linspace(0, 1, rows + 1)

    # get position of upper right corner of each box (10% margin)
    positions = np.empty((rows, cols, 2))
    for row in range(rows):
        y_top_right = y[row] + 0.9/rows
        for col in range(cols):
            x_top_right = x[col] + 0.9/cols
            positions[row, col] = [x_top_right, y_top_right]

    return positions

def annotate_image(image, rows, cols, text):
    # read image
    img = mpimg.imread(image)

    # create figure with same size as input image
    img_width, img_height = img.shape[1], img.shape[0]
    fig, ax = plt.subplots(figsize=(img_width / 100, img_height / 100), tight_layout={'pad': 0})

    # scale fontsize to image width
    fontsize = 50*img_width/3072

    # plot text into upper right corner of each box
    positions = get_positions(rows, cols)
    for row in range(rows):
        for col in range(cols):
            position = positions[row, col]
            ax.text(position[0], position[1], text[col], horizontalalignment='right', verticalalignment='top',
                    transform=ax.transAxes, fontsize=fontsize, color='white', fontname='Comic Sans MS')

    # plot image
    ax.imshow(img, interpolation='none')
    ax.axis('off')

    # save image
    plt.savefig(image[0:-4] + '_annotated.png')

    return

def get_time_stamps(start_time, number_of_increments, increment):
    # split hours and minutes
    hours, minutes =  map(int, start_time.split(':'))

    # define function to write times in '*(h)h:mm' format
    time = lambda hours, minutes: str(hours) + ':' + str(minutes).zfill(2) + 'h'

    # calculate time for each increment
    time_stamps = [time(hours + (minutes + increment*i)//60, (minutes + increment*i)%60) for i in range(number_of_increments)]
   
    return time_stamps

# Beispiel 1
time_stamps = get_time_stamps('5:35', 6, 10)
annotate_image('testimage1.png', 3, 6, time_stamps)

# Beispiel 2
time_stamps = get_time_stamps('1:55', 5, 7)
annotate_image('testimage2.png', 4, 5, time_stamps)