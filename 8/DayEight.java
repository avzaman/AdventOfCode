import java.util.*;
import java.io.File;

public class DayEight {

    /*
     * Main method to code run code this time
     */
    public static void main(String[] args){

        //reading my text hehehehehe
        String content = "";
        try{
            content = new Scanner(new File("input7.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }
        //god I hate this character
        content = content.replaceAll("\r","");

        String[] lines =  content.split("\n");


    }

}
