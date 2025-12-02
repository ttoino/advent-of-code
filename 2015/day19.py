import sys
import re


def part1(replacements: list[list[str]], molecule: str):
    s: set[str] = set()

    for a, b in replacements:
        i = -1
        while (i := molecule.find(a, i + 1)) != -1:
            s.add(molecule[:i] + molecule[i:].replace(a, b, 1))

    return len(s)


def part2(molecule: str):
    # All replacements are of the following types
    #   - µ => αβ
    #   - µ => αRnβAr
    #   - µ => αRnβYγAr
    #   - µ => αRnβYγYδAr
    # All types produce an additional atom.
    # Rn and Ar only show up on the right hand side and always in pairs, so they
    #  can be ignored.
    # Y always shows up on the right hand side, between an Rn and an Ar and for
    #  every Y there is another atom, so we can ignore these.
    # This gives us the expression
    #   #atoms - #Rn - #Ar - 2×#Y - 1
    # (- 1 because we start with a symbol, e)
    return (
        len(re.findall(r"[A-Z]", molecule))
        - molecule.count("Rn")
        - molecule.count("Ar")
        - 2 * molecule.count("Y")
        - 1
    )


if __name__ == "__main__":
    replacements, molecule = "".join(sys.stdin.readlines()).split("\n\n")
    replacements = [s.split(" => ") for s in replacements.strip().splitlines()]
    molecule = molecule.strip()
