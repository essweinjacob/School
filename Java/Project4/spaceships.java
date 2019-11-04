import java.util.*;

class Spaceship {
    private String shipName;
    private String engineType;
    private int maxSpeed;
    private int shipHealth;
    private int attackPower;
    private int xPosition;
    private int yPosition;
    private int shieldHealth;
    private int shipType;

    // Default constructor
    Spaceship(){
        Random mS = new Random();

        shipName = "why are you going here?";
        engineType = "potato";
        maxSpeed = (int)(Math.random() * 3 + 1);
        shipHealth = (int)(Math.random() * 100 + 50);
        attackPower = (int)(Math.random() * 20 + 5);
        xPosition = (int)(Math.random() * 10);
        yPosition = (int)(Math.random() * 10);
    }

    // Overloaded constructor
    Spaceship(String inputShipName){
        Random mS = new Random();

        shipName = inputShipName;
        engineType = "non-default";
        maxSpeed = (int)(Math.random() * 3 + 1);
        shipHealth = (int)(Math.random() * 100 + 50);
        attackPower = (int)(Math.random() * 20 + 5);
        xPosition = (int)(Math.random() * 10);
        yPosition = (int)(Math.random() * 10);
    }

    // Moves piece up
    void moveUp(){
        if(yPosition == 10){
            System.out.println("You cant go up any further you igit. Now you wasted your turn");
        }
        else{
            yPosition = yPosition + 1;
        }
    }
    
    // Moves pieces down
    void moveDown(){
        if(yPosition == 0){
            System.out.println("You cant go down any further you igit. Now you wasted your turn");
        }
        else{
            yPosition = yPosition - 1;
        }
    }

    // Moves piece to the left
    void moveLeft(){
        if(xPosition == 0){
            System.out.println("You cant go left any further you igit. Now you waster your turn");
        }
        else{
            xPosition = xPosition - 1;
        }
    }

    // Moves piece to the right
    void moveRight(){
        if(xPosition == 10){
            System.out.println("You cant go right any further you igit. Now you wasted your turn");
        }
        else{
            xPosition = xPosition + 1;
        }
    }
    
    // Prints ship diagnostics
    void printShipDiagnostic(){
        System.out.println("Ship Name: " + shipName);
        System.out.println("Engine type: " + engineType);
        System.out.println("Max Speed: " + maxSpeed);
        System.out.println("Ship Health: " + shipHealth);
        System.out.println("Attack Power: " + attackPower);
        System.out.println("X-Position: " + xPosition);
        System.out.println("Y-Position: " + yPosition);
    }
    
    // Resets the position of the pieces
    void randomPosition(){
        xPosition = (int)(Math.random() * 10);
        yPosition = (int)(Math.random() * 10);
    }

    // Gets ship name
    String getShipName(){
        return shipName;
    }

    // Sets ship name
    void setShipName(String inShipName){
        shipName = inShipName;
    }
    
    // Sets engine type
    void setEngineType(String inEngineType){
        engineType = inEngineType;
    }

    // Gets max speed
    int getMaxSpeed(){
        return maxSpeed;
    }

    // Sets max speed
    void setMaxSpeed(int inMaxSpeed){
        maxSpeed = inMaxSpeed;
    }

    // Gets ship health
    int getShipHealth(){
        return shipHealth;
    }

    // Gets attack power
    int getAttackPower(){
        return attackPower;
    }

    // Sets attack power
    void setAttackPower(int inAttackPower){
        attackPower = inAttackPower;
    }

    // Gets x position
    int getXPosition(){
        return xPosition;
    }

    // Gets y position
    int getYPosition(){
        return yPosition;
    }

    // Sets ship health
    void setShipHealth(int newHealth){
        shipHealth = newHealth;
    }
}

// XWing sub class
class XWing extends Spaceship{
    String engineType = "Default X-Wing Engine";
    //This ship will be faster and have 'more' attack power, but will have less default health
    int shipHealth = 60;
    int maxSpeed = 3;
    int attackPower = 10;

    XWing(){
        setEngineType(engineType);
        setMaxSpeed(maxSpeed);
        setAttackPower(attackPower);
        setShipHealth(shipHealth);
    }

    XWing(String inputShipName){
        setShipName(inputShipName);
        setEngineType(engineType);
        setMaxSpeed(maxSpeed);
        setAttackPower(attackPower);
        setShipHealth(shipHealth);
    }
}

// Tie Fighter subclass
class TieFighter extends Spaceship{
    String engineType = "Default Tie Fighter Engine";
    // This ship will be tankyier by default, buy slower
    int shipHealth = 90;
    int maxSpeed = 1;

    TieFighter(){
        setEngineType(engineType);
        setShipHealth(shipHealth);
        setMaxSpeed(maxSpeed);
    }

    TieFighter(String inputShipName){
        setShipName(inputShipName);
        setEngineType(engineType);
        setShipHealth(shipHealth);
        setMaxSpeed(maxSpeed);
    }
}
