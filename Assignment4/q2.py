import math
import re

def tokenize_c_program(code):
    # Remove comments
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    
    # Common C keywords / operators to identify operators
    keywords = {'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 
                'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
                'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 
                'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 
                'volatile', 'while', 'main', 'printf', 'scanf'}
    
    # Operators in C
    operator_symbols = {'+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=', 
                        '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '++', '--', 
                        '+=', '-=', '*=', '/=', ',', ';', '(', ')', '{', '}', '[', ']', '.', '->'}
    
    # Tokenize words, numbers, and operators
    # We use regex to find words, numbers, and multi-char/single-char operators
    tokens = re.findall(r'[a-zA-Z_]\w*|\d+(?:\.\d+)?|==|!=|<=|>=|&&|\|\||\+\+|--|\+=|-=|\*=|/=|->|[+\-*/%=<>&|^~.,;(){}\[\]]', code)
    
    operators_list = []
    operands_list = []
    
    for token in tokens:
        if token in keywords or token in operator_symbols:
            operators_list.append(token)
        elif re.match(r'^[a-zA-Z_]\w*$', token):
            operands_list.append(token)
        elif re.match(r'^\d+(?:\.\d+)?$', token):
            operands_list.append(token)
        else:
            operators_list.append(token)
            
    # Calculate unique and total counts
    unique_operators = set(operators_list)
    unique_operands = set(operands_list)
    
    n1 = len(unique_operators)
    n2 = len(unique_operands)
    N1 = len(operators_list)
    N2 = len(operands_list)
    
    return n1, n2, N1, N2

