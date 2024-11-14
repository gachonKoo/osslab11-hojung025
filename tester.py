import geo.utils as utils

# calculate the length of hypotenuse (c) when a = 3 and b = 4
a, b = 3, 4
c = utils.pythagoras(a, b)  # geo.utils의 함수를 이용해 c 계산
print('c =', c)

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle(r)  # geo.utils의 함수를 이용해 원의 면적 계산
print('area =', area)

