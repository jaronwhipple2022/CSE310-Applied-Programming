package CSE310_Applied_Programming.module_5;

import java.io.Serializable;

public class Document implements Serializable {
    // declare variables
    private String documentName;
    private String text;

    // getter setter methods
    public Document(String aDocumentName, String theText) {
        documentName = aDocumentName;
        text = theText;
    }

    // create method to return the document name
    public String getName() {
        return documentName;
    }

    // create method to return text
    public String getText() {
        return text;
    }
}
