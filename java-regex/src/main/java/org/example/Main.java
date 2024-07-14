package org.example;


import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Main {

    /**
     * Replace every occurrence of "{id}"
     * with its ordinal occurrence number.
     * First occurrence replaced by 1
     * Second replaced by 2 and so on...
     */
    public static void main(String[] args) {
        String s = "This is id: {id}, then " +
                "another id {id}, " +
                "and last: {id}.";
        Pattern idPattern = Pattern
                .compile("(\\{id})");
        Matcher matcher = idPattern
                .matcher(s);
        StringBuilder builder =
                new StringBuilder();
        int id = 1;
        while (matcher.find()) {
            matcher.appendReplacement(
                    builder,
                    Integer.toString(id++)
            );
        }
        matcher.appendTail(builder);
        System.out.println("Final result:\n" +
                builder);
    }
}






