import java.util.Scanner;
import java.io.*;

public class DayTwo {
    public static void main(String args[]){
        int sum = 0;

        try{
            String content = new Scanner(new File("input2.txt")).useDelimiter("\\Z").next();

            String[] lines = content.split("\n");

            for(String line:lines){
                sum += parseGame(line); 
            }
            System.out.println(sum);

        } catch (Exception e){
            System.out.print(e);
        }
    }

    //this function takes in one row from the game file and checks if valid game
    //a valid game has no pulls with red>12, 13>green, 14>blue
    //each pull in a game string is separated by a semicolon ";"
    static int parseGame(String game){
        int red, blue, green, gameNum;
        
        String[] garbage = game.split(":"); //separates game num from game info
        String[] gameNumString = garbage[0].split(" "); //grabs the game num from garbage
        gameNum = Integer.parseInt(gameNumString[1]);

        String[] gameInfo = garbage[1].split(";"); //seperates the pulls of the game

        //loop over each pull for this game
        for(String pull:gameInfo){
            
            red = 0;
            blue = 0;
            green = 0;
            String[] colors = pull.split(",");
            //find out the values for colors of this pull
            for(String currentColor:colors){
                int val = Integer.parseInt(currentColor.split(" ")[1]);
                if(currentColor.contains("red")){
                    red = val;
                } else if(currentColor.contains("blue")){
                    blue = val;
                } else {
                    green = val;
                }
            }

            //after getting color counts for each pull, check if the counts are valid
            if(red>12 || green>13 || blue>14){
                return 0;
            }
        }

        return gameNum;
    }
}
