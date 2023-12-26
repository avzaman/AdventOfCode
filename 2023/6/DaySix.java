import java.util.*;
import java.io.File;

public class DaySix {
    //so it looks looks like t/2 gives the most optimal button to travel ratio for time
    //this results in a maximum distance
    //so find this then test each factor counting down from t/2
    //eventually you will find a number less than the record time, at which you stop
    //keep count of all the winning way and multiply by 2,
    //for even times add 1

    /*
     * method for counting total solutions to a single race
     */
    static int checkRace(int time, int distance){

    }

    public static void main(String[] args){
        

        String content = "";
        try{
            content = new Scanner(new File("input6.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }
        //god I hate this character
        content = content.replaceAll("\r","");    
    }
    
}
