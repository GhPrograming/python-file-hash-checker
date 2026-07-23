import hashlib
path = "C:/Users/USER/Downloads/test.txt"
#destinatia/path -- loactia fisierului

with open(path, "rb") as file:
	continut = file.read()

file_hash = hashlib.sha256(continut).hexdigest()
if file_hash == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
	print("Fisier gol")

else:
	print(file_hash)
