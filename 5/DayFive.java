import java.util.*;
import java.io.File;

public class DayFive {
    //create array of seeds, the index is the seed number
    //the value at each index willl change as we use maps
    //the maps will change values to correlate with new category

    //create a list of ranges from current map
    //run each seed over all the possible ranges in the map
    //once it lands in a range find the offset with:
    //seed[i] - lowEndOfFirstCat
    //then add the offset to the low end of second category
    //then set that number as the new value fr seed[i]
    //if number falls in no range then seed[i] remains unchanged

    //for some fuck all reason the format in each range is:
    //destinationStart sourceStart rangeLength
    //instead of source then destination but whatever

    //after going over every seed with every map
    //find the min of the seed array

    /*
     * Range class to store ranges for a row of a map
     */
    static class Range{
        long srcStart, srcEnd, desStart;

        public Range(long src, long des, long len){
            srcStart = src;
            srcEnd = src+len-1;
            desStart = des;
        }
    }

    /*
     * method to create ranges for a map
     */
    static List<Range> createRanges(String map){
        //split by colon then by \n, forget index 0 and last cuz just \n
        List<Range> ranges = new ArrayList<>();
        String[] rangeStrings = map.split(":")[1].split("\n");
        String[] row;// = new String[3];
        long src, des, len;
        //System.out.println(Arrays.toString(rangeStrings));

        for(String s : rangeStrings){
            if(s.equals("")){continue;}
            row = s.split(" ");
            src = Long.parseLong(row[1]);
            des = Long.parseLong(row[0]);
            len = Long.parseLong(row[2]);
            ranges.add(new Range(src,des,len));
        }

        return ranges;
    }

    /*
     * method to return new value by sifting seed through a map's ranges
     */
    static long remapSeed(List<Range> ranges, long seed){
        long offset = 0;
        for(Range range : ranges){
            if(seed >= range.srcStart && seed <= range.srcEnd){
                offset = seed - range.srcStart;
                return range.desStart + offset;
            }
        }
        return seed;
    }

    /*
     * method to find min of unsorted int array
     */
    static long findMin(long[] seeds){
        long min = Long.MAX_VALUE;
        for(long num : seeds){
            if(num < min){
                min = num;
            }
        }
        return min;
    }

    /*
     * driver method!!!!
     */
    public static void main(String[] args){
        //read in the input txt file
        String content = "";
        try{
            content = new Scanner(new File("input5.txt")).useDelimiter("\\Z").next();
            
        } catch (Exception e){
            System.out.print(e);
        }
        //god I hate this character
        content = content.replaceAll("\r","");

        String[] maps =  content.split("Z");

        String[] seedStrings = maps[0].split(" ");

        //create list of seeds
        //-2 length accounting for text out front and \n in back
        long[] seeds = new long[seedStrings.length-2];
        for(int i = 1; i < seedStrings.length-1;i++){
            seeds[i-1] = Long.parseLong(seedStrings[i]);
        }

        //loop over all maps
        //in each map loop, create list of ranges
        //for every seed check range list and change seed[i] accordingly
        //System.out.println(Arrays.toString(maps));
        for(int i = 1; i < maps.length;i++){
            List<Range> ranges = createRanges(maps[i]);
            for(int j = 0; j < seeds.length; j++){
                seeds[j] = remapSeed(ranges,seeds[j]);
            }
        }

        //find min of seeds (technically now they're locations)
        System.out.println(findMin(seeds));
    }
}