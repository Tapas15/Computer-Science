import java.util.Scanner;


public class Application {

	public static void main(String[] args) {
		// Create a scanner object 
		Scanner input = new Scanner(System.in); // ctrl + shift + O to import short-cut 
		//Output of prompt
		System.out.println("Enter a line of text  ");
        // wait for user to enter something
	    String line = input.nextLine();
		// output of text 
        System.out.println("you entered :"+ line);
	}

}
