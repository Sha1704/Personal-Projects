/*
 * Created on: Dec 21, 2024
 *
 * ULID: <sadibos>
 * Class: IT 179 
 */
package personalFinanceManager_PersonalProject1;

/**
 * <This class has all the most important code (in my opinion)>
 *
 * @author <Adiboshi Shalom;
 *
 */
public class Expense
{
	private String date, category;
	private double amount;

	public Expense(String date, String category, double amount)
	{
		this.date = date;
		this.category = category;
		this.amount = amount;
	}

	public String getDate()
	{
		return date;
	}

	public void setDate(String date)
	{
		this.date = date;
	}

	public String getCategory()
	{
		return category;
	}

	public void setCategory(String category)
	{
		this.category = category;
	}

	public double getAmount()
	{
		return amount;
	}

	public void setAmount(double amount)
	{
		this.amount = amount;
	}

	public String toString()
	{
		String str = "";
		System.out.println("Date: " + getDate());
		System.out.println("Category: " + getCategory());
		System.out.printf("Amount: $%.2f", getAmount());
		System.out.println();
		return str;
	}
}
