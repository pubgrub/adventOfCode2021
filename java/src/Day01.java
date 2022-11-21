import java.util.List;


public class Day01 {
    public static void main(String[] args) throws Exception {
        
        List<String> lines = DataLoader.getLines( "01.data");
        int[] values = new int[ lines.size()];
        int i = 0;
        for( String line : lines) {
            values[ i] = Integer.parseInt(line);
            i++;
        }
    
        // Task 1
        
        int lastDepth = 99999999;
        int increased = 0;
        for( int d : values) {
            if( d > lastDepth) {
                increased++;
            }
            lastDepth = d;
        }
        System.out.println( "Solution Task 1: " + increased);

        // Task 2
        
        lastDepth = 99999999;
        increased = 0;
        for( i = 0; i < values.length - 2; i++) {
            int d = values[i] + values[i+1] + values[i+2];
            if( d > lastDepth) {
                increased++;
            }
            lastDepth = d;
        }
        System.out.println( "Solution Task 2: " + increased);

    }
}