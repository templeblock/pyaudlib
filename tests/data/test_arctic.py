"""Test the ARCTIC dataset."""
from audlib.data.arctic import ARCTIC1


def test_arctic():
    arctic = ARCTIC1('/home/xyy/data/ARCTIC', egg=True)
    print(arctic)
    for ii, elem in enumerate(arctic):
        pass


if __name__ == "__main__":
    test_arctic()