'''

    This is for styling the shadow texts

'''


def changeShadowColor(shadow, color):
    '''
    This is used to change the shadow color
    :param shadow: QGraphicsDropShadowEffect
    :param color: QColor
    :return:
    '''

    shadow.setColor(color)


def applyBlur(shadow, amount):
    '''
    This is to setBlurRadius to a widget
    :param shadow: QGraphicsDropShadowEffect
    :return:
    '''

    shadow.setBlurRadius(amount)


def positionShadow(shadow, x, y):
    '''
    This is to position the shadow
    :param shadow: QGraphicsDropShadowEffect
    :param x: int
    :param y: int
    :return:
    '''

    shadow.setXOffset(x)
    shadow.setYOffset(y)