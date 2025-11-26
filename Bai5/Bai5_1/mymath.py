print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    sum_val = 0.0
    for v in values:
        sum_val += v
    return float(sum_val) / nvals
