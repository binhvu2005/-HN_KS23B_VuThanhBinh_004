# Hướng dẫn sử dụng hàm remove_duplicates

## Mô tả tổng quan

Hàm `remove_duplicates` là một hàm Python được thiết kế để loại bỏ các phần tử trùng lặp trong một danh sách (list) và trả về một danh sách mới chứa các phần tử duy nhất. Hàm này giữ nguyên thứ tự xuất hiện ban đầu của các phần tử trong danh sách gốc.

## Tham số

- **my_list** (list): Danh sách đầu vào chứa các phần tử có thể trùng lặp
  - Kiểu dữ liệu: list
  - Bắt buộc: Có
  - Mô tả: Danh sách cần loại bỏ các phần tử trùng lặp

## Giá trị trả về

- **unique_items** (list): Danh sách mới chứa các phần tử duy nhất
  - Kiểu dữ liệu: list
  - Mô tả: Danh sách đã loại bỏ các phần tử trùng lặp, giữ nguyên thứ tự ban đầu

## Ví dụ minh họa

### Ví dụ 1: Loại bỏ số trùng lặp
```python
# Đầu vào
my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print(result)
# Kết quả: [1, 2, 3, 4, 5]
```

### Ví dụ 2: Loại bỏ chuỗi trùng lặp
```python
# Đầu vào
fruits = ["táo", "chuối", "táo", "cam", "chuối", "nho"]
unique_fruits = remove_duplicates(fruits)
print(unique_fruits)
# Kết quả: ["táo", "chuối", "cam", "nho"]
```

### Ví dụ 3: Danh sách không có phần tử trùng lặp
```python
# Đầu vào
numbers = [10, 20, 30, 40, 50]
result = remove_duplicates(numbers)
print(result)
# Kết quả: [10, 20, 30, 40, 50]
```

### Ví dụ 4: Danh sách rỗng
```python
# Đầu vào
empty_list = []
result = remove_duplicates(empty_list)
print(result)
# Kết quả: []
```

## Lưu ý quan trọng

1. **Giữ nguyên thứ tự**: Hàm giữ nguyên thứ tự xuất hiện đầu tiên của mỗi phần tử
2. **Không thay đổi danh sách gốc**: Hàm tạo ra một danh sách mới, không sửa đổi danh sách đầu vào
3. **Tương thích với mọi kiểu dữ liệu**: Hàm hoạt động với các phần tử có thể so sánh được (số, chuỗi, tuple, v.v.)
4. **Độ phức tạp thời gian**: O(n²) trong trường hợp xấu nhất do sử dụng toán tử `in` với list

## Cách sử dụng

```python
# Import hoặc định nghĩa hàm
def remove_duplicates(my_list):
    unique_items = []
    for item in my_list:
        if item not in unique_items: 
            unique_items.append(item)
    return unique_items

# Sử dụng hàm
my_data = [1, 2, 2, 3, 4, 4, 5]
cleaned_data = remove_duplicates(my_data)
print(f"Danh sách gốc: {my_data}")
print(f"Danh sách đã loại bỏ trùng lặp: {cleaned_data}")
```
