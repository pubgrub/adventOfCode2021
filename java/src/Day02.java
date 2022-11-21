import java.util.List;


public class Day02 {
    public static void main(String[] args) throws Exception {
        
        List<String> lines = DataLoader.getLines( "02.data");
        
                
        int[] directions = new int[ lines.size()];
        int[] distances = new int[ lines.size()];
        
      
        int i = 0;
        String[] s = new String[2];
        for( String line : lines) {
            s = line.split( " ", -2);
            if( s[0].equals("forward")) {
                directions[i] = 0;
            } else if( s[0].equals("down")) {
                directions[i] = 1;
            } else {
                directions[i] = -1;
            }
            distances[i] = Integer.parseInt(s[1]);
            i++;
        }
    
        // Task 1
        
        int xPos = 0;
        int yPos = 0;

        for( i = 0; i < directions.length; i++) {
            if( directions[i] == 0) {
                xPos += distances[i];
            } else {
                yPos += distances[i] * directions[i];
            }
        }

        System.out.println( "Solution Task 1: " + xPos * yPos);
 
        // Task 2
        
        xPos = 0;
        yPos = 0;
        int aim = 0;

        for( i = 0; i < directions.length; i++) {
            if( directions[i] == 0) {
                xPos += distances[i];
                yPos += distances[i] * aim;
            } else {
                aim += distances[i] * directions[i];
            }
        }

        System.out.println( "Solution Task 2: " + xPos * yPos);

    }
}