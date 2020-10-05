
public class App {

	public static void main(String[] args) {
	//1D array
		int [] values = {3,5,2343};
		//Only need 1 index to access values.
		System.out.println(values[2]);
		
		
		int [][] grid = {{3,4,2343},
				        {2,4},
				        {1,2,3,4}
				        };
		System.out.println(grid[1][1]);
		System.out.println(grid[0][2]);
		System.out.println(grid[2][3]);
		
		//can also create without initializing.
		String [][] texts = new String[2][3];
		texts[0][1] = "Hello there";
		texts[0][0] = "hello not there";
		System.out.println(texts[0][0]);
		System.out.println(texts[0][1]);
		
		//How to iterate through 2D arrays.
		// first iterate through rows then for each row
		//go through the columns.
		
		for(int row =0; row < grid.length; row++)
		{
			for(int col =0; col < grid[row].length; col++)
			{
				System.out.println(grid[row][col]+"\t");
			}
			System.out.println();
		}
		
		//The last array index is optional.
		String[][] words = new String[2][];
		
		//each sub- array index is optional
		System.out.println(words[0]);
		
		// we can sreate the sub array mannually
		words[0] = new String[3];
		
		//can set a value in thesub-array we 
		//just created 
		words[0][1] = "hi there";
		
		System.out.println(words[0][1]);
		
		}
}
