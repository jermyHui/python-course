#-*-coding:gb2312-*-

# ͨ������������ҳ�����a��b��c�е����ֵ
# �������a��b��c
a = 10
b = 30
c = 20
# �ҳ�a��b�нϴ��ֵ���Ƹ�����d
d = a if a > b else b
# �Ƚ�d��c�Ĵ�С����������Ƹ�����max
max = c if c > d else d
# ���max
print(max)