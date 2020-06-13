import pyautogui as pg
import time

pg.FAILSAFE = False  # 防止出现崩溃
# sc = pg.screenshot()


# 根据输入的坐标，将鼠标移动至此处，并且点击左边左键
def click(x, y):
    pg.moveTo(x, y)
    pg.click()


# 输入截图，找到屏幕中与截图相似的位置，并且中心坐标
def get_button_center_from_screen(button1, puth1="C:\\Users\\autogen\\Desktop\\wzjb"):
    # pg.screenshot("screen.png")
    button_png = puth1 + "\\" + button1
    start_pos = pg.locateOnScreen(button_png)
    button_centre = pg.center(start_pos)
    return button_centre


def get_times():  # 自定义刷副本的次数
    a = input("请输入你要刷副本的次数：")
    return a


# 由于locateonscreen函数在搜索不到对应函数时，会报错，所以用try的形式不断循环访问，一旦得到坐标，立即返回坐标值
def get_xy(png_path):
    a = 1
    while True:
        try:
            x, y = get_button_center_from_screen(png_path)
        except:
            time.sleep(1)
            a = a + 1
            if a == 60:
                break
            continue
        else:
            break
    return x, y


# 开始根据关卡整合按键顺序
def automouse():
    print("开始")
    n = 1
    deadline = get_times()
    deadline = int(deadline)
    while n <= deadline:
        print("{now} 第{n}次\n".format(now=time.strftime("%m-%d %H:%M:%S"), n=n))
        # 开始进图，本程序选用 大师级刺秦之地、
        x, y = get_xy("chuangguan.png")
        if (x, y) != (0, 0):
            print("开始闯关")
            click(x, y)
        else:
            print("不好意思兄弟失败了！关闭吧。")
        # time.sleep(5)

        # 进图开始碰到阿珂，左上角有跳过按钮，取到x,y并且跳过
        x, y = get_xy("tiaoguo1.png")
        click(x, y)
        print("第一次跳过")
        # time.sleep(60)
        # print("60秒已醒")

        # 大约60s后打完怪，然后再次检验两次跳过并且点击
        x, y = get_xy("tiaoguo2.png")
        click(x, y)
        print("第二次跳过")
        x, y = get_xy("tiaoguo3.png")
        click(x, y)
        print("第三次跳过")

        # 选择重新开始点击任意继续
        # time.sleep(1)
        x, y = get_xy("jixu.png")
        click(x, y)

        # 点击再次闯关，进入下次循环
        print("重新开始")
        # time.sleep(1)
        print("第%d次闯关成功！" % n)
        x, y = get_xy("zaicitiaozhan.png")
        n = n + 1
        click(x, y)
        # time.sleep(1)


if __name__ == '__main__':
    automouse()
