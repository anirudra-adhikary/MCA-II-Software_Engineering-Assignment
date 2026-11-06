import java.util.Scanner;

public class COCOMO {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mainChoice;

        do {
            System.out.println("\n--- COCOMO I Main Menu ---");
            System.out.println("1. Basic COCOMO");
            System.out.println("2. Intermediate COCOMO");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            mainChoice = sc.nextInt();

            if (mainChoice == 1) {
                runBasicCOCOMO(sc);
            } else if (mainChoice == 2) {
                runIntermediateCOCOMO(sc);
            } else if (mainChoice == 3) {
                System.out.println("Exiting Program.");
            } else {
                System.out.println("Invalid choice.");
            }
        } while (mainChoice != 3);

        sc.close();
    }

    private static void runBasicCOCOMO(Scanner sc) {
        System.out.print("Enter Lines of Code (LOC): ");
        double loc = sc.nextDouble();
        double kloc = loc / 1000.0;

        int type = getProjectType(kloc);
        
        double[][] constants = {
            {2.4, 1.05, 2.5, 0.38},
            {3.0, 1.12, 2.5, 0.35},
            {3.6, 1.20, 2.5, 0.32}
        };

        double effort = constants[type][0] * Math.pow(kloc, constants[type][1]);
        double time = constants[type][2] * Math.pow(effort, constants[type][3]);
        double people = effort / time;

        int choice;
        do {
            System.out.println("\n--- Basic COCOMO Sub-Menu ---");
            System.out.println("1. Determine the Effort");
            System.out.println("2. Determine the Time");
            System.out.println("3. Determine the Number of People");
            System.out.println("4. Exit to Main Menu");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.printf("Effort = %.2f Person-Months\n", effort);
                    break;
                case 2:
                    System.out.printf("Development Time = %.2f Months\n", time);
                    break;
                case 3:
                    System.out.printf("Number of People engaged = %d Persons\n", Math.round(people));
                    break;
                case 4:
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
    }

    private static void runIntermediateCOCOMO(Scanner sc) {
        System.out.print("Enter Lines of Code (LOC): ");
        double loc = sc.nextDouble();
        double kloc = loc / 1000.0;

        int type = getProjectType(kloc);
        
        double[][] constants = {
            {3.2, 1.05, 2.5, 0.38},
            {3.0, 1.12, 2.5, 0.35},
            {2.8, 1.20, 2.5, 0.32}
        };

        double eaf = 1.0;
        System.out.println("Enter the values for the 15 cost driver attributes:");
        for (int i = 1; i <= 15; i++) {
            System.out.print("Cost Driver " + i + " multiplier: ");
            eaf *= sc.nextDouble();
        }

        double effort = constants[type][0] * Math.pow(kloc, constants[type][1]) * eaf;
        double time = constants[type][2] * Math.pow(effort, constants[type][3]);
        double people = effort / time;

        int choice;
        do {
            System.out.println("\n--- Intermediate COCOMO Sub-Menu ---");
            System.out.println("1. Determine the Effort");
            System.out.println("2. Determine the Time");
            System.out.println("3. Determine the Number of People");
            System.out.println("4. Determine the value of EAF");
            System.out.println("5. Exit to Main Menu");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.printf("Effort = %.2f Person-Months\n", effort);
                    break;
                case 2:
                    System.out.printf("Development Time = %.2f Months\n", time);
                    break;
                case 3:
                    System.out.printf("Number of People engaged = %d Persons\n", Math.round(people));
                    break;
                case 4:
                    System.out.printf("EAF = %.4f\n", eaf);
                    break;
                case 5:
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 5);
    }

    private static int getProjectType(double kloc) {
        if (kloc <= 50) {
            System.out.println("Project Type: Organic");
            return 0;
        } else if (kloc <= 300) {
            System.out.println("Project Type: Semi-detached");
            return 1;
        } else {
            System.out.println("Project Type: Embedded");
            return 2;
        }
    }
}