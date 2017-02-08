[TOC]

# Algorithm

## Baisc

### Search



### Sort

#### Quick Sort

由 C.A.R.Hoare 在 1962 年提出。 通过一趟排序将要排序的数据分割成独立的两部分， 其中一部分的所有数据都要比另外一部分的所有数据都要小， 然后再按此方法对这两部分分别进行快速排序， 整个排序过程可以递归进行， 以此达到整个数据变成有序序列。 具体步骤如下：

- 设置两个变量i、j，排序开始的时候：i=0，j=N-1；
- 以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
- 从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
- 从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
- 重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。

Java 代码实现：

```java
static void quicksort(int n[], int left, int right) { // 对特殊值和边界值的检查，提高程序的鲁棒性
  if (n == null || left < 0) {
    return;
  }
  int dp;
  if (left < right) {
    dp = partition(n, left, right);
    quicksort(n, left, dp - 1);
    quicksort(n, dp + 1, right);
  }
}

static int partition(int n[], int left, int right) {
  int pivot = n[left];
  while (left < right) {
    while (left < right && n[right] >= pivot)
      right--;
    if (left < right)
      n[left++] = n[right];
    while (left < right && n[left] <= pivot)
      left++;
    if (left < right)
      n[right--] = n[left];
  }
  n[left] = pivot;
  return left;
}
```

**快速排序算法分析**：

- 算法是不稳定的
- 每层排序大约需要 O(n) 复杂度。 而一个长度为 n 的数组， 调用深度最多为 log(n) 层。 二者相乘， 得到快速排序的平均时间复杂度 O(nlogn)

**算法优化**：

我们很容易发现这个算法的缺陷：这就是在我们输入数据基本有序甚至完全有序的时候，这算法退化为冒泡排序，不再是O(n㏒n)，而是O(n^2)了。 我们可以在每次划分后比较两端的长度，并先对短的序列进行排序（目的是先结束这些栈以释放空间），可以将最大深度降回到O(㏒n)级别。

**算法使用场景**：

快速排序在大多数情况下都是适用的，尤其在数据量大的时候性能优越性更加明显。但是在必要的时候，需要考虑下优化以提高其在最坏情况下的性能。

**快速排序是否适合递归**： 

按照通常的理论，我们知道递归算法一般比较直观自然，容易理解和书写；而非递归算法一般更为晦涩，但是性能比递归算法更优良，因为其省去了大量的函数调用开销。 快速排序的Java非递归实现当然有，通常都是用自己实现的栈来模拟递归操作。但是我并不认为它们比递归的方式有极大的性能提升，反而丢失了可读性，晦涩难懂。因此，我个人不提倡使用非递归方式。