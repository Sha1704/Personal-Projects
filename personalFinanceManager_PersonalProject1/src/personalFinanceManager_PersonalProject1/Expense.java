/*
 * Created on: Dec 21, 2024
 *
 * ULID: <sadibos>
 * Class: IT 179 
 */
package personalFinanceManager_PersonalProject1;

/**
 * <insert class description here>
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
	
	public void displayExpenses()
	{
		//to be implemented
	}
	
	public void calculateSpending()
	{
		System.out.println();
		// to be implemented
	}
	
	public void categorizeSpending()
	{
		// to be implemented
	}
}
