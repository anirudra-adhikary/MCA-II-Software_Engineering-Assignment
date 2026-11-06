import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class LexicalAnalyzer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a C program statement:");
        if (scanner.hasNextLine()) {
            String input = scanner.nextLine();
            analyze(input);
        }
        scanner.close();
    }

    public static void analyze(String input) {
        int i = 0;
        int n = input.length();
        List<String> keywords = Arrays.asList("if", "for", "while", "int", "float", "char");
        String operators = "+-*/=<>";
        String symbols = ",();?";

        while (i < n) {
            char c = input.charAt(i);
            
            if (Character.isWhitespace(c)) {
                i++;
                continue;
            }

            if (Character.isLetter(c)) {
                StringBuilder sb = new StringBuilder();
                while (i < n && (Character.isLetterOrDigit(input.charAt(i)) || input.charAt(i) == '_')) {
                    sb.append(input.charAt(i));
                    i++;
                }
                String token = sb.toString();
                
                if (keywords.contains(token)) {
                    System.out.println(token + " : Keyword");
                } else if (token.length() <= 8) {
                    System.out.println(token + " : Identifier");
                } else {
                    System.out.println(token + " : Invalid Token (Identifier exceeds 8 characters)");
                }
            } 
            else if (Character.isDigit(c)) {
                StringBuilder sb = new StringBuilder();
                while (i < n && Character.isDigit(input.charAt(i))) {
                    sb.append(input.charAt(i));
                    i++;
                }
                String token = sb.toString();
                
                try {
                    int num = Integer.parseInt(token);
                    if (num >= 1 && num <= 999) {
                        System.out.println(token + " : Constant");
                    } else {
                        System.out.println(token + " : Invalid Token (Constant not between 1 and 999)");
                    }
                } catch (NumberFormatException e) {
                    System.out.println(token + " : Invalid Token (Constant out of range)");
                }
            } 
            else if (operators.indexOf(c) != -1) {
                System.out.println(c + " : Operator");
                i++;
            } 
            else if (symbols.indexOf(c) != -1) {
                System.out.println(c + " : Symbol");
                i++;
            } 
            else {
                System.out.println(c + " : Invalid Token (Unrecognized character)");
                i++;
            }
        }
    }
}