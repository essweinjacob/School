import java.util.*;

public abstract class creatures implements Reproduction {
    public abstract String eatFood();
    public abstract String modeOfReproduction();
    public abstract String toString();
}

class Plant extends creatures implements Reproduction {
    private String plantName;

    Plant(String name) {
        plantName = name;
    }
    
    public String getName() {
        return plantName;
    }

    @Override
    public String eatFood() {
        return "Sunlight";
    }

    @Override
    public String modeOfReproduction(){
        return "Seeds";
    }

    public String toString(){
        return "Name: " + getName() + "\nFood eaten: " + eatFood() + "\nType of sexual reproduction: " + modeOfReproduction() + "\n";
    }
}

class Animal extends creatures implements Reproduction {
    private String animalName;

    Animal(String name){
        animalName = name;
    }

    public String getName() {
        return animalName;
    }

    @Override
    public String eatFood() {
        return "Ingestion";
    }

    @Override
    public String modeOfReproduction() {
        return "Sexual Reproduction";
    }

    public String toString(){
        return "Name: " + getName() + "\nFood eaten: " + eatFood() + "\nType of sexual reproduction: " + modeOfReproduction() + "\n";
    }

}

class Fungi extends creatures implements Reproduction {
    private String fungiName;

    Fungi(String name){
        fungiName = name;
    }

    public String getName() {
        return fungiName;
    }

    @Override
    public String eatFood() {
        return "External digestion with hyphae";
    }

    @Override
    public String modeOfReproduction() {
        return "Spores";
    }

    public String toString(){
        return "Name: " + getName() + "\nFood eaten: " + eatFood() + "\nType of sexual reproduction: " + modeOfReproduction() + "\n";
    }
}
