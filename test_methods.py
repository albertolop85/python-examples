from methods import sum, write, calculator
import pytest

def test_sum () :
    assert sum(2,2) == 4

@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        (1,2,3),
        (2,4,6),
        (3,6,9)
    ] 
)
def test_parametrized_sum(input1, input2, expected) :
    assert sum(input1, input2) == expected

def test_temp_dir(tmpdir) :

    data = "texto"
    fpath = f"{tmpdir}/test.txt"
    write(fpath, data)

    with open(fpath) as file_out :
        data_file = file_out.read()

    assert data == data_file

def test_calculator_sum(monkeypatch) :
    monkeypatch.setattr(calculator, "sum", lambda x, y : 4)
    calc = calculator()
    assert calculator.sum(2, 7) == 4