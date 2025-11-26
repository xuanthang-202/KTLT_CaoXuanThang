def bubbleSort(nlist):
    """
    Thực hiện thuật toán sắp xếp nổi bọt (Bubble Sort) trên danh sách nlist.
    """
    n = len(nlist)
    # Lặp qua tất cả các phần tử của danh sách
    for passnum in range(n - 1, 0, -1):
        swapped = False
        # Lặp để so sánh các cặp phần tử
        for i in range(passnum):
            # So sánh các phần tử kề nhau
            if nlist[i] > nlist[i + 1]:
                # Đổi chỗ
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp
                swapped = True        
        # Nếu không có sự đổi chỗ nào trong một lần lặp (pass),
        # danh sách đã được sắp xếp và có thể thoát khỏi vòng lặp ngoài
        if not swapped:
            break  
    return nlist
