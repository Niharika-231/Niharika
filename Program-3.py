def generate_custom_series(a: int):
    limit = a if a % 2 != 0 else a - 1  # Use a-1 if even, else a
    series = []
    for i in range(limit):
        series.append(2 * i + 1)
    return series

# Example usage
if __name__ == "__main__":
    a = int(input("Enter a value: "))
    result = generate_custom_series(a)
    print("Output:", ", ".join(map(str, result)))
