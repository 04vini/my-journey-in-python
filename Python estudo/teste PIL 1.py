from PIL import Image

nome = input("Digite um nome: ");

if (nome == "Paulo"):
    Image = Image.open("./Paulo.png");
    Image.show();
else:
    Image = Image.open ("./Marcos.png");
    Image.show();
