import java.util.*;
import java.io.File;

public class DaySeven {
    //need an enum 2 to Ace to compare ranks

    //looks like i need to make a hand class:
    //this class will take in a String for it's constructor,
    //from this String it will populate an enum field
    //enum 7 vals:5ofKind,4ofKind,FullHouse,ThreeOfKind,2Pair,1Pair,HighCard
    //also populate an enum array size 5 of cards
    //also store the hand's bid

    //after having a list of compareable hands made, make a prio queue
    //highest rank hand has highest value

    //after prio queue made multiply bid*queuesize and pop off queue
    //add that vlaue to the sum

    public static void main(String[] args){
        String content = "";
        try{
            content = new Scanner(new File("input7.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }
        //god I hate this character
        content = content.replaceAll("\r","");

        String[] lines =  content.split("\n");
        PriorityQueue<Hand> queue = new PriorityQueue<>();
        int sum = 0;

        for(String line : lines){
            queue.add(new Hand(line));
        }

        System.out.println(queue.size());

        while(!queue.isEmpty()){
            System.out.println(queue.peek().bid +" "+ queue.peek().type.toString());
            sum += (queue.size())*(queue.poll().bid);
        }

        System.out.println(queue.size());

        System.out.println(sum);

    }
}