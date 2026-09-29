# permite introducir una word e imprime el caracter del medio. supon que el usuario simempre introduce una word impar
word = input('enter a word')
mid = len(word) // 2
print(word[mid])

# permite introducir una word e imprime el caracter del medio. supon que el usuario simempre introduce una word par
word = input('enter a word')
mid = len(word) // 2
print(word[mid-1:mid+1])

