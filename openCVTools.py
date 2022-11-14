import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt


def safeLoad(pathToFile):
    '''
    OpenCV does no validation checks due to performance reasons.
    Therefore, this function checks if the image could be loaded
    '''
    img = cv.imread(pathToFile)
    if img is None:
        sys.exit("Image could not be loaded.")
    return img


# TODO Aufgabe 1
'''
Passen Sie die Funktion `imageStats(..)` so an, dass sie sowohl Grau- als auch Farbbilder korrekt anzeigt.
Erweitern Sie die Funktion zusätzlich so dass der Datentyp mit ausgegeben wird.
'''
def imageStats(img):
    '''
    Returns a few image statistics
    '''
    s = img.shape
    if len(s) == 3:
        data_type = str(type(img[0][0][0]))
        pre_out = f'Width: {s[1]}, Height: {s[0]}, Channels: {s[2]}, Datatype: '
    elif len(s) == 2:
        data_type = str(type(img[0][0]))
        pre_out = f'Width: {s[1]}, Height: {s[0]}, Channels: 1 (grayscale), Datatype: '
    idz = []
    for i in range(len(data_type)):
        if data_type[i] == "'":
            idz.append(i)

    return pre_out + f'{data_type[idz[0]+1:idz[1]]}'



# TODO Aufgabe 1
'''
Passen Sie die Funktion `showImage(..)` so an, dass sie sowohl Grau- als auch Farbbilder korrekt anzeigt.
'''
def showImage(title, originalImg, normalize, **kwargs):
    # default values
    add_callbacks = False
    contrast_buffers = 0
    for key, value in kwargs.items():
        if key == "add_callbacks":
            add_callbacks = value
        if key == "contrast_buffers":
           contrast_buffers = value

    print(imageStats(originalImg))
    s = originalImg.shape
    if len(s) == 3:
        img = originalImg.copy()
    elif len(s) == 2:
        img = cv.cvtColor(originalImg, cv.COLOR_GRAY2BGR)
    img = img[:,:,::-1]

    #### Einschub zu Aufgabe 5
    if normalize:
        idz =[]
        data_type = str(type(img[0][0][0]))
        for i in range(len(data_type)):
            if data_type[i] == "'":
                idz.append(i)
        if data_type[idz[0]+1:idz[1]] == "numpy.float64":
            img = img[:,:,:]*255
            img = img.astype(np.uint8)
        gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_16Bit = img.astype(np.int16)
        min_l = gray_scale.min()
        max_l = gray_scale.max()
        if contrast_buffers > 0:
            amount_per_luminance = [0 for i in range(max_l+1)]
            for y in range(len(gray_scale)):
                for x in range(len(gray_scale[0])):
                    amount_per_luminance[gray_scale[y][x]] += 1
            new_lower_luminance_boarder = min_l
            new_upper_luminance_boarder = max_l
            overall_px_cnt = len(img[0])*len(img)
            px_cnt = 0
            for i in range(max_l+1):
                px_cnt += amount_per_luminance[max_l-i]
                if px_cnt >= round(overall_px_cnt/100*contrast_buffers):
                    new_upper_luminance_boarder = max_l-i
                    break
            px_cnt = 0
            for i in range(max_l+1):
                px_cnt += amount_per_luminance[i]
                if px_cnt >= round(overall_px_cnt/100*contrast_buffers):
                    new_lower_luminance_boarder = i
                    break

            for y in range(len(gray_scale)):
                for x in range(len(gray_scale[0])):
                    optimized_l = (gray_scale[y][x]-new_lower_luminance_boarder)*(255/(new_upper_luminance_boarder-new_lower_luminance_boarder))
                    if optimized_l > 255:
                        optimized_l = 255
                    if gray_scale[y][x]*optimized_l <= 0:
                        img_16Bit[y][x] = [0,0,0]
                    else:
                        img_16Bit[y][x][0] = round(img[y][x][0]/gray_scale[y][x]*optimized_l)
                        img_16Bit[y][x][1] = round(img[y][x][1]/gray_scale[y][x]*optimized_l)
                        img_16Bit[y][x][2] = round(img[y][x][2]/gray_scale[y][x]*optimized_l)
            waiter = 0
        else:
            for y in range(len(gray_scale)):
                for x in range(len(gray_scale[0])):
                    optimized_l = (gray_scale[y][x]-min_l)*(255/(max_l-min_l))
                    if gray_scale[y][x] == 0:
                        img_16Bit[y][x] = [0,0,0]
                    else:
                        img_16Bit[y][x][0] = round(img[y][x][0]/gray_scale[y][x]*optimized_l)
                        img_16Bit[y][x][1] = round(img[y][x][1]/gray_scale[y][x]*optimized_l)
                        img_16Bit[y][x][2] = round(img[y][x][2]/gray_scale[y][x]*optimized_l)
                
        max_l_corr = img_16Bit.max()
        img_16Bit = img_16Bit[:,:,:]/max_l_corr*255
        img_corr = img_16Bit.astype(np.uint8)

        figure = plt.figure(title)
    
        # Zu Aufgabe 3.): callbacks müssen vor .show() hinzugefügt werden, weil sonst das Skript diese nicht vor Schließen des Bildes hinzufügt
        if add_callbacks:
            disco_id_move = figure.canvas.mpl_connect('motion_notify_event', mouse_move)
            disco_id_button = figure.canvas.mpl_connect('key_press_event', key_press)
            disco_id_click = figure.canvas.mpl_connect('button_press_event', lambda event: mouse_click(event, figure, disco_id_move, disco_id_button,disco_id_click))
            # Quelle für lambda event: https://stackoverflow.com/questions/24960910/how-can-i-pass-parameters-to-on-key-in-fig-canvas-mpl-connectkey-press-event
        
        ax_left = plt.subplot(121)
        ax_right = plt.subplot(122)
        ax_left.imshow(img)
        ax_right.imshow(img_corr)
        ax_right.get_xaxis().set_visible(False)
        ax_left.get_xaxis().set_visible(False)
        ax_right.get_yaxis().set_visible(False)
        ax_left.get_yaxis().set_visible(False)
        plt.show()
    ####
    else:
        figure = plt.figure(title)
        
        # Zu Aufgabe 3.): callbacks müssen vor .show() hinzugefügt werden, weil sonst das Skript diese nicht vor Schließen des Bildes hinzufügt
        if add_callbacks:
            disco_id_move = figure.canvas.mpl_connect('motion_notify_event', mouse_move)
            disco_id_button = figure.canvas.mpl_connect('key_press_event', key_press)
            disco_id_click = figure.canvas.mpl_connect('button_press_event', lambda event: mouse_click(event, figure, disco_id_move, disco_id_button,disco_id_click))
            # Quelle für lambda event: https://stackoverflow.com/questions/24960910/how-can-i-pass-parameters-to-on-key-in-fig-canvas-mpl-connectkey-press-event
        
        plt.imshow(img)
        plt.show()
    
    return 0

