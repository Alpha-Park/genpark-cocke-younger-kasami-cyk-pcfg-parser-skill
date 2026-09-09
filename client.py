"""
Autonomous Agent CYK PCFG Parser Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Tuple, Any

class CYKParser:
    """
    Probabilistic CYK Parser for Chomsky Normal Form grammars.
    """
    def __init__(self, cnf_rules: Dict[str, List[Tuple[float, Tuple[str, ...]]]]):
        self.rules = cnf_rules

    def parse(self, tokens: List[str]) -> Dict[str, Any]:
        n = len(tokens)
        table = [[{} for _ in range(n)] for _ in range(n)]

        for i in range(n):
            tok = tokens[i]
            for lhs, rhs_list in self.rules.items():
                for prob, rhs in rhs_list:
                    if len(rhs) == 1 and rhs[0] == tok:
                        table[0][i][lhs] = (prob, tok)

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    left_cell = table[k - i][i]
                    right_cell = table[j - (k + 1)][k + 1]
                    for lhs, rhs_list in self.rules.items():
                        for prob, rhs in rhs_list:
                            if len(rhs) == 2:
                                b, c = rhs
                                if b in left_cell and c in right_cell:
                                    p_comb = prob * left_cell[b][0] * right_cell[c][0]
                                    if lhs not in table[l - 1][i] or p_comb > table[l - 1][i][lhs][0]:
                                        table[l - 1][i][lhs] = (p_comb, (left_cell[b], right_cell[c]))

        start_matches = table[n - 1][0]
        has_parse = "S" in start_matches
        best_prob = start_matches["S"][0] if has_parse else 0.0
        return {
            "has_parse": has_parse,
            "best_prob": round(best_prob, 6)
        }
