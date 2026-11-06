import java.util.Scanner;

public class COCOMOII {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mainChoice;

        do {
            System.out.println("\n--- COCOMO II Main Menu ---");
            System.out.println("1. Application Composition Model");
            System.out.println("2. Early Design Stage Model");
            System.out.println("3. Post Architecture Stage Model");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            mainChoice = sc.nextInt();

            switch (mainChoice) {
                case 1:
                    runAppComposition(sc);
                    break;
                case 2:
                    runEarlyDesign(sc);
                    break;
                case 3:
                    runPostArchitecture(sc);
                    break;
                case 4:
                    System.out.println("Exiting Program.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (mainChoice != 4);

        sc.close();
    }

    private static void runAppComposition(Scanner sc) {
        System.out.print("Enter Simple, Average, Complex Screens Count: ");
        int s1 = sc.nextInt();
        int s2 = sc.nextInt();
        int s3 = sc.nextInt();
        
        System.out.print("Enter Simple, Average, Complex Reports Count: ");
        int r1 = sc.nextInt();
        int r2 = sc.nextInt();
        int r3 = sc.nextInt();
        
        System.out.print("Enter Simple, Average, Complex Components Count: ");
        int c1 = sc.nextInt();
        int c2 = sc.nextInt();
        int c3 = sc.nextInt();
        
        System.out.print("Enter % Reuse (e.g., 90 for 90%): ");
        double reuse = sc.nextDouble();
        
        System.out.print("Enter Productivity: ");
        double prod = sc.nextDouble();

        double op = (s1 * 1 + s2 * 2 + s3 * 3) + 
                    (r1 * 2 + r2 * 5 + r3 * 8) + 
                    (c1 * 1 + c2 * 1 + c3 * 10);
        
        double nop = op * ((100.0 - reuse) / 100.0);
        double effort = nop / prod;
        double cost = effort * 1500.0;

        int choice;
        do {
            System.out.println("\n--- Application Composition Sub-Menu ---");
            System.out.println("1. Determine the Object Point");
            System.out.println("2. Determine the New Object Point");
            System.out.println("3. Determine the Effort");
            System.out.println("4. Determine the Total Project Cost");
            System.out.println("5. Return to Main Menu");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.printf("Object Point = %.2f\n", op);
                    break;
                case 2:
                    System.out.printf("New Object Point = %.2f\n", nop);
                    break;
                case 3:
                    System.out.printf("Effort = %.2f Person-Months\n", effort);
                    break;
                case 4:
                    System.out.printf("Total Project Cost = $%.2f\n", cost);
                    break;
                case 5:
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 5);
    }

    private static void runEarlyDesign(Scanner sc) {
        System.out.print("Enter Size in KLOC: ");
        double kloc = sc.nextDouble();
        
        System.out.print("Enter sum of 5 Scale Factors: ");
        double sfSum = sc.nextDouble();
        
        double eaf = 1.0;
        System.out.println("Enter the 7 Cost Drivers for Early Design:");
        for (int i = 1; i <= 7; i++) {
            System.out.print("Cost Driver " + i + ": ");
            eaf *= sc.nextDouble();
        }

        double e = 0.91 + 0.01 * sfSum;
        double effort = 2.94 * Math.pow(kloc, e) * eaf;
        double people = effort / 60.0;

        int choice;
        do {
            System.out.println("\n--- Early Design Stage Sub-Menu ---");
            System.out.println("1. Determine the Effort");
            System.out.println("2. Determine the Number of People (5 years duration)");
            System.out.println("3. Return to Main Menu");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.printf("Effort = %.2f Person-Months\n", effort);
                    break;
                case 2:
                    System.out.printf("Number of People = %d Persons\n", Math.round(people));
                    break;
                case 3:
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 3);
    }

    private static void runPostArchitecture(Scanner sc) {
        System.out.print("Enter Size in KLOC: ");
        double kloc = sc.nextDouble();
        
        System.out.print("Enter sum of 5 Scale Factors: ");
        double sfSum = sc.nextDouble();
        
        double eaf = 1.0;
        System.out.println("Enter the 16 Cost Drivers (Cd1 to Cd16):");
        for (int i = 1; i <= 16; i++) {
            System.out.print("Cd" + i + ": ");
            eaf *= sc.nextDouble();
        }

        double e = 0.91 + 0.01 * sfSum;
        double effort = 2.94 * Math.pow(kloc, e) * eaf;
        double people = effort / 60.0;

        int choice;
        do {
            System.out.println("\n--- Post Architecture Stage Sub-Menu ---");
            System.out.println("1. Determine the Effort");
            System.out.println("2. Determine the Number of People (5 years duration)");
            System.out.println("3. Return to Main Menu");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.printf("Effort = %.2f Person-Months\n", effort);
                    break;
                case 2:
                    System.out.printf("Number of People = %d Persons\n", Math.round(people));
                    break;
                case 3:
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 3);
    }
}