/*
 * Created on: Dec 20, 2024
 *
 * ULID: <sadibos>
 * Class: IT 179 
 */
package personalFinanceManager_PersonalProject1;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * <Main class; runs the program and contains all necessary stuff>
 *
 * @author <Adiboshi Shalom;
 *
 */
public class Main
{

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		try
		{

			ArrayList<Expense> a1 = new ArrayList<>();
			Scanner scan = new Scanner(System.in);

			System.out.println("Welcome to the Personal Finance Manager!");

			showMenu();
			int input = scan.nextInt();

			while (input != 4)
			{
				if (input < 1 || input > 4)
				{
					System.out.println("Please enter a number between 1-4: ");
					input = scan.nextInt();
				} else
				{
					if (input == 1)
					{
						System.out.println("Enter Date (YYYY-MM-DD): ");
						String date = scan.next();

						System.out.println("Enter Category: ");
						String category = scan.next();

						System.out.println("Enter Amount: ");
						double amount = scan.nextDouble();

						Expense e1 = new Expense(date, category, amount);

						a1.add(e1);
						System.out.println("Expense added!");

						showMenu();
						input = scan.nextInt();
					} else if (input == 2)
					{
						if (a1.size() == 0)
						{
							System.out.println("There are no expenses to view!");
						} else
						{
							System.out.println("Here are your expenses...");
							System.out.printf("-------------------------------------%n");
							System.out.printf("             Expenses %n");
							System.out.printf("-------------------------------------%n");
							System.out.printf("%-11s %-15s %-15s", "Date", "Category", "Amount");
							System.out.println();

							for (int i = 0; i < a1.size(); i++)
							{
								System.out.printf("%-11s %-15s %-15.2f", a1.get(i).getDate(), a1.get(i).getCategory(),
										a1.get(i).getAmount());
								System.out.println();
							}
						}

						showMenu();
						input = scan.nextInt();
					} else if (input == 3)
					{
						double total = 0;
						for (int i = 0; i < a1.size(); i++)
						{
							total += a1.get(i).getAmount();
						}
						System.out.printf("Your total expense is: $%.2f", total);
						System.out.println();
						showMenu();
						input = scan.nextInt();
					}
				}
			}
			System.out.println("Thank you for using the personal finance manager!");
		} catch (InputMismatchException e)
		{
			System.out.println(
					"Input Mismatch (you enterd the wrong data-type) please run the program again. Error message: "
							+ e.getMessage());
		}
	}

	public static void showMenu()
	{
		System.out.println();
		System.out.println("Please choose one of the following options");
		System.out.println("1. Add Expense");
		System.out.println("2. View Expenses");
		System.out.println("3. Calculate Total Spending");
		System.out.println("4. Exit");
		System.out.println("Choose an option:");
	}
}
