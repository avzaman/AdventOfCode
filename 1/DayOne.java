import java.util.Scanner;
import java.io.*;

public class DayOne {
    public static void main(String args[]){
        int sum = 0;

        try{
            String content = new Scanner(new File("input.txt")).useDelimiter("\\Z").next();

            String[] lines = content.split("\n");

            for(String line:lines){
                sum += findVal(line);
            }
            System.out.println(sum );
        } catch (Exception e){
            System.out.print(e);
        }
    }

    static int findVal(String in){
        int a, b;
        a = 0; b= 0;

        for(int i = 0; i<in.length();i++){
            if(Character.isDigit(in.charAt(i))){
                a = Character.getNumericValue(in.charAt(i));
                break;
            }
        }

        for(int i = in.length()-1; i>=0;i--){
            if(Character.isDigit(in.charAt(i))){
                b = Character.getNumericValue(in.charAt(i));
                break;
            }
        }

        return (a*10)+b;
    }
}