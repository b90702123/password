import base64
import hashlib
import tkinter as tk
from tkinter import messagebox
import pyperclip


# 核心處理函數：執行10次哈希+Base64轉換
def multi_sha1_base64(input_str, iterations=10):
    current_hash = input_str.encode("utf-8")

    for _ in range(iterations):
        sha1 = hashlib.sha1()
        sha1.update(current_hash)
        current_hash = sha1.digest()

    return base64.b64encode(current_hash).decode("utf-8")


# 執行計算 (加入 event=None 以便同時支援按鈕點擊與 Enter 鍵觸發)
def generate_hashes(event=None):
    user_input = entry_input.get()

    # 計算結果
    full_result = multi_sha1_base64(user_input)
    short_result = str(full_result[18:28])  # 截取 18:28 的字元

    # 更新 UI 上的完整輸出欄位
    entry_full.config(state="normal")  # 解除唯讀以寫入
    entry_full.delete(0, tk.END)
    entry_full.insert(0, full_result)
    entry_full.config(state="readonly")  # 設回唯讀防止誤改

    # 更新 UI 上的截取輸出欄位
    entry_short.config(state="normal")
    entry_short.delete(0, tk.END)
    entry_short.insert(0, short_result)
    entry_short.config(state="readonly")

    # 【新增】預設自動複製「完整輸出」至剪貼簿
    pyperclip.copy(full_result)

    # 更新狀態提示
    status_label.config(text="計算完成！已自動複製「完整輸出」。", fg="blue")


# 手動複製功能函數 (保留給按鈕使用)
def copy_to_clipboard(target_entry, label_name):
    content = target_entry.get()
    if content:
        pyperclip.copy(content)
        status_label.config(
            text=f"已成功手動複製 {label_name}！", fg="#4CAF50"
        )
    else:
        messagebox.showwarning("警告", "沒有可複製的內容，請先執行計算！")


# --- 以下為 GUI 視窗介面設定 ---

# 建立主視窗
root = tk.Tk()
root.title("PassWord 多重轉換工具")
root.geometry("480x250")
root.resizable(False, False)  # 固定視窗大小

# 視窗內邊距設定
frame = tk.Frame(root, padx=20, pady=15)
frame.pack(fill="both", expand=True)

# 1. 使用者輸入區
tk.Label(frame, text="請輸入要處理的字串:").grid(
    row=0, column=0, sticky="w", pady=5
)
entry_input = tk.Entry(frame, width=35)
entry_input.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
entry_input.focus()  # 啟動時游標直接定位在此

# 【新增】綁定 Enter 鍵觸發計算
entry_input.bind("<Return>", generate_hashes)

# 2. 執行按鈕
btn_generate = tk.Button(
    frame, text="執行Hash計算", command=generate_hashes, bg="#4CAF50", fg="white"
)
btn_generate.grid(row=1, column=0, columnspan=3, pady=10, sticky="we")

# 分隔線
tk.Frame(frame, height=2, bd=1, relief="sunken").grid(
    row=2, column=0, columnspan=3, sticky="we", pady=10
)

# 3. 第一段程式結果 (完整輸出)
tk.Label(frame, text="完整輸出:").grid(row=3, column=0, sticky="w", pady=5)
entry_full = tk.Entry(frame, width=30, state="readonly")
entry_full.grid(row=3, column=1, padx=5, pady=5)
btn_copy_full = tk.Button(
    frame,
    text="複製",
    command=lambda: copy_to_clipboard(entry_full, "「完整輸出」"),
)
btn_copy_full.grid(row=3, column=2, padx=5, pady=5)

# 4. 第二段程式結果 (截取 18:28)
tk.Label(frame, text="截取輸出 (10bit):").grid(
    row=4, column=0, sticky="w", pady=5
)
entry_short = tk.Entry(frame, width=30, state="readonly")
entry_short.grid(row=4, column=1, padx=5, pady=5)
btn_copy_short = tk.Button(
    frame,
    text="複製",
    command=lambda: copy_to_clipboard(entry_short, "「截取輸出」"),
)
btn_copy_short.grid(row=4, column=2, padx=5, pady=5)

# 5. 狀態提示區
status_label = tk.Label(
    frame, text="請輸入字串並按 Enter 鍵直接執行。", fg="gray"
)
status_label.grid(row=5, column=0, columnspan=3, pady=10)

# 啟動主迴圈
root.mainloop()