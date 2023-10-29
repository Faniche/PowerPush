import tkinter as tk


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 创建一个窗口
    root = tk.Tk()

    # 创建联系人列表
    contact_list = tk.Listbox(root)
    contact_list.pack(side="left", fill="both", expand=True)

    # 创建聊天窗口
    chat_window = tk.Text(root)
    chat_window.pack(side="right", fill="both", expand=True)

    # 添加联系人
    for name in ["张三", "李四", "王五"]:
        contact_list.insert("end", name)


    # 绑定事件处理程序
    def on_contact_click(event):
        # 获取点击的联系人
        contact = contact_list.get(event.widget.curselection()[0])

        # 清空聊天窗口
        chat_window.delete("1.0", "end")

        # 添加聊天内容
        chat_window.insert("end", "你好，" + contact + "\n")


    # 绑定联系人列表的单击事件
    contact_list.bind("<Button-1>", on_contact_click)

    # 运行窗口
    root.mainloop()
