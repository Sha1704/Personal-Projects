/*
 * Created on: Dec 20, 2024
 *
 * ULID: <sadibos>
 * Class: IT 179 
 */
package personalFinanceManager_PersonalProject1;

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
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Welcome to the Personal Finance Manager!");
		
		showMenu();
		int input = scan.nextInt();
		
		while (!scan.hasNextInt())
		{
			System.out.println("Please enter a number");
		}
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
					// add expense method (expense class)
				}
				else if (input == 2)
				{
					//view expense method (expense class)
				}
				else if (input == 3)
				{
					//calculate total spending (expense class)
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
