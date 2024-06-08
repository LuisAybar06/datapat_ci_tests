def process_numbers(a, b, c, d, e, f):
    # Realiza varias operaciones con los números
    sum_all = a + b + c + d + e + f
    product_all = a * b * c * d * e * f
    average = sum_all / 6
    max_num = max(a, b, c, d, e, f)
    min_num = min(a, b, c, d, e, f)
    
    result = {
        'sum': sum_all,
        'product': product_all,
        'average': average,
        'max': max_num,
        'min': min_num
    }
    return result
