frase_longa = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum."""

frase = 'Curso em Video Python'
dividido = frase.split()
print(frase[3:13])
print(frase[:13])
print(frase[::2])
print(len(frase))
print(f'frase dividida ', dividido[2][3])
print(frase.replace('Python', 'Android'))
