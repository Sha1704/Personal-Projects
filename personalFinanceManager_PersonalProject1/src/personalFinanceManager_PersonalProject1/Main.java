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
			}
			else
			{
				if (input == 1)
				{
					System.out.println("Enter Date (YYYY-MM-DD): ");
					String date = scan.nextLine();
					scan.next();
					System.out.println("Enter Category: ");
					String category = scan.nextLine();
					scan.next();
					System.out.println("Enter Amount: ");
					double amount = scan.nextDouble();
					
					Expense e1 = new Expense(date, category, amount);
					
					a1.add(e1);
					System.out.println("Expense added!");
					
					showMenu();
					input = scan.nextInt();
				}
				else if (input == 2)
				{
					//view expense method (expense class) loop through l1 and call view expenses for all
				}
				else if (input == 3)
				{
					//calculate total spending (expense class) go through l1 and calculate total spending
				}
			}
		}
		System.out.println("Thank you for using the personal finance manager!");
	}
	catch (InputMismatchException e)
	{
			System.out.println("Input Mismatch (you enterd the wrong data-type) please run the program again. Error message: " + e.getMessage());
	}
	}	
	
	public static void showMenu()
	{
		System.out.println("Please choose one of the following options");
		System.out.println("1. Add Expense");
		System.out.println("2. View Expenses");
		System.out.println("3. Calculate Total Spending");
		System.out.println("4. Exit");
		System.out.println("Choose an option:");
	}
}
