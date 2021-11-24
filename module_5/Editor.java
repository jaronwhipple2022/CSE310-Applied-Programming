package CSE310_Applied_Programming.module_5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.stream.Stream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;

public class Editor {

    // create shortcut variable to receive input
    static Scanner input = new Scanner(System.in);

    // write file into designated folder
    public static void createDoc(String title, String text) {

        try {
            BufferedWriter writer = new BufferedWriter(
                    new FileWriter("C:\\Users\\jaron\\Desktop\\FALL 2021\\module5files\\" + title));
            writer.write(text);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // prompt user for their choice
    public static int decision() {

        System.out.print(
                "What would you like to do?\n 1: Create new file.\n 2: View existing Files.\n 3: Read existing file.\n 4: Quit. ");

        System.out.println();
        int choice = input.nextInt();
        input.nextLine();
        // return choice
        return choice;
    }

    // prompt user for the title and store it to a variable
    public static String getDocTitle() {

        System.out.print("Enter title ");
        String title = input.nextLine();
        // return title
        return title;
    }

    // prompt user for the text and store it to a variable
    public static String getDocText() {

        System.out.println("Enter the file text: ");
        String text = input.nextLine();
        // return text
        return text;
    }

    // prompt user for the title to read and store it to a variable
    public static String getTitleToRead() {

        System.out.println("Enter the file's name: ");
        String titleToRead = input.nextLine();
        // return text
        return titleToRead;
    }

    // read in the selected document into the terminal
    public static void getDoc(String titleToRead) {

        try {
            BufferedReader reader = new BufferedReader(
                    new FileReader("C:\\Users\\jaron\\Desktop\\FALL 2021\\module5files\\" + titleToRead));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // display an array of existing documents
    public static void getExistingDocs() {

        // get folder where files are stored
        Path path = Paths.get("C:\\Users\\jaron\\Desktop\\FALL 2021\\module5files");

        // blank line to keep it tidy
        System.out.println("");

        // "walk" through the directory, print each existing file
        try (Stream<Path> subPaths = Files.walk(path)) {
            subPaths.forEach(System.out::println);
            input.nextLine();

        } catch (

        IOException e) {
            e.printStackTrace();
        }

        // blank line to keep it tidy
        System.out.println("");
    }

    public static void main(String[] args) {

        // begin loop that will ask the user what they wish to do.
        while (decision() != 4) {
            if (decision() == 1) {
                // call functions to create a new file
                createDoc(getDocTitle(), getDocText());
            } else if (decision() == 2) {
                // call function to display existing files
                getExistingDocs();
            } else if (decision() == 3) {
                // call function to read a desired file
                getDoc(getTitleToRead());
            }

            // blank line to keep it tidy each time loop is run
            System.out.println("");
        }

    }
}
