# Дан массив целых чисел nums и целое число target. Написать функцию, возвращающую индексы элементов,
# дающих в сумме число target?

class For_indexing_sums(object):
    def sums_indexes(self, nums, target):
        # Создаем пустой словарь, куда помещается список nums
        required = {}
        # Делаем цикл, которой возвращает индексы чисел суммы числа targen
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


# Проверочные данные
input_list = [2, 8, 12, 15]
obj_for_class = For_indexing_sums()
print(obj_for_class.sums_indexes(input_list, 20))

# # Предполагается, что в каждом массиве имеется не больше одной пары дающих в сумме заданное число target.
# # Нельзя использовать один и тот же элемент дважды?
def search_pairs(Mylist, target):
#     #Создаем пустой список pairs, куда будем помещать пары
    pairs = []
#     #Cоздаем два цикла проверяющих два соседних числа из всего переданного списка myList,если их сумма равна
#     #числу target их их нет в списке pairs, добавляем полученную пару в список, при наличии больше двух чисел прерываем
#     #цикл
    for i in range(len(Mylist)):
        for i2 in range(i + 1, len(Mylist)):
            if Mylist[i] + Mylist[i2] == target:
                if (Mylist[i], Mylist[i2]) not in pairs and (Mylist[i2], Mylist[i]) not in pairs:
                   #Лучше не смог придумать)
                    pairs.append(Mylist[i])
                    pairs.append(Mylist[i2])
        if len(pairs)>=2:
            break
    return pairs
#
# #Данные для проверки работоспособности кода
Mylist=[2,7,11,15,3,4,5,6,8,9]
target=int(input())
print(search_pairs(Mylist,target))
