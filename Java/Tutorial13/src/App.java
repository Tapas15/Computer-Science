
public class App {

	public static void main(String[] args) {
		//Decalre arrow of reference 
		String[] words = new String[3];
		
		//set the array reference to point the reference 
		
		words[0] = "Hello";
		words[1] = "to";
		words[2] = "you";
	
	
	// Access an array element and print it 
		System.out.println(words[2]);
	//Simultaneously declare an array element string
		String [] fruits = {"apple","banana","pear","kiwi"};
		
		// iterate through an array
		for(String fruit:fruits)
		{
			System.out.println(fruit);
		}
	// defaault value for an integer 
		int value = 0;
	//defalut value for a reference is null 
	String text = null;
	System.out.println(text);
   
	//Declare of string 
	String[] texts = new String [1];
	//The reference to the string in the array
	// are initialised to null 
	System.out.println(texts[0]);
	
	texts[0] = "one";

	}

}
