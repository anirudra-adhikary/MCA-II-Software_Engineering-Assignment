package q1;
import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TextJustifierGUI extends JFrame {

    private JTextArea inputArea;
    private JTextArea outputArea;
    private JSpinner widthSpinner;

    public TextJustifierGUI() {
        setTitle("Text Justifier");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);
        setLayout(new BorderLayout());

        inputArea = new JTextArea(10, 50);
        inputArea.setText("    This is a set of lines of arbitrary length.\n" +
                "We want to left and right justify the text without splitting\n" +
                "words. Paragraphs should stay indented.\n" +
                "\n" +
                "This is a new paragraph that should be processed separately.\n" +
                "The extra blanks must be evenly distributed.");
        JScrollPane inputScroll = new JScrollPane(inputArea);
        inputScroll.setBorder(BorderFactory.createTitledBorder("Input Text"));

        outputArea = new JTextArea(15, 50);
        outputArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
        outputArea.setEditable(false);
        JScrollPane outputScroll = new JScrollPane(outputArea);
        outputScroll.setBorder(BorderFactory.createTitledBorder("Justified Output"));

        JPanel controlPanel = new JPanel();
        controlPanel.add(new JLabel("Max Width:"));
        widthSpinner = new JSpinner(new SpinnerNumberModel(40, 10, 200, 1));
        controlPanel.add(widthSpinner);

        JButton justifyButton = new JButton("Justify Text");
        justifyButton.addActionListener(e -> justifyAndDisplay());
        controlPanel.add(justifyButton);

        JSplitPane splitPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT, inputScroll, outputScroll);
        splitPane.setResizeWeight(0.4);

        add(splitPane, BorderLayout.CENTER);
        add(controlPanel, BorderLayout.SOUTH);
    }

    private void justifyAndDisplay() {
        String text = inputArea.getText();
        List<String> lines = Arrays.asList(text.split("\\n"));
        int maxWidth = (int) widthSpinner.getValue();

        List<String> justifiedText = justifyText(lines, maxWidth);
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 1; i <= maxWidth; i++) {
            sb.append(i % 10);
        }
        sb.append("\n");
        for (int i = 0; i < maxWidth; i++) {
            sb.append("-");
        }
        sb.append("\n");

        for (String line : justifiedText) {
            sb.append(line).append("\n");
        }
        
        outputArea.setText(sb.toString());
    }

    public static List<String> justifyText(List<String> lines, int maxWidth) {
        List<String> result = new ArrayList<>();
        List<String> currentParagraphWords = new ArrayList<>();
        String currentIndent = "";
        
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            
            if (line.trim().isEmpty()) {
                if (!currentParagraphWords.isEmpty()) {
                    result.addAll(formatParagraph(currentParagraphWords, currentIndent, maxWidth));
                    currentParagraphWords.clear();
                }
                result.add("");
                currentIndent = "";
                continue;
            }

            if (currentParagraphWords.isEmpty()) {
                currentIndent = getLeadingSpaces(line);
            }

            String[] words = line.trim().split("\\s+");
            for (String word : words) {
                if (!word.isEmpty()) {
                    currentParagraphWords.add(word);
                }
            }
        }
        
        if (!currentParagraphWords.isEmpty()) {
            result.addAll(formatParagraph(currentParagraphWords, currentIndent, maxWidth));
        }

        return result;
    }

    private static List<String> formatParagraph(List<String> words, String indent, int maxWidth) {
        List<String> formattedLines = new ArrayList<>();
        int i = 0;
        boolean isFirstLine = true;

        while (i < words.size()) {
            String lineIndent = isFirstLine ? indent : "";
            int availableWidth = maxWidth - lineIndent.length();
            
            int lineWordsLength = 0;
            int j = i;
            
            while (j < words.size()) {
                int wordLen = words.get(j).length();
                int minSpaces = j - i;
                
                if (lineWordsLength + minSpaces + wordLen > availableWidth) {
                    if (j == i) { 
                        j++;
                    }
                    break;
                }
                lineWordsLength += wordLen;
                j++;
            }

            List<String> lineWords = words.subList(i, j);
            boolean isLastLineOfParagraph = (j == words.size());

            formattedLines.add(formatLine(lineWords, maxWidth, lineIndent, isLastLineOfParagraph));
            
            i = j;
            isFirstLine = false;
        }

        return formattedLines;
    }

    private static String formatLine(List<String> words, int maxWidth, String indent, boolean isLastLine) {
        StringBuilder sb = new StringBuilder(indent);

        if (words.size() == 1 || isLastLine) {
            for (int i = 0; i < words.size(); i++) {
                sb.append(words.get(i));
                if (i < words.size() - 1) {
                    sb.append(" ");
                }
            }
            while (sb.length() < maxWidth) {
                sb.append(" ");
            }
            return sb.toString();
        }

        int wordsLength = 0;
        for (String w : words) {
            wordsLength += w.length();
        }

        int totalSpacesToDistribute = maxWidth - indent.length() - wordsLength;
        int gaps = words.size() - 1;
        int spacesPerGap = totalSpacesToDistribute / gaps;
        int extraSpaces = totalSpacesToDistribute % gaps;

        for (int i = 0; i < words.size() - 1; i++) {
            sb.append(words.get(i));
            
            int spaces = spacesPerGap + (i < extraSpaces ? 1 : 0);
            for (int s = 0; s < spaces; s++) {
                sb.append(" ");
            }
        }
        sb.append(words.get(words.size() - 1));

        return sb.toString();
    }

    private static String getLeadingSpaces(String line) {
        int i = 0;
        while (i < line.length() && line.charAt(i) == ' ') {
            i++;
        }
        return line.substring(0, i);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new TextJustifierGUI().setVisible(true);
        });
    }
}