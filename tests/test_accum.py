import pytest
from stuff.accum import Accumulator

def test_accumulator_init(): #verifies that the new instance of the Accumulator class has a starting count of zero.
  accum = Accumulator()
  assert accum.count == 0


def test_accumulator_add_one(): #verifies that the add() method adds one to the internal count when it is called with no other arguments
  accum = Accumulator()
  accum.add()
  assert accum.count == 1


def test_accumulator_add_three(): #verifies that the add() method adds 3 to the count when it is called with the argument of 3.
  accum = Accumulator()
  accum.add(3)
  assert accum.count == 3


def test_accumulator_add_twice(): #verifies that the count increases appropriately with multiple add() calls
  accum = Accumulator()
  accum.add()
  accum.add()
  assert accum.count == 2


def test_accumulator_cannot_set_count_directly(): #verifies that the count attribute cannot be assigned directly because it is a read-only property. Notice how we use pytest.raises to verify the attribute error.
  accum = Accumulator()
  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    accum.count = 10

#Arrange assets for the test (like a setup procedure).

#Act by exercising the target behavior.

#Assert that expected outcomes happened.