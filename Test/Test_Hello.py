from Hello import hello
def test_default():
    #hello("Sumaira") == "Hello, Sumaira"
    assert hello() == "Hello, World!"

def test_arguement():
    assert hello("Sumaira") == "Hello, Sumaira"