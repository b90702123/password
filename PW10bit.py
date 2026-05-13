import hashlib
import base64
import pyperclip

def multi_sha1_base64(input_str, iterations=10):
    current_hash = input_str.encode('utf-8')
    
    for _ in range(iterations):
        sha1 = hashlib.sha1()
        sha1.update(current_hash)
        current_hash = sha1.digest()

    return base64.b64encode(current_hash).decode('utf-8')

# 用戶輸入
user_input = input("請輸入要處理的字串: ")

# 執行10次哈希+Base64轉換
result = multi_sha1_base64(user_input)
result10bit = str(result [18:28])
print("最終輸出:", result10bit)
pyperclip.copy(result10bit)
input()