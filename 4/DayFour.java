import java.io.File;
import java.util.*;

public class DayFour {


    /*
     * method to take in line of text as a card
     * creates a set of winning numbers then itterates of lame numbers checking for a match
     * returns 2^matches where 1 match = 0 power, as points
     */
    static int readCard(String line){
        int points = 0;
        int matches = -1;

        //System.out.println(line.split("\\|")[0]);

        String[] winnersTxt = line.split("\\|")[0].split(":")[1].split(" ");
        String[] lameNums = line.split("\\|")[1].split("\r")[0].split(" ");
        HashSet<String> winners = new HashSet<>(Arrays.asList(winnersTxt));
        if(winners.contains("")){
            winners.remove("");
        }
        if(winners.contains("\r")){
            winners.remove("\r");
        }

        System.out.println(winners.toString());
        System.out.println(Arrays.toString(lameNums));

        for(String num : lameNums){
            if(winners.contains(num)){
                matches++;
            }
        }
        points = (int)Math.pow(2, matches);

        System.out.println(matches+"\n");

        return points==-1 ? 0:points;
    }

    public static void main(String[] args){
        //create a set of winner numbers:
        //if current number in your set is in winning then matches++
        //2^matches starting at -1, if -1 return 0
        //add each card to the points sum in main method

        int sum = 0;

        //read in the input txt file
        String content = "";
        try{
            content = new Scanner(new File("input4.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }

        String[] lines = content.split("\n");

        for(String line : lines){
            sum += readCard(line);
        }

        System.out.println(sum);
        
    }
    
}
