
# ============================================================
# PROBLEM:
#   Given the 1,000-digit number below, find the 13 consecutive
#   (adjacent) digits whose product is the largest possible,
#   and report that product.
#
# APPROACH — SLIDING WINDOW:
#   We place an imaginary "window" of width 13 at the very start
#   of the number (position 0).  We read the 13 digits under the
#   window, multiply them, and note the result.  Then we slide the
#   window one position to the right and repeat.  We do this until
#   the right edge of the window reaches the very last digit.
#   The largest result we ever saw is our answer.
#
#   Total windows to check = 1000 - 13 + 1 = 988
# ============================================================

import math   # We will use math.prod() to multiply a list of numbers
import time   # We will use time to measure how long the program takes

begin = time.time()

# ── STEP 1: STORE THE 1000-DIGIT NUMBER ─────────────────────
# We write it as a multi-line string for readability.
# Triple quotes let us span many lines without worrying about
# concatenation operators.

raw_number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455443629812309878799227244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

# ── STEP 2: CLEAN THE STRING ─────────────────────────────────
# The raw string contains newline characters (\n) and possibly spaces.
# We must remove them so we end up with a single flat string of exactly 1,000 digit characters.

number = raw_number.replace("\n", "").replace(" ", "")

# ── STEP 3: SET UP TRACKING VARIABLES ────────────────────────
# Before the loop starts we need somewhere to store the best
# result we've found so far.

WINDOW_SIZE = 13          # We are looking for 13 adjacent digits

best_product  = 0         # The largest product seen so far.We start at 0; any product of non-zero digits will immediately beat this

# ── STEP 4: SLIDE THE WINDOW ACROSS THE NUMBER ───────────────
# The window's left edge (i) starts at index 0 and must stop at index 1000 - 13 = 987, so that the right edge (i+13) never goes past the end of the string.
# Python's range(a, b) produces a, a+1, ..., b-1, so we pass len(number) - WINDOW_SIZE + 1  as the stop value to include index 987.

for i in range(len(number) - WINDOW_SIZE + 1):

    # Extract the 13-character substring at position i.
    # Python slicing: number[i : i+WINDOW_SIZE] gives characters
    # at indices i, i+1, ..., i+WINDOW_SIZE-1 — exactly 13 chars.
    window = number[i : i + WINDOW_SIZE]

    # ── OPTIMISATION: SKIP WINDOWS THAT CONTAIN A ZERO ───────
    # If even one digit is '0', the product of all 13 digits is guaranteed to be 0.  Multiplying the rest is pointless, so we jump straight to the next window.
    if '0' in window:
        continue   # Skip to next value of i

    # ── STEP 5: COMPUTE THE PRODUCT ──────────────────────────
    # Convert each character in the window to an integer, then
    # multiply them all together.
    # int(ch) turns '7' -> 7, '3' -> 3, etc.
    # math.prod([a, b, c, ...]) multiplies the whole list at once.
    digits  = [int(ch) for ch in window]   # list of 13 integers
    product = math.prod(digits)            # single integer result

    # ── STEP 6: UPDATE THE BEST IF THIS PRODUCT IS LARGER ────
    # We compare the current product to our running maximum.
    # If it's strictly greater, this window becomes our new winner.
    if product > best_product:
        best_product  = product


print(f"Greatest product : {best_product}")

end = time.time()
print(f"Finished in {end - begin} seconds.")
