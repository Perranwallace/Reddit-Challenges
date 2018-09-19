import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;

public class diceRoll {
    public static void main ( String [] args ) {
		
		Scanner scanner = new Scanner(System.in);
		String input = scanner.next(); 
		
		if (input.contains("d")){
			String[] splitInput = input.split("d"); // split the input string in 2 divided by the 'd' character
			String diceStr = splitInput[0]; // the chars before the 'd' are the number of dices to be rolled
			String sidesStr = splitInput[1]; // the chars after the 'd' are the number of sides on the dice
			
			int dice = Integer.parseInt(diceStr);	
			int sides = Integer.parseInt(sidesStr);				
			
			int[] rollList = new int[dice]; // the list of numbers obtained at each roll
			int total = 0; // the total of these rolls
			
			for(int roll = 0; roll < dice ; roll++) { // iterate for each roll
				
				Random r = new Random();
				int randNum = r.nextInt(sides-1) + 1; // generate a random number between 1 and the number of sides on the die
				rollList[roll] = randNum; // add this roll to the list
				total += randNum; 
				
			}
			
			
		
			System.out.print("Rolls: ");
			for (int i = 0; i < dice; i++) {
				System.out.print(rollList[i] + " "); // print the roll list
			}
			System.out.println ("\nTotal: " + total);
			
		}
		else //if the input does not have a 'd' in
			System.out.println ("Incorrect format.");
    }
}