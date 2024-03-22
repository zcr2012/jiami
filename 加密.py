import tkinter
tk=tkinter.Tk()
tk.minsize(490,495)
tk.maxsize(490,495)
tk.title('加密与解密')

#加密
isencry=False #为了防止点击多次加密出现问题
#加密算法,参数：秘钥，文本
def encryption():
    key=inputkey.get()
    global isencry
    if len(key)>2 and len(key)<10 and isencry:
        text=inputtext.get(1.0,'end')
        text2=''
        #将key转化成ascii码列表
        newkey=[]
        for i in key:
            newkey.append(ord(i))
        ii=0
        for i in text:
            if ord(i)!=10:
                text2=text2+chr(ord(i)+newkey[ii])#关键部分，加密公式
            else:
                text2=text2+chr(10)
            ii=ii+1
            if ii>=len(newkey):
                ii=0
        inputtext.delete(1.0,'end')
        inputtext.insert('insert',text2)
    isencry=False
#修改文本触发
def ismodifytext(*o):
    global isencry
    isencry=True
tkinter.Label(tk,text='------------------------------------加 密------------------------------------').place(x=10,y=0)
#设置秘钥
tkinter.Label(tk,text="请输入3-9位的秘钥").place(x=10,y=30)
ik=tkinter.StringVar()
inputkey=tkinter.Entry(tk,textvariable=ik,width=36)
inputkey.place(x=150,y=30)
#输入要加密的文本
tkinter.Label(tk,text="请输入要加密的文本").place(x=10,y=60)
inputtext=tkinter.Text(tk,width=36,height=10)
inputtext.place(x=150,y=60)
inputtext.bind('<KeyRelease>',ismodifytext)
#点击加密
tkinter.Button(tk,text='点击加密',width=14,command=encryption).place(x=10,y=198)

#解密
isdecry=False #为了防止点击多次解密出现bug
#解密算法,参数：秘钥，文本
def decrypt():
    key=inputkey2.get()
    global isdecry
    if len(key)>2 and len(key)<10 and isdecry:
        text=inputtext2.get(1.0,'end')
        text2=''
        #将key转化成ascii码列表
        newkey=[]
        for i in key:
            newkey.append(ord(i))
        ii=0
        for i in text:
            if ord(i)!=10:
                text2=text2+chr(ord(i)-newkey[ii])#关键部分，解密公式
            else:
                text2=text2+chr(10)
            ii=ii+1
            if ii>=len(newkey):
                ii=0
        inputtext2.delete(1.0,'end')
        inputtext2.insert('insert',text2)
    isdecry=False
#修改文本触发
def ismodify2(*o):
    global isdecry
    isdecry=True
tkinter.Label(tk,text='------------------------------------解 密------------------------------------').place(x=10,y=250)
#设置秘钥
tkinter.Label(tk,text="请输入3-9位的秘钥").place(x=10,y=280)
ik2=tkinter.StringVar()
inputkey2=tkinter.Entry(tk,textvariable=ik2,width=36)
inputkey2.place(x=150,y=280)
#输入要解密的文本
tkinter.Label(tk,text="请输入要解密的文本").place(x=10,y=310)
inputtext2=tkinter.Text(tk,width=36,height=10)
inputtext2.place(x=150,y=310)
inputtext2.bind('<KeyRelease>',ismodify2)
#点击解密
tkinter.Button(tk,text='点击解密',width=14,command=decrypt).place(x=10,y=448)

tk.mainloop() #显示窗口