import java.util.Scanner;


public class Application {

	public static void main(String[] args) {
		//create a Scanner object
		Scanner input = new Scanner(System.in);
		//Output of prompt
		System.out.println("Enter a value  : ");
		//Wait for user to enter 
		int value = input.nextInt();
		//Tell them what they entered
		System.out.println("You entered " + value);
		
		

	}

}
