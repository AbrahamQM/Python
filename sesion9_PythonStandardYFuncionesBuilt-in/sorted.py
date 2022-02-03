lista = ['z', 'c', 'd', 'a']
print(f'lista: {lista}, sorted(lista): {sorted(lista)}')
print(f'lista: {lista}, sorted(lista, reverse=True): {sorted(lista, reverse=True)}')
print(f'lista: {lista}, sorted(lista, reverse=True, key=lambda x: str(x).startswith("c")):'
      f'{sorted(lista, reverse=True, key=lambda x: str(x).startswith("c"))}')
# A esta última le hemos indicado reverse y, que muestre primero la que empieza por 'c'

