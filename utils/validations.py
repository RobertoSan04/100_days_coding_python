from typing import Union, Optional


def get_number(
    prompt: str, 
    number_type: type = float,
    min_value: Optional[Union[int, float]] = None, 
    max_value: Optional[Union[int, float]] = None
) -> Union[int, float]:
    """
    Get a valid number (int or float) from user input with optional range validation.
    
    Args:
        prompt: The message to display to the user
        number_type: The type of number to return (int or float)
        min_value: Optional minimum value (inclusive)
        max_value: Optional maximum value (inclusive)
    
    Returns:
        The validated number as int or float
    
    Example:
        age = get_number("Enter your age: ", int, 0, 120)
        price = get_number("Enter price: $", float, 0.01)
        score = get_number("Enter score: ")  # No limits
    """
    while True:
        try:
            if number_type == int:
                value = int(input(prompt).strip())
            elif number_type == float:
                value = float(input(prompt).strip())
            else:
                raise ValueError("number_type must be int or float")
            
            if min_value is not None and value < min_value:
                if max_value is not None:
                    print(f"Please enter a number between {min_value} and {max_value}")
                else:
                    print(f"Please enter a number >= {min_value}")
                continue
                
            if max_value is not None and value > max_value:
                if min_value is not None:
                    print(f"Please enter a number between {min_value} and {max_value}")
                else:
                    print(f"Please enter a number <= {max_value}")
                continue
            
            return value
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print(f"Please enter a valid {number_type.__name__}")
            else:
                print(f"Error: {e}")


def get_positive_number(
    prompt: str, 
    number_type: type = float
) -> Union[int, float]:
    return get_number(prompt, number_type, min_value=0.01 if number_type == float else 1)

def get_int(prompt: str, min_value: Optional[int] = None, max_value: Optional[int] = None) -> int:
    return get_number(prompt, int, min_value, max_value)


def get_float(prompt: str, min_value: Optional[float] = None, max_value: Optional[float] = None) -> float:
    return get_number(prompt, float, min_value, max_value)


def get_positive_int(prompt: str) -> int:
    return get_number(prompt, int, min_value=1)


def get_positive_float(prompt: str) -> float:
    return get_number(prompt, float, min_value=0.01)