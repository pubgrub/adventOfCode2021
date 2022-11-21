import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class DataLoader {

  public static List<String> getLines( String fileName) {
    
    List<String> lines = null;
    try {
//      lines = Files.readAllLines( Paths.get( "data", fileName));  
      lines = Files.readAllLines( Paths.get( fileName));  
    } catch( IOException e) {
        System.exit(1);
      }
      return lines;
    }
  }
