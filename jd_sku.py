import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 创建主窗口
root = tk.Tk()
root.title("京东SKU好评率查询工具")

# 设置窗口大小和位置
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 设置主题颜色
BG_COLOR = "#f0f0f0"  # 背景色
BUTTON_BG = "#e0e0e0"  # 按钮背景色
BUTTON_FG = "#333333"  # 按钮文字颜色
FRAME_BG = "#ffffff"   # 框架背景色

# 配置根窗口
root.configure(bg=BG_COLOR)

# 创建主框架
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 创建标题标签
title_label = tk.Label(
    main_frame,
    text="京东SKU好评率查询工具",
    font=("Arial", 16, "bold"),
    bg=BG_COLOR,
    fg="#333333"
)
title_label.pack(pady=20)

# 创建内容框架
content_frame = tk.Frame(main_frame, bg=FRAME_BG, relief="solid", bd=1)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# 创建输入区域
input_frame = tk.Frame(content_frame, bg=FRAME_BG)
input_frame.pack(fill=tk.X, padx=20, pady=20)

# SKU输入框
sku_label = tk.Label(input_frame, text="SKU:", bg=FRAME_BG)
sku_label.pack(side=tk.LEFT, padx=5)
sku_entry = tk.Entry(input_frame, width=30)
sku_entry.pack(side=tk.LEFT, padx=5)

# 查询按钮
query_button = tk.Button(
    input_frame,
    text="查询",
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    relief="flat",
    padx=20
)
query_button.pack(side=tk.LEFT, padx=10)

# 创建结果显示区域
result_frame = tk.Frame(content_frame, bg=FRAME_BG)
result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 创建表格
columns = ("SKU", "总好评率", "当前好评率", "状态")
tree = ttk.Treeview(result_frame, columns=columns, show="headings", height=10)

# 设置列标题
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# 添加滚动条
scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# 放置表格和滚动条
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建底部状态栏
status_frame = tk.Frame(root, bg=BG_COLOR, relief="solid", bd=1)
status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

status_label = tk.Label(
    status_frame,
    text="就绪",
    bg=BG_COLOR,
    fg="#666666"
)
status_label.pack(side=tk.LEFT, padx=10, pady=5)

# 启动主循环
root.mainloop()