def remove_duplicates_ordered(string):
    """
    Remove duplicate characters from a string while maintaining the original order.
    
    Args:
        string (str): Input string to remove duplicates from
    
    Returns:
        str: String with duplicates removed, maintaining original order
    
    Example:
        >>> remove_duplicates_ordered("hello")
        'helo'
        >>> remove_duplicates_ordered("programming")
        'progamin'
    """
    # Using dict.fromkeys() to maintain order (Python 3.7+)
    return "".join(dict.fromkeys(string))


def remove_duplicates_set(string):
    """
    Remove duplicate characters from a string using set (does not maintain order).
    
    Args:
        string (str): Input string to remove duplicates from
    
    Returns:
        str: String with duplicates removed, order not guaranteed
    
    Example:
        >>> remove_duplicates_set("hello")
        'helo'  # Order might vary
        >>> remove_duplicates_set("programming")
        'progamin'  # Order might vary
    """
    return "".join(set(string))


def remove_duplicates_loop(string):
    """
    Remove duplicate characters from a string using a loop approach.
    This is more verbose but helps understand the logic.
    
    Args:
        string (str): Input string to remove duplicates from
    
    Returns:
        str: String with duplicates removed, maintaining original order
    
    Example:
        >>> remove_duplicates_loop("hello")
        'helo'
        >>> remove_duplicates_loop("programming")
        'progamin'
    """
    result = ""
    seen = set()
    
    for char in string:
        if char not in seen:
            seen.add(char)
            result += char
    
    return result


def remove_duplicates_list_comprehension(string):
    """
    Remove duplicate characters from a string using list comprehension.
    
    Args:
        string (str): Input string to remove duplicates from
    
    Returns:
        str: String with duplicates removed, maintaining original order
    
    Example:
        >>> remove_duplicates_list_comprehension("hello")
        'helo'
        >>> remove_duplicates_list_comprehension("programming")
        'progamin'
    """
    seen = set()
    return "".join([char for char in string if not (char in seen or seen.add(char))])


# Example usage and testing
if __name__ == "__main__":
    test_strings = [
        "hello",
        "programming",
        "python",
        "mississippi",
        "aabbccdd",
        "",  # Empty string
        "a",  # Single character
        "aaa",  # All same characters
        "abcde"  # No duplicates
    ]
    
    print("Testing different approaches to remove duplicates:\n")
    
    for test_str in test_strings:
        print(f"Original string: '{test_str}'")
        print(f"Using ordered approach:     '{remove_duplicates_ordered(test_str)}'")
        print(f"Using set approach:         '{remove_duplicates_set(test_str)}'")
        print(f"Using loop approach:        '{remove_duplicates_loop(test_str)}'")
        print(f"Using list comprehension:   '{remove_duplicates_list_comprehension(test_str)}'")
        print("-" * 50) 