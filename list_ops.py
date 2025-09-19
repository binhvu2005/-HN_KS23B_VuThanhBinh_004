
"""Module chứa các hàm xử lý danh sách."""

from typing import List, TypeVar

T = TypeVar('T')


def remove_duplicates(input_list: List[T]) -> List[T]:
    """
    Loại bỏ các phần tử trùng lặp trong danh sách.
    
    Hàm này tạo ra một danh sách mới chứa các phần tử duy nhất từ danh sách đầu vào,
    giữ nguyên thứ tự xuất hiện đầu tiên của mỗi phần tử.
    
    Args:
        input_list (List[T]): Danh sách đầu vào chứa các phần tử có thể trùng lặp.
        
    Returns:
        List[T]: Danh sách mới chứa các phần tử duy nhất, giữ nguyên thứ tự.
        
    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    unique_items = []
    
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)
    
    return unique_items


if __name__ == "__main__":
    # Example usage
    test_data = [1, 2, 2, 3, 4, 4, 5]
    result = remove_duplicates(test_data)
    print(f"Original list: {test_data}")
    print(f"List after removing duplicates: {result}")