def main():
    print("=== C Program Structural Complexity Analyzer (Halstead Metrics) ===")
    print("Enter or paste your C-Program below (Type 'END' on a new line when finished):")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
            
    c_code = "\n".join(lines)
    
    if not c_code.strip():
        # Fallback sample code if user didn't enter anything
        c_code = """
        int main() {
            int a, b, c, avg;
            scanf("%d %d %d", &a, &b, &c);
            avg = (a + b + c) / 3;
            printf("avg = %d", avg);
            return 0;
        }
        """
        print("\n[Notice] No code entered. Using default sample C program.")

    n1, n2, N1, N2 = tokenize_c_program(c_code)
    
    # Ensure non-zero values to avoid math domain errors
    n1 = max(n1, 1)
    n2 = max(n2, 1)
    N1 = max(N1, 1)
    N2 = max(N2, 1)
    
    while True:
        print("\n================ MENU ================")
        print("1. Unique number of operands and operators (n1, n2)")
        print("2. Total number of operands and operators (N1, N2)")
        print("3. Actual Program Length (N)")
        print("4. Expected Program Length (N^)")
        print("5. Program Volume (V)")
        print("6. Program Critical / Potential Volume (V*)")
        print("7. Program Level (L)")
        print("8. Effort to develop Program (E)")
        print("9. Program Time (T) [Stroud number = 18s]")
        print("10. Number of People engaged [Duration = 5 months]")
        print("11. Display All Metrics")
        print("0. Exit")
        print("======================================")
        
        choice = input("Enter your choice (0-11): ").strip()
        
        if choice == '1':
            print(f"\n(i) Unique Operators (n1) = {n1}")
            print(    f"    Unique Operands (n2) = {n2}")
            print(    f"    Total Vocabulary (n) = {n1 + n2}")
            
        elif choice == '2':
            print(f"\n(ii) Total Operators (N1) = {N1}")
            print(     f"     Total Operands (N2) = {N2}")
            
        elif choice == '3':
            N = N1 + N2
            print(f"\n(iii) Actual Program Length (N = N1 + N2) = {N}")
            
        elif choice == '4':
            N_hat = (n1 * math.log2(n1)) + (n2 * math.log2(n2))
            print(f"\n(iv) Expected Program Length (N^ = n1*log2(n1) + n2*log2(n2)) = {N_hat:.2f}")
            
        elif choice == '5':
            N = N1 + N2
            vocabulary = n1 + n2
            V = N * math.log2(vocabulary)
            print(f"\n(v) Program Volume (V = N * log2(n1 + n2)) = {V:.2f} bits")
            
        elif choice == '6':
            # Assuming n2* (unique input/output parameters) defaults to min(n2, 2) or estimated
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            print(f"\n(vi) Program Critical / Potential Volume (V*) = {V_star:.2f} bits")
            
        elif choice == '7':
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            N = N1 + N2
            V = N * math.log2(n1 + n2)
            L = V_star / V if V > 0 else 0
            print(f"\n(vii) Program Level (L = V* / V) = {L:.4f}")
            
        elif choice == '8':
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            N = N1 + N2
            V = N * math.log2(n1 + n2)
            L = V_star / V if V > 0 else 1e-5
            E = V / L
            print(f"\n(viii) Effort to develop Program (E = V / L) = {E:.2f} elementary mental discriminations")
            
        elif choice == '9':
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            N = N1 + N2
            V = N * math.log2(n1 + n2)
            L = V_star / V if V > 0 else 1e-5
            E = V / L
            S = 18 # Stroud number
            T = E / S
            print(f"\n(ix) Program Time (T = E / S, S=18s) = {T:.2f} seconds ({T/60:.2f} minutes)")
            
        elif choice == '10':
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            N = N1 + N2
            V = N * math.log2(n1 + n2)
            L = V_star / V if V > 0 else 1e-5
            E = V / L
            # Duration given as 5 months. Using person-power estimation model: I = E / (Duration in months * factor) or standard Halstead manpower formula: I = E^(1/3) / 3000 or E / (T_dev)
            # In standard software engineering problems where development duration is 5 months:
            duration_months = 5
            # Manpower = Effort / (Duration * working hours/month) or using Halstead's manpower approximation
            # Alternatively, using standard Putnam/Halstead relation: People = Effort / (Duration * constant)
            # Let's present both standard derivations:
            people_est = E / (duration_months * 160 * 3600) # Assuming effort in seconds
            print(f"\n(x) Number of People engaged for 5 months duration:")
            print(f"    Estimated Team Size / Personnel = {max(1.0, people_est):.2f} (approx. 1 to 2 developers based on cognitive effort)")
            
        elif choice == '11':
            N = N1 + N2
            vocabulary = n1 + n2
            N_hat = (n1 * math.log2(n1)) + (n2 * math.log2(n2))
            V = N * math.log2(vocabulary)
            n2_star = min(n2, 2)
            V_star = (2 + n2_star) * math.log2(2 + n2_star)
            L = V_star / V if V > 0 else 1e-5
            E = V / L
            T = E / 18
            people = max(1.0, E / (5 * 160 * 3600))
            
            print("\n================ ALL METRICS ================")
            print(f"(i) Unique Operators ($n_1$) & Operands ($n_2$): {n1}, {n2}")
            print(f"(ii) Total Operators ($N_1$) & Operands ($N_2$): {N1}, {N2}")
            print(f"(iii) Actual Program Length ($N$): {N}")
            print(f"(iv) Expected Program Length ($\hat{{N}}$): {N_hat:.2f}")
            print(f"(v) Program Volume ($V$): {V:.2f} bits")
            print(f"(vi) Critical Volume ($V^*$): {V_star:.2f} bits")
            print(f"(vii) Program Level ($L$): {L:.4f}")
            print(f"(viii) Development Effort ($E$): {E:.2f}")
            print(f"(ix) Program Time ($T$ @ S=18s): {T:.2f} seconds")
            print(f"(x) People Engaged (5 months): {people:.2f} developer(s)")
            print("=============================================")
            
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("[Error] Invalid choice! Please enter a number between 0 and 11.")

if __name__ == "__main__":
    main()