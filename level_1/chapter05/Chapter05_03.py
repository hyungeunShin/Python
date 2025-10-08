# package

import sys
import os

# 현재 파일 기준으로 상위 폴더(level_1)를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# print(sys.path)

# 예제1
import sub.sub1.module1
import sub.sub2.module2

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()
m2.mod2_test1()
m2.mod2_test2()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()
module2.mod2_test1()
module2.mod2_test2()
print()