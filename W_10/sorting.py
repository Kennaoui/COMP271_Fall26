def bubble_sort(items: list[int]) -> None:​
    """Sort items in place, ascending (early-exit version)."""​
    n = len(items)​
    pass_num = 0
    swapped = True
    while pass_num < n-1 and swapped:​
      swapped = False​
      for j in range(n - 1 - pass_num):   # skip final suffix​
         if items[j] > items[j + 1]:​
           items[j], items[j + 1] = items[j + 1], items[j]​
           swapped = True​
      pass_num += 1
