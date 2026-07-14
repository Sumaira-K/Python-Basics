from Hello import hello
def test_default():
    #hello("Sumaira") == "Hello, Sumaira"
    assert hello() == "Hello, World!"

def test_arguement():
    for name in ["Hermoine", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"
   