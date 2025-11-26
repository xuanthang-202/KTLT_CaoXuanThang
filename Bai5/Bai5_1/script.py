print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import mymath
import mymath as mt

values = [2, 4, 6, 8, 10]

print('--- Using original module name (mymath) ---')
print('Squares:')
for v in values:
    print(mymath.square(v))

print('\nCubes:')
for v in values:
    print(mymath.cube(v))

print('\nAverage: ' + str(mymath.average(values)))

print('\n--- Using module alias (mt) ---')
print('Square of 2:', mt.square(2))
print('Cube of 3:', mt.cube(3))
