import pytest

def test_one_plus_one():
    assert 1+2==3
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

   # assert 'divison by zero' in str(e.value)

def test_multiply_by_three():
    a=5
    b=3
    a*b==15

    #DRY principle:Don't Repeat yourself
    #We use parametrized function to overcome this
    # --------------------------------------------
    # A  Parametrized test function example for multiplication-refer to chapter 4 intro to pytest(TAU)
    #-----------------


    #equivalence class for testcase inputs is a unique kind of input that yields a unique kind of output.
products= [ #tuple
        (2,3,6),        #positive integers
        (1,99,99),      #identity
        (0,99,0),       #zero
        (3,-4,-12),     #positive by negative
        (-5,-5,25),     #negative by negative
        (2.5,6.7,16.75) #floats
    ]
@pytest.mark.parametrize('a,b,product', products) #decorator for the test_multiplication function.decorator is a special function that wraps around another function  #pass 2 arguements                                               
def test_multiplication(a,b,product):
        assert a*b==product #this test will be run 6 times