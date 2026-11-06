
        setSize(800, 600);
        setLayout(new BorderLayout());

        inputArea = new JTextArea(10, 50);
        inputArea.setText("    This is a set of lines of arbitrary length.\n" +
                "We want to left and right justify the text without splitting\n" +
                "words. Paragraphs should stay indented.\n" +
                "\n" +