from pynput import mouse

class MyException(Exception):pass

X = []
Y = []
NumberOfMouseClicks = 0
print('Click Origin')

def on_click(x, y, button, pressed):
    button = str(button)
    global NumberOfMouseClicks

    NumberOfMouseClicks = NumberOfMouseClicks + 1
    if NumberOfMouseClicks==1:
        print('Click Top Right')  
    if NumberOfMouseClicks==3:
        print('Click data points. Right-click to end.')
    
    X.append(x)
    Y.append(y)
    
    if button!='Button.left':
        raise MyException(button)


def plot_data(X, Y, Xmin, Xmax, Ymin, Ymax):
    import matplotlib.pyplot as plt

    plt.plot(X,Y,'b-')
    plt.xlim((Xmin, Xmax))
    plt.ylim((Ymin, Ymax))
    plt.show() 


def main(X,Y):
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            pass

    # drop duplicates
    X = X[::2]
    Y = Y[::2]

    # input boundaries
    Xmin = float(input('Input X-min: '))
    Xmax = float(input('Input X-max: '))
    Ymin = float(input('Input Y-min: '))
    Ymax = float(input('Input Y-max: '))

    # define scales from data
    origin = [X[0],Y[0]]
    topRight = [X[1],Y[1]]
    XminScale = origin[0]
    XmaxScale = topRight[0]
    YminScale = origin[1]
    YmaxScale = topRight[1]

    # drop extras
    X = X[2:-1]
    Y = Y[2:-1]

    # scale
    ## (old_value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min
    Xplot = [(i - XminScale) / (XmaxScale - XminScale) * (Xmax - Xmin) + Xmin for i in X]
    Yplot = [(i - YminScale) / (YmaxScale - YminScale) * (Ymax - Ymin) + Ymin for i in Y]

    # print outputs
    print('Origin:     {}'.format([round(i, 2) for i in origin]))
    print('Top Right:  {}'.format([round(i, 2) for i in topRight]))
    print('X: {}'.format([round(i, 2) for i in Xplot]))
    print('Y: {}'.format([round(i, 2) for i in Yplot]))

    # plot
    plot_data(Xplot, Yplot, Xmin, Xmax, Ymin, Ymax)


if __name__ == '__main__':
    main(X,Y)