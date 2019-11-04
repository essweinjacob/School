import java.util.*;

public abstract class Creature implements Reproduction {
    public abstract String eatFood();
}

class Plant extends Creature implements Reproduction {

    @Override
    public String eatFood() {
        return "sunlight";
    }

    @Override
    public String modeOfReproduction(){
        return "Sexual Reproduction";
    }
}

class Animal extends Creature implements Reproduction {

    @Override
    public String eatFood() {
        return "ingestion";
    }

    @Override
    public String modeOfReproduction() {
        return "seeds";
    }
}

class Fungi extends Creature implements Reproduction {

    @Override
    public String eatFood() {
        return "external digestion with hyphae";
    }

    @Override
    public String modeOfReproduction() {
        return "Spores";
    }
}
