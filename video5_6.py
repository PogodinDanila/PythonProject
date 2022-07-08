def print_info(object_name='unknown object', color='white', price='0'):
    print('Object:', object_name, sep='\t')
    print('Color:', color, sep='\t')
    print('Price:', price, sep='\t')
    print()

print_info('pen', 'blue')
print_info(color='red', price=3)