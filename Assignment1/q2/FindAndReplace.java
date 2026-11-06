import java.util.Scanner;

public class FindAndReplace {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the original text:");
        String originalText = scanner.nextLine();
        
        System.out.println("Enter the pattern to search for:");
        String searchPattern = scanner.nextLine();
        
        System.out.println("Enter the replacement pattern:");
        String replacementPattern = scanner.nextLine();
        
        String result = replacePattern(originalText, searchPattern, replacementPattern);
        
        System.out.println("\n--- Modified Text ---");
        System.out.println(result);
        
        scanner.close();
    }

    public static String replacePattern(String text, String target, String replacement) {
        if (text == null || target == null || target.isEmpty()) {
            return text;
        }

        StringBuilder result = new StringBuilder();
        int currentIndex = 0;
        int targetLength = target.length();

        while (currentIndex < text.length()) {
            if (currentIndex + targetLength <= text.length() && 
                text.substring(currentIndex, currentIndex + targetLength).equals(target)) {
                
                result.append(replacement);
                currentIndex += targetLength;
            } else {
                result.append(text.charAt(currentIndex));
                currentIndex++;
            }
        }

        return result.toString();
    }
}