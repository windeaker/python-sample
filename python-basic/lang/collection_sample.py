def list_sample():
    # 初始化
    l = [1, 313, 1, 31]
    l = list([1, 313, 1, 31])

    # 第一个
    firstone = l[0]
    print(firstone)
    # 最后一个 同理倒数第二个-2
    lastone = l[-1]
    print(lastone)
    l.append(-222)
    print(l)
    l.insert(1, 7890)
    print(l)
    var = l.pop()
    print(var)
    var = l.pop(1)
    print(var)
    print(l)
    l.insert(2, [1, 2, 3, 4, 56])
    print(l)
    print(len(l))
    print(l[2][3])
    # print(list[1][3]) 会抛异常 TypeError: 'int' object is not subscriptable
    l[1] = False
    print(l)
    l = []
    print("%s" % l)


# 元组，定长有序不可更改，类似于 Arrays.ArrayList
# 除了不能更改元素外，其余操作和list一致
def turple_sample():
    t = ('Michael', 'Bob', 'Tracy')
    print(t)
    # t[1]="1" 会报错
    # 空tuple
    t = ()
    print(t)
    # 一个元素
    t = (2,)
    print(t)
    # 2 这个数值，就是这个数
    t = (2)
    print(t)
    print(t * 3)
    # t内部的list的元素是可变的
    t = ('a', 'b', ['A', 'B'])
    print(t)
    t[2][0] = 'X'
    print(t)
    pass


# 字典 类似于java 的map
def dict_sample():
    # 初始化
    d1 = {}
    d2 = dict()
    d3 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d1)
    print(d2)
    print(d3)

    # 访问元素
    print(d3["Michael"])
    # 访问不存在的元素会报错如
    # d1["Michael"]
    # 正确访问元素的方式有
    print(d1.get('Thomas'))
    print(d1.get('Thomas', -1))
    pass

# 集合，不可重复，无序，与java set类似
def set_sample():
    # 初始化
    s = set([1, 2, 3])
    s = {1, 2, 3}
    print(s)

    s = set([1, 1, 2, 2, 3, 3])
    print(s)
    s.add(6)
    print(s)
    # s.remove(8) 删除不存在的元素会报错
    print(s)
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    # 交集
    print(s1 & s2)
    # 并集
    print(s1 | s2)
    pass


# list_sample()
# turple_sample()
# dict_sample()
set_sample()