####
#  Zu Aufgabe 3.):
def mouse_move(event):
    x = event.xdata
    y = event.ydata
    if x is None or y is None:
        return False
    else:
        print(round(x), round(y))

def key_press(event):
    name = event.key
    print(name)

def mouse_click(event, fig, disc_move, disc_key, disc_click):
    name = event.button
    print(name)
    if str(name) == 'MouseButton.LEFT':
        fig.canvas.mpl_disconnect(disc_move)
        fig.canvas.mpl_disconnect(disc_key)
        fig.canvas.mpl_disconnect(disc_click)
    return 0
####

def showImageList(title, images, normalize, **kwargs):
    # default values
    add_callbacks = False
    arr_type = "row"
    bg_color = [255, 255, 255]
    spacing = [0.1, 0.1]
    # optional
    axes_off = True
    contrast_buffers = 0

    for key, value in kwargs.items():
        if key == "add_callbacks":
            add_callbacks = value   # False, True
        if key == "arrangement_type":
            arr_type = value        # "row", "column", "grid"
        if key == "bg_color_RGB":
            bg_color = value        # [R: 0-255, G: 0-255, B: 0-255]
        if key == "spacing":
            spacing = value         # [horizontal: 0.0-1.0, vertical: 0.0-1.0]
        if key == "axes_off":
            axes_off = value        # False, True
        if key == "contrast_buffers":
            contrast_buffers = value  # 0-50
    
    img_list = []
    if len(images) > 0:
        for originalImg in images:
            print(imageStats(originalImg))
            s = originalImg.shape
            if len(s) == 3:
                img = originalImg.copy()
            elif len(s) == 2:
                img = cv.cvtColor(originalImg, cv.COLOR_GRAY2BGR)
            img = img[:,:,::-1]
            if normalize:
                idz =[]
                data_type = str(type(img[0][0][0]))
                for i in range(len(data_type)):
                    if data_type[i] == "'":
                        idz.append(i)
                if data_type[idz[0]+1:idz[1]] == "numpy.float64":
                    img = img[:,:,:]*255
                    img = img.astype(np.uint8)
                gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                img_16Bit = img.astype(np.uint16)
                min_l = gray_scale.min()
                max_l = gray_scale.max()
                if contrast_buffers > 0:
                    amount_per_luminance = [0 for i in range(max_l+1)]
                    for y in range(len(gray_scale)):
                        for x in range(len(gray_scale[0])):
                            amount_per_luminance[gray_scale[y][x]] += 1
                    new_lower_luminance_boarder = min_l
                    new_upper_luminance_boarder = max_l
                    overall_px_cnt = len(img[0])*len(img)
                    px_cnt = 0
                    for i in range(max_l+1):
                        px_cnt += amount_per_luminance[max_l-i]
                        if px_cnt >= round(overall_px_cnt/100*contrast_buffers):
                            new_upper_luminance_boarder = max_l-i
                            break
                    px_cnt = 0
                    for i in range(max_l+1):
                        px_cnt += amount_per_luminance[i]
                        if px_cnt >= round(overall_px_cnt/100*contrast_buffers):
                            new_lower_luminance_boarder = i
                            break

                    for y in range(len(gray_scale)):
                        for x in range(len(gray_scale[0])):
                            optimized_l = (gray_scale[y][x]-new_lower_luminance_boarder)*(255/(new_upper_luminance_boarder-new_lower_luminance_boarder))
                            if optimized_l > 255:
                                optimized_l = 255
                            if gray_scale[y][x]*optimized_l <= 0:
                                img_16Bit[y][x] = [0,0,0]
                            else:
                                img_16Bit[y][x][0] = round(img[y][x][0]/gray_scale[y][x]*optimized_l)
                                img_16Bit[y][x][1] = round(img[y][x][1]/gray_scale[y][x]*optimized_l)
                                img_16Bit[y][x][2] = round(img[y][x][2]/gray_scale[y][x]*optimized_l)
                    waiter = 0
                else:        
                    for y in range(len(gray_scale)):
                        for x in range(len(gray_scale[0])):
                            optimized_l = (gray_scale[y][x]-min_l)*(255/(max_l-min_l))
                            if gray_scale[y][x] == 0:
                                img_16Bit[y][x] = [0,0,0]
                            else:
                                img_16Bit[y][x][0] = round(img[y][x][0]/gray_scale[y][x]*optimized_l)
                                img_16Bit[y][x][1] = round(img[y][x][1]/gray_scale[y][x]*optimized_l)
                                img_16Bit[y][x][2] = round(img[y][x][2]/gray_scale[y][x]*optimized_l)
                        
                max_l_corr = img_16Bit.max()
                img_16Bit = img_16Bit[:,:,:]/max_l_corr*255
                img = img_16Bit.astype(np.uint8)
            img_list.append(img)

        figure = plt.figure(title)
        #figure.delaxes()

        if add_callbacks:
            disco_id_move = figure.canvas.mpl_connect('motion_notify_event', mouse_move)
            disco_id_button = figure.canvas.mpl_connect('key_press_event', key_press)
            disco_id_click = figure.canvas.mpl_connect('button_press_event', lambda event: mouse_click(event, figure, disco_id_move, disco_id_button,disco_id_click))
            # Quelle für lambda event: https://stackoverflow.com/questions/24960910/how-can-i-pass-parameters-to-on-key-in-fig-canvas-mpl-connectkey-press-event
        

        for x in range(len(img_list)):
            if arr_type == "row":
                ax = plt.subplot(100+len(img_list)*10+x+1)
            elif arr_type == "column":
                ax = plt.subplot(len(img_list)*100+10+x+1)
            elif arr_type == "grid":
                root = int(np.ceil(np.sqrt(len(img_list))))
                row_num = int(np.ceil(len(img_list)/root))
                ax = plt.subplot(row_num*100+root*10+x+1)
            ax.imshow(img_list[x])
            if axes_off:
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
        plt.subplots_adjust(wspace= spacing[0], hspace= spacing[1])
        for c in range(len(bg_color)):
            bg_color[c] = bg_color[c]/255.0
        figure.set_facecolor(bg_color)

        #big_img = np.ndarray([0,0,3])
        #plt.imshow(big_img)
        
        plt.show()
    
    return 0