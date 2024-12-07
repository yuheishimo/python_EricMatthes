first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

# 出力結果はada lovelace
print(full_name)
# 出力結果はhello ada lovelace!
print(f"hello {full_name}!")

message = f"hello {full_name}!"
# 出力結果はhello ada lovelace!
print(message)


url = "https://nostarch.com"
# 上記のhttps:// 部分削除
url.removeprefix('https://')
# 新しい値を保持
simple_url = url.removeprefix('https://')