"""Intiger to bin convertor"""


def convert(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not (0 <= n <= 100):
        raise ValueError("n must be between 0 and 100")

    return bin(n)[2:]
