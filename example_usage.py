"""Example usage for CYK PCFG Parser Skill."""
from client import CYKParser

def main():
    print("Executing CYK PCFG Parser...")
    grammar = {
        "S": [(1.0, ("NP", "VP"))],
        "NP": [(0.7, ("Det", "N")), (0.3, ("alice",))],
        "VP": [(1.0, ("V", "NP"))],
        "Det": [(1.0, ("the",))],
        "N": [(1.0, ("rabbit",))],
        "V": [(1.0, ("follows",))]
    }
    parser = CYKParser(grammar)
    res = parser.parse(["alice", "follows", "the", "rabbit"])
    print("Parse Result:", res)
    assert res["has_parse"] == True
    assert res["best_prob"] > 0.0
    print("CYK PCFG Parser verified successfully!")

if __name__ == "__main__":
    main()
