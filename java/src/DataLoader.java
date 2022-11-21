import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class DataLoader {

  public static List<String> getLines( String fileName) {
    
    List<String> lines = null;
    String p1 = Paths.get("").toAbsolutePath().toString();
    Path p = Paths.get( p1, "java", "src", "data", fileName);
    
    try {
      lines = Files.readAllLines( p);  
    } catch( IOException e) {
      System.exit(1);
    }
    return lines;
  }
}
