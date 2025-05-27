nums = [2, 7, 11, 15]
target = 9
array_len = len(nums)

for i in range(array_len):
    # Copia de la lista original para no modificarla
    nums_copy = nums.copy()
    
    # Intercambia el primer número con el número en el índice i
    nums_copy[0], nums_copy[i] = nums_copy[i], nums_copy[0]
    
    # Ahora intenta sumar nums_copy[0] con los demás
    for j in range(1, array_len):
        if nums_copy[0] + nums_copy[j] == target:
            print(f'{nums_copy[0]} + {nums_copy[j]} = {target} (índices originales: {i} y {j})')
