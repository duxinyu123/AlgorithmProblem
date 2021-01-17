# 小根堆
class min_heap():
    def __init__(self):
        # 使用线性表存储堆数据，第一个位置不使用，用0填充

        self.__data = [0]

    # 往堆中插入数据

    def shift_up(self, l):
        i = 1
        while i <= len(l):
            self.__data.append(l[i-1])
            cur = i
            # 依次与父节点比较

            while cur > 1 and self.__data[cur] < self.__data[int(cur/2)]:
                self.__data[cur], self.__data[int(cur/2)] = self.__data[int(cur/2)], self.__data[cur]
                cur = int(cur/2)
            i += 1
        print(self.__data)

    # 从堆中取出当前最小元素

    def shift_down(self):
        result = []
        length = len(self.__data)
        i = length-1
        while i > 1:
            result.append(self.__data[1])
            self.__data[1] = self.__data[i]
            self.__data.pop()
            i -= 1
            cur = 1
            # 依次与左右子节点中较小的值比较

            while cur <= i:
                if 2*cur + 1 <= i:
                    # 左子节点 <= 右子节点

                    if self.__data[2*cur] <= self.__data[2*cur + 1]:
                        # cur > 左子节点时则交换，否则 break

                        if self.__data[cur] > self.__data[2 * cur]:
                            self.__data[cur], self.__data[2 * cur] = self.__data[2 * cur], self.__data[cur]
                            cur = 2 * cur
                        else:
                            break
                    # 左子节点 > 右子节点
                    else:
                        # cur > 右子节点时则交换，否则 break
                        if self.__data[cur] > self.__data[2 * cur + 1]:
                            self.__data[cur], self.__data[2 * cur + 1] = self.__data[2 * cur + 1], self.__data[cur]
                            cur = 2 * cur + 1
                        else:
                            break
                elif 2*cur <= i:
                    # cur > 左子节点时则交换，否则 break
                    if self.__data[cur] > self.__data[2 * cur]:
                        self.__data[cur], self.__data[2 * cur] = self.__data[2 * cur], self.__data[cur]
                        cur = 2 * cur
                    else:
                        break
                else:
                    break
        return result


if __name__ == '__main__':
    h = min_heap()
    h.shift_up([3,2,4,5,8,7,3,6,1,3,4,6,4,3,2,1,0,9,8,5,6,7,8,9])
    print(h.shift_down())



