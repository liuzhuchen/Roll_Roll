import numpy as np
import tkinter as tk

roll = tk.Tk()
roll.title('Hasegawa Lab 吃饭Roll点专用')
roll.geometry('400x400')
l = tk.Label(roll,
    text='选择困难吃饭Roll点',    # 标签的文字
    bg='white',     # 背景颜色
    font=('Times New Roman', 20),     # 字体和字体大小
    width=400, height=2  # 标签长宽
    )
l.pack()

login_hit = False
sign_hit = False

def pushlogin():
    global login_hit
    if login_hit == False:
        login_hit = True
    else:
        login_hit = False

def pushsign():
    global sign_hit
    if sign_hit == False:
        sign_hit = True
    else:
        sign_hit = False

# user information
tk.Label(roll, text='User name: ').place(x=50, y= 120)#创建一个`label`名为`User name: `置于坐标（50,150）
tk.Label(roll, text='Password: ').place(x=50, y= 160)

usr_name = tk.StringVar()#定义变量
usr_name.set('fku@iis.u-tokyo.ac.jp')#变量赋值
entry_usr_name = tk.Entry(roll, textvariable=usr_name)#创建一个`entry`
entry_usr_name.place(x=160, y=120)
usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(roll, textvariable=usr_pwd, show='*')#`show`这个参数将输入的密码变为`***`的形式
entry_usr_pwd.place(x=160, y=160)

login_b = tk.Button(roll,
    text='登陆',      # 显示在按钮上的文字
    width=15, height=2,
    command=pushlogin)     # 点击按钮式执行的命令
login_b.place(x = 120, y = 200)    # 按钮位置

sign_b = login_b = tk.Button(roll,
    text='注册',      # 显示在按钮上的文字
    width=15, height=2,
    command=pushsign)     # 点击按钮式执行的命令
sign_b.place(x = 120, y = 240)    # 按钮位置


roll.mainloop()