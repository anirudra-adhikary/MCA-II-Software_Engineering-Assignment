import math
import sys

KEYWORDS = {
    "auto",
    "break",
    "case",
    "char",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extern",
    "float",
    "for",
    "goto",
    "if",
    "int",
    "long",
    "register",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "typedef",
    "union",
    "unsigned",
    "void",
    "volatile",
    "while",
    "#include",
    "printf",
    "scanf",
    "cin",
    "cout",
}

OPERATORS = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "=",
    "==",
    "!=",
    "<",
    ">",
    "<=",
    ">=",
    "&&",
    "||",
    "!",
    "&",
    "|",
    "^",
    "~",
    "<<",
    ">>",
    "++",
    "--",
    "+=",
    "-=",
    "*=",
    "/=",
    "->",
    ".",
    ",",
    ";",
}
DELIMITERS = {",", ";", "(", ")", "{", "}", "[", "]"}


class LexicalAnalyzer:

  def __init__(self, source_code):
    self.source = source_code
    self.length = len(source_code)
    self.pos = 0
    self.line = 1
    self.tokens = []
    self.invalid_identifiers = set()
    self.invalid_constants = set()
    self.invalid_operators = set()

  def error(self, msg):
    pass

  def tokenize(self):
    i = 0
    n = self.length
    while i < n:
      ch = self.source[i]

      if ch == "\n":
        self.line += 1
        i += 1
        continue

      if ch.isspace():
        i += 1
        continue

      if ch == "/" and i + 1 < n and self.source[i + 1] == "/":
        while i < n and self.source[i] != "\n":
          i += 1
        continue
      if ch == "/" and i + 1 < n and self.source[i + 1] == "*":
        i += 2
        while i + 1 < n and not (
            self.source[i] == "*" and self.source[i + 1] == "/"
        ):
          if self.source[i] == "\n":
            self.line += 1
          i += 1
        i += 2
        continue

      if ch == "#":
        start = i
        i += 1
        while i < n and (self.source[i].isalnum() or self.source[i] == "include"):
          i += 1
        directive = self.source[start:i]
        if directive == "#include":
          self.tokens.append(("OPERATOR", "#include"))
        else:
          self.tokens.append(("OPERATOR", directive))
        continue

      if ch == '"' or ch == "'":
        quote = ch
        start = i
        i += 1
        while i < n and self.source[i] != quote:
          if self.source[i] == "\n":
            self.line += 1
          i += 1
        if i < n:
          i += 1
        literal = self.source[start:i]
        self.tokens.append(("CONSTANT", literal))
        continue

      if ch.isalpha() or ch == "_":
        start = i
        while i < n and (self.source[i].isalnum() or self.source[i] == "_"):
          i += 1
        lexeme = self.source[start:i]
        if lexeme in KEYWORDS:
          self.tokens.append(("OPERATOR", lexeme))
        else:
          self.tokens.append(("IDENTIFIER", lexeme))
        continue

      if ch.isdigit():
        start = i
        is_invalid_const = False
        dot_count = 0
        while i < n and (self.source[i].isdigit() or self.source[i] == "."):
          if self.source[i] == ".":
            dot_count += 1
          i += 1
        lexeme = self.source[start:i]
        if dot_count > 1:
          self.invalid_constants.add(lexeme)
        else:
          self.tokens.append(("CONSTANT", lexeme))
        continue

      if ch.isdigit() == False and (ch.isalnum() == False):
        two_char = self.source[i : i + 2] if i + 1 < n else ""
        if two_char in {
            "==",
            "!=",
            "<=",
            ">=",
            "&&",
            "||",
            "<<",
            ">>",
            "++",
            "--",
            "+=",
            "-=",
            "*=",
            "/=",
            "->",
        }:
          self.tokens.append(("OPERATOR", two_char))
          i += 2
          continue
        elif ch in DELIMITERS:
          self.tokens.append(("DELIMITER", ch))
          i += 1
          continue
        elif ch in OPERATORS or ch in {"<", ">"}:
          self.tokens.append(("OPERATOR", ch))
          i += 1
          continue
        else:
          self.invalid_operators.add(ch)
          i += 1
          continue

      i += 1


def analyze_halstead(tokens, source_code):
  operators_list = []
  operands_list = []
  input_operands = set()
  lines = source_code.splitlines()
  for line in lines:
    if "scanf" in line or "cin" in line:
      for token_type, val in tokens:
        if token_type == "IDENTIFIER" and val in line:
          input_operands.add(val)

  for token_type, val in tokens:
    if token_type == "OPERATOR":
      operators_list.append(val)
    elif token_type == "IDENTIFIER" or token_type == "CONSTANT":
      operands_list.append(val)

  N1 = len(operators_list)
  N2 = len(operands_list)
  eta1 = len(set(operators_list))
  eta2 = len(set(operands_list))
  eta2_star = len(input_operands)
  if eta2_star == 0:
    eta2_star = 1

  N = N1 + N2
  Ne = (eta1 * math.log2(eta1) if eta1 > 0 else 0) + (
      eta2 * math.log2(eta2) if eta2 > 0 else 0
  )
  V = N * math.log2(eta1 + eta2) if (eta1 + eta2) > 0 else 0
  Vc = (2 + eta2_star) * math.log2(2 + eta2_star)
  L = Vc / V if V > 0 else 0
  E = V / L if L > 0 else 0

  return {
      "N1": N1,
      "N2": N2,
      "eta1": eta1,
      "eta2": eta2,
      "eta2_star": eta2_star,
      "N": N,
      "Ne": Ne,
      "V": V,
      "Vc": Vc,
      "L": L,
      "E": E,
      "unique_operators": sorted(list(set(operators_list))),
      "unique_operands": sorted(list(set(operands_list))),
      "input_operands": sorted(list(input_operands)),
  }


def main():
  if len(sys.argv) < 2:
    print("Usage: python halstead_analyzer.py <source_file.txt>")
    return

  filename = sys.argv[1]
  try:
    with open(filename, "r") as f:
      code = f.read()
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return

  lexer = LexicalAnalyzer(code)
  lexer.tokenize()

  metrics = analyze_halstead(lexer.tokens, code)

  print("=" * 50)
  print(f" HALSTEAD SOFTWARE SCIENCE METRICS FOR: {filename}")
  print("=" * 50)
  print(
      f"(a) Actual Program Length (N)       : {metrics['N']}"
      f" (N1={metrics['N1']}, N2={metrics['N2']})"
  )
  print(f"(b) Estimated Program Length (Ne)    : {metrics['Ne']:.2f}")
  print(f"(c) Program Volume (V)             : {metrics['V']:.2f} bits")
  print(f"(d) Critical Volume (Vc)           : {metrics['Vc']:.2f} bits")
  print(f"(e) Program Level (L)              : {metrics['L']:.4f}")
  print(f"(f) Program Effort (E)             : {metrics['E']:.2f} bits")
  print("-" * 50)
  print(
      f"Unique Operators (eta1 = {metrics['eta1']}):"
      f" {metrics['unique_operators']}"
  )
  print(
      f"Unique Operands (eta2 = {metrics['eta2']}):"
      f" {metrics['unique_operands']}"
  )
  print(
      f"Actual Input Operands (eta2* = {metrics['eta2_star']}):"
      f" {metrics['input_operands']}"
  )
  print("-" * 50)
  print(
      f"Invalid Identifiers found          :"
      f" {list(lexer.invalid_identifiers) if lexer.invalid_identifiers else 'None'}"
  )
  print(
      f"Invalid Constants found            :"
      f" {list(lexer.invalid_constants) if lexer.invalid_constants else 'None'}"
  )
  print(
      f"Invalid Operators/Symbols found    :"
      f" {list(lexer.invalid_operators) if lexer.invalid_operators else 'None'}"
  )
  print("=" * 50)


if __name__ == "__main__":
  main()