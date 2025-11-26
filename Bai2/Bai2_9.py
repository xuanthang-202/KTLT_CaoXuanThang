print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
s = input("Enter a string: ")
d = {}

for ch in s:
    d[ch] = s.count(ch)

print(d)
