import java.util.*;

public class main{
    public static void main(String[] args) {
        List<creatures> Animals = new ArrayList<creatures>();

        Animal lion = new Animal("Lion");
        Animals.add(lion);
        Animal dog = new Animal("Dog");
        Animals.add(dog);
        Animal cat = new Animal("Cat");
        Animals.add(cat);

        Animals.forEach(System.out::println);
        

        List<creatures> Plants = new ArrayList<creatures>();
        Plant tree = new Plant("Tree");
        Plants.add(tree);
        Plant sunflower = new Plant("Sunflower");
        Plants.add(sunflower);
        Plant grass = new Plant("Grass");
        Plants.add(grass);

        Plants.forEach(System.out::println);

        List<creatures> Fungis = new ArrayList<creatures>();
        Fungi blue = new Fungi("Blue Fungi");
        Fungis.add(blue);
        Fungi red = new Fungi("Red Fungi");
        Fungis.add(red);
        Fungi green = new Fungi("Green Fungi");
        Fungis.add(green);

        Fungis.forEach(System.out::println);
    }
}
