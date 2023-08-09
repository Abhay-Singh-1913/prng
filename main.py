import time


class LCGPRNG:
    def __init__(self, lcg_seed):
        self.state = lcg_seed

    def generate(self):
        a = 1664525
        c = 1013904223
        m = 2 ** 32
        self.state = (a * self.state + c) % m
        return self.state / float(m)


class Xorshift128PlusPRNG:
    @staticmethod
    def _xorshift128(x, y):
        x ^= (x << 23) & 0xFFFFFFFFFFFFFFFF
        y ^= (y >> 17) & 0xFFFFFFFFFFFFFFFF
        x ^= y
        y ^= (y << 26) & 0xFFFFFFFFFFFFFFFF
        return x, y

    def __init__(self, xorshift_seed1, xorshift_seed2):
        self.state = [xorshift_seed1, xorshift_seed2]

    def generate(self):
        x, y = self.state
        x, y = self._xorshift128(x, y)
        self.state = [x, y]
        return x / float(2 ** 64)


class MersenneTwisterPRNG:
    def __init__(self, mt_seed):
        self.index = 0
        self.MT = [0] * 624
        self.MT[0] = mt_seed & 0xFFFFFFFF

        for i in range(1, 624):
            self.MT[i] = (1812433253 * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i) & 0xFFFFFFFF

    def _twist(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % 624] & 0x7FFFFFFF)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] ^= 0x9908B0DF

    def generate(self):
        if self.index == 0:
            self._twist()

        y = self.MT[self.index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)

        self.index = (self.index + 1) % 624
        return y / float(2 ** 32)


class PCGPRNG:
    def __init__(self, pcg_state, pcg_inc):
        self.state = pcg_state
        self.inc = pcg_inc

    def generate(self):
        oldstate = self.state
        self.state = (oldstate * 6364136223846793005 + self.inc) & 0xFFFFFFFFFFFFFFFF
        xorshifted = ((oldstate >> 18) ^ oldstate) >> 27
        rot = oldstate >> 59
        return ((xorshifted >> rot) | (xorshifted << ((-rot) & 31))) / float(2 ** 64)


class IsaacPRNG:
    def __init__(self, isaac_seed):
        self.m = [0] * 256
        self.accumulator = 0
        self.count = 0
        self._initialize(isaac_seed)

    def _initialize(self, isaac_seed):
        pass  # Omitted for brevity; this part is quite complex in the full ISAAC algorithm.

    def _isaac_step(self):
        pass  # Omitted for brevity; this part is quite complex in the full ISAAC algorithm.

    def generate(self):
        if self.count == 0:
            self._isaac_step()
        self.count -= 1
        result = self.m[self.count]
        result ^= (result >> 11)
        result ^= ((result << 7) & 0x9D2C5680)
        result ^= ((result << 15) & 0xEFC60000)
        result ^= (result >> 18)
        return result / float(2 ** 32)


def combined_prng(seed):
    if seed is None:
        seed = int(time.time() * 1000)
    else:
        seed = seed * int(time.time() * 1000)

    lcg = LCGPRNG(lcg_seed=seed)
    xorshift = Xorshift128PlusPRNG(xorshift_seed1=seed, xorshift_seed2=seed + 1)
    mt = MersenneTwisterPRNG(mt_seed=seed)
    pcg = PCGPRNG(pcg_state=seed, pcg_inc=seed + 1)
    isaac = IsaacPRNG(isaac_seed=seed)

    random_numbers = [
        lcg.generate(),
        xorshift.generate(),
        mt.generate(),
        pcg.generate(),
        isaac.generate()
    ]

    combined_random = sum(random_numbers) / len(random_numbers)
    return combined_random


# Get user input for the seed
user_input = input("Enter a seed value (press Enter for default): ")
if user_input.strip() == "":
    user_seed = None
else:
    user_seed = int(user_input)

# Usage
random_number = combined_prng(seed=user_seed)
print("Combined Random Number:", random_number)
