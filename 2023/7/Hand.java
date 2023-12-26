import java.util.*;

public class Hand implements Comparable<Hand> {

    static enum Card {
        TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE
    }

    static enum HandType {
        HIGHCARD, ONEPAIR, TWOPAIR, THREEKIND, FULLHOUSE, FOURKIND, FIVEKIND
    }

    Card[] cards;
    HandType type;
    int bid;

    public Hand(String line) {
        String[] thisHand = line.split(" ");
        
        this.bid = Integer.parseInt(thisHand[1]);
        cards = new Card[5];
        String[] cardsStrings = thisHand[0].split("");

        //System.out.println(bid);
        //System.out.println(Arrays.toString(cardsStrings));

        for (int i = 0; i < cards.length; i++) {
            switch (cardsStrings[i]) {
                case "2":
                    cards[i] = Card.TWO;
                    break;
                case "3":
                    cards[i] = Card.THREE;
                    break;
                case "4":
                    cards[i] = Card.FOUR;
                    break;
                case "5":
                    cards[i] = Card.FIVE;
                    break;
                case "6":
                    cards[i] = Card.SIX;
                    break;
                case "7":
                    cards[i] = Card.SEVEN;
                    break;
                case "8":
                    cards[i] = Card.EIGHT;
                    break;
                case "9":
                    cards[i] = Card.NINE;
                    break;
                case "T":
                    cards[i] = Card.TEN;
                    break;
                case "J":
                    cards[i] = Card.JACK;
                    break;
                case "Q":
                    cards[i] = Card.QUEEN;
                    break;
                case "K":
                    cards[i] = Card.KING;
                    break;
                case "A":
                    cards[i] = Card.ACE;
                    break;
                default:
                    System.out.println("parse card err");
                    break;
            }
        }
        type = setHandType(cards);

        //System.out.println(type.toString());
    }

    /*
     * method to set hand type given then array of cards
     * using a hash map wey push the cards as keys,
     * their value is the count of the cards
     * if size is 5 highcard, if size = 1 fivekind,
     * if size is 4 onepair,
     * if size is 2 four of kind or full house,
     * if size is 3 threekind or twopair,
     */
    static HandType setHandType(Card[] cards) {
        HashMap<Card, Integer> counts = new HashMap<>();

        for(Card c: cards){
            if(counts.containsKey(c)){
                counts.replace(c,counts.get(c)+1);
            }else{
                counts.put(c,1);
            }
        }

        if(counts.size() == 5){
            return HandType.HIGHCARD;
        } else if(counts.size() == 4){
            return HandType.ONEPAIR;
        } else if(counts.size() == 1){
            return HandType.FIVEKIND;
        } else if(counts.size() == 2){
            if(counts.values().contains(3)){
                return HandType.FULLHOUSE;
            } else{
                return HandType.FOURKIND;
            }
        } else{
            if(counts.values().contains(3)){
                return HandType.THREEKIND;
            } else{
                return HandType.TWOPAIR;
            }
        }
    }

    /*
     * method to compare hands to each other for prio queue
     */
    @Override
    public int compareTo(Hand h) {
        if (this.type != h.type) {
            return -this.type.compareTo(h.type);
        } else {
            for (int i = 0; i < this.cards.length; i++) {
                if (!this.cards[i].equals(h.cards[i])) {
                    return -this.cards[i].compareTo(h.cards[i]);
                }
            }
        }
        return 0;
    }
}