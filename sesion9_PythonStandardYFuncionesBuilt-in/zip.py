# Zip agrega iterables en una tupla y los devuelve

cursos = ['java', 'python', 'git', 'otra cosa'] # 'otra cosa' no aparecerá en el resultado porque no lo puede asociar
asistentes = [15, 20, 4]

demo = zip(cursos, asistentes)
print(f'Tipo de dato que devuelve: {type(demo)}, es en definitiva una lista con tuplas en el interior')
print(list(demo))