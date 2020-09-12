# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import sys
import socket
import threading

from tkinter import *
from tkinter.ttk import *

from tkinter.messagebox import *
from tkinter.scrolledtext import ScrolledText

class LoginFrame:
    def __init__(self, parent, f1, f2):

        self._target = None
        # 自定义组件里最好用一个frame包起来, 便于统一操作
        self._frame = Frame(parent)

        Label(self._frame, text="Host: ").grid(row=1, column=1, columnspan=2)
        self._host = Entry(self._frame)
        self._host.insert(END, socket.gethostname()+":8088")
        self._host.grid(row=1, column=3, columnspan=3)

        Label(self._frame, text="ID: ").grid(row=2, column=1, columnspan=2)
        self._id = Entry(self._frame)
        self._id.insert(END, '160')
        self._id.grid(row=2, column=3, columnspan=3)

        Button(self._frame, text='退出', command=lambda : f1(self)).grid(row=3, column=2, columnspan=2, pady=15)
        Button(self._frame, text='登陆', command=lambda : f2(self, self._target)).grid(row=3, column=4, columnspan=1, pady=15)

    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def pack_forget(self):
        self._frame.pack_forget()

    def get_host(self):
        host, port = self._host.get().split(':')
        return host, int(port)

    def get_id(self):
        return self._id.get()

    def set_target(self, target):
        self._target = target

class ChatFrame:
    def __init__(self, parent, thread, f):

        self._thread = thread

        self._frame = Frame(parent)
        self._text = ScrolledText(self._frame, state=DISABLED, width=50, height=20)
        self._text.pack()

        self._target = Entry(self._frame, width=5)
        self._target.pack(side=LEFT)

        self._message = Entry(self._frame, width=25)
        self._message.pack(side=LEFT)

        Button(self._frame, text='发送', command=lambda : f(self)).pack(side=RIGHT)

    def clear_content(self):
        # DISABLED状态不光用户不能编辑, delete, insert也无效
        self._text.configure(state=NORMAL)
        self._text.delete(1.0, END)
        self._text.configure(state=DISABLED)

    def get_content(self):
        return self._text.get(1.0, END)

    def add_content(self, value):
        self._text.configure(state=NORMAL)
        self._text.insert(END, value)
        self._text.configure(state=DISABLED)

    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def pack_forget(self):
        self._frame.pack_forget()

    def listen(self):
        thread = self._thread(self)
        thread.setDaemon(True)
        thread.start()

root = Tk()
root.geometry("+600+300")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def login_f1(self: LoginFrame):
    root.quit()

def login_f2(self: LoginFrame, target: ChatFrame):
    host, port = self.get_host()

    try:
        client.connect((host, port))
    except OSError:
        showerror("提示", "\n连接失败!")
        return

    client.send(self.get_id().encode('utf-8'))

    self.pack_forget()
    target.pack()
    target.listen()

class RecvThread(threading.Thread):
    def __init__(self, chatroom: ChatFrame):
        threading.Thread.__init__(self)
        self._chatroom = chatroom

    def run(self) -> None:
        while True:
            data = client.recv(1024)
            if data:
                origin, message = data.decode('utf-8').split(':')
                self._chatroom.add_content(origin+': '+message+'\n')
            else:
                showerror('提示', '\n服务器断开连接')
                sys.exit()

def chat_f(self: ChatFrame):
    target = self._target.get()
    message = self._message.get()
    self.add_content("->"+target+": "+message+"\n")
    client.send((target+":"+message).encode('utf-8'))

login_frame = LoginFrame(root, login_f1, login_f2)
login_frame.pack()
chat_frame = ChatFrame(root, RecvThread, chat_f)
login_frame.set_target(chat_frame)

root.mainloop()

