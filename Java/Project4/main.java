import java.util.*;

public class main{
    public static void main(String[] args) {
        // Game Setup
        //Board Creation
        char[][] board = new char [11][11];
        int shipType;
        String shipName;

        // Fill array
        for(int x = 0; x <= 10; x++){
            for(int y = 0; y <= 10; y++){
                board[x][y] = ' ';
            }
        }

        // Create Objects/Game pieces
        // Player 1 ship creation
        System.out.println("What ship would you like to pilot?");
        System.out.println("1. X-Wing");
        System.out.println("2. Tie Fighter");
        Scanner shipTypeInput = new Scanner(System.in);
        shipType = shipTypeInput.nextInt();
        System.out.println("What would you like to name your ship?");
        Scanner shipNameInput = new Scanner(System.in);
        shipName = shipNameInput.nextLine();
        Spaceship player1 = getSpaceship(shipType, shipName);
        
        //Player 2 ship creation
        System.out.println("What ship would you like to pilot?");
        System.out.println("1. X-Wing");
        System.out.println("2. Tie Fighter");
        shipType = shipTypeInput.nextInt();
        System.out.println("What would you like to name your ship?");
        shipNameInput = new Scanner(System.in);
        shipName = shipNameInput.nextLine();
        Spaceship player2 = getSpaceship(shipType, shipName);
        
        // Game Starts
        char turn = '1';
        board = placePieces(board, player1, turn);
        turn = '2';
        board = placePieces(board, player2, turn);
        displayBoard(board);

        turn = '1';
        String winner = "None";
        // Start the cycle
        while(winner == "None"){
            takeTurn(turn, board, player1, player2);
            displayBoard(board);
            winner = checkWinner(winner, player1, player2);
            turn = changeTurn(turn);
        }    
        
        // Print out message for winner
        if(winner == "player1"){
            System.out.println("Player 1 has won");
        }
        if(winner == "player2"){
            System.out.println("Player 2 has won");
        }
        if(winner == "both"){
            System.out.println("Some how, by the grace of god, you both died");
        }
    }

    // Prints out array similar to connect 4 project
    public static void displayBoard(char array[][]){
        for(int y = 10; y >= 0; y--){
            System.out.print(y);
            for(int x = 0; x <= 10; x++){
                if(y == 10){
                    if(x != 10){
                        System.out.print("|  " + array[x][y] + " ");
                    }
                    else{
                        System.out.print("|  " + array[x][y]);
                    }
                }
                else{
                    System.out.print(" | " + array[x][y] + " ");
                }
                if(x == 10){
                    System.out.print("|");
                }
            }
            System.out.println();
        }
        System.out.println("  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10|");
    }

    //Place the pieces on the board
    public static char[][] placePieces(char array[][], Spaceship player, char turn){
        array[player.getXPosition()][player.getYPosition()] = turn;

        return array;
    }

    //Creates spaceship class based on player choice
    public static Spaceship getSpaceship(int choice, String name){
        if (choice == 1) {
            return new XWing(name);
        }
        else{
            return new TieFighter(name);
        }
    }
            
    // Player takes their turn
    public static void takeTurn(char turn, char board[][], Spaceship player1, Spaceship player2){
        if(turn == '1'){
            // Max speed it turned to 'action points', that is, the higher speed the more movement you get
            // If battle is reached before you've used up your action points, it will go to the next players turn
            for(int actionPoints = player1.getMaxSpeed(); actionPoints > 0; actionPoints--){
                System.out.println("Player 1, you have " + actionPoints + " remaining, what would you like to do?");
                System.out.println("1. Move Up \n" +
                                   "2. Move Down \n" +
                                   "3. Move Right \n" +
                                   "4. Move Left \n" +
                                   "5. Print Diagnostics");
                Scanner choiceInput  = new Scanner(System.in);
                int choice = choiceInput.nextInt();
            
                if(choice == 1){
                    board = movePieces(board, player1);
                    player1.moveUp();
                    board = placePieces(board, player1, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 2){
                    board = movePieces(board, player1);
                    player1.moveDown();
                    board = placePieces(board, player1, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 3){
                    board = movePieces(board, player1);
                    player1.moveRight();
                    board = placePieces(board, player1, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 4){
                    board = movePieces(board, player1);
                    player1.moveLeft();
                    board = placePieces(board, player1, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 5){
                    player1.printShipDiagnostic();
                    actionPoints++;
                    displayBoard(board);
                }
            }
        }
        else{
            for(int actionPoints = player2.getMaxSpeed(); actionPoints > 0; actionPoints--){
                System.out.println("Player 2, you have " + actionPoints + " remaining, what would you like to do?");
                System.out.println("1. Move Up \n" +
                                   "2. Move Down \n" +
                                   "3. Move Right \n" +
                                   "4. Move Left \n" +
                                   "5. Print Diagnostics");
                Scanner choiceInput  = new Scanner(System.in);
                int choice = choiceInput.nextInt();
            
                if(choice == 1){
                    board = movePieces(board, player2);
                    player2.moveUp();
                    board = placePieces(board, player2, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 2){
                    board = movePieces(board, player2);
                    player2.moveDown();
                    board = placePieces(board, player2, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 3){
                    board = movePieces(board, player2);
                    player2.moveRight();
                    board = placePieces(board, player2, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 4){
                    board = movePieces(board, player2);
                    player2.moveLeft();
                    board = placePieces(board, player2, turn);
                    displayBoard(board);
                    checkBattle(board, player1, player2);
                }
                if(choice == 5){
                    player2.printShipDiagnostic();
                    actionPoints++;
                    displayBoard(board);
                }
            }
        }
    }

    public static char changeTurn(char turn){
        if(turn == '1'){
            turn = '2';
            return turn;
        }
        else{
            turn = '1';
            return turn;
        }
    }

    // Moves the pieces, around/removes the previous position of a player's piece
    public static char[][] movePieces(char board[][], Spaceship player){
        board[player.getXPosition()][player.getYPosition()] = ' ';
        return board;
    }

    // Checks if a battle has taken place
    public static void checkBattle(char board[][], Spaceship player1, Spaceship player2){
            // When the two players are on the same board spot
            if(player1.getXPosition() == player2.getXPosition() && player1.getYPosition() == player2.getYPosition()){
                System.out.println("BATTLE HAS BEGUN");
                battle(board, player1, player2);
            }
    }

    // Battle takes place
    public static void battle(char board[][], Spaceship player1, Spaceship player2){
        // Change health
        int health1 = player1.getShipHealth();
        int health2 = player2.getShipHealth();

        // Subtract each ships's attack power from their health
        health1 = player1.getShipHealth() - player2.getAttackPower();
        health2 = player2.getShipHealth() - player1.getAttackPower();

        player1.setShipHealth(health1);
        player2.setShipHealth(health2);

        // Randomize position
        board = movePieces(board, player1);
        board = movePieces(board, player2);
        player1.randomPosition();
        player2.randomPosition();

        // Place Pieces back down
        board[player1.getXPosition()][player1.getYPosition()] = '1';
        board[player2.getXPosition()][player2.getYPosition()] = '2';
    }

    // See if a player has won
    public static String checkWinner(String winner, Spaceship player1, Spaceship player2){
        if(player1.getShipHealth() <= 0 && player2.getShipHealth() <= 0){
            winner = "both";
            return winner;
        }
        if(player1.getShipHealth() <= 0){
            winner = "player2";
            return winner;
        }
        if(player2.getShipHealth() <= 0){
            winner = "player1";
            return winner;
        }
        else{
            return winner;
        }
    }
}
