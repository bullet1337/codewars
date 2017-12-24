// https://www.codewars.com/kata/58924f2ca8c628f21a0001a1
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class BF_Translator {
    static Set<Character> alphabet = Stream.of('.', ',', '+', '<', '>', '+', '-', '[', ']').collect(Collectors.toSet());
    static Map<Character, Character> commandsReverse = new HashMap<>();
    static Map<Character, String> commandsMap = new HashMap<>();
    static Map<Integer, String> prefixes = new HashMap<>();

    static {
        commandsMap.put('+', "*p += ");
        commandsMap.put('-', "*p -= ");
        commandsMap.put('>', "p += ");
        commandsMap.put('<', "p -= ");
        commandsMap.put('.', "putchar(*p)");
        commandsMap.put(',', "*p = getchar()");

        commandsReverse.put('+', '-');
        commandsReverse.put('-', '+');
        commandsReverse.put('>', '<');
        commandsReverse.put('<', '>');

        prefixes.put(0, "");
    }

    public static class Node {
        char c;
        int count;
        int level;
        String prefix;

        Node(char c) {
            this.c = c;
        }

        Node(char c, int count, int level) {
            this(c);
            if (c != '.' && c != ',') {
                this.count = count;
            }
            this.level = level;
            this.prefix = prefixes.get(level);
        }

        Node(String code, int level) {
            this.prefix = prefixes.get(level) + code;
        }
    }

    public static class Level {
        LinkedList<Node> nodes = new LinkedList<>();

        Level(int level) {

        }
    }

    public static String getCode(LinkedList<Node> nodes) {
        StringBuilder code = new StringBuilder();
        for (Node node : nodes) {
            if (node.c != 0) {
                code.append(node.prefix).append(commandsMap.get(node.c)).append(node.count == 0 ? "" : node.count)
                          .append(";\n");
            } else {
                code.append(node.prefix);
            }
        }

        return code.toString();
    }

    public static void addNode(LinkedList<Node> nodes, char lastChar, int count, int level) {
        Node lastNode = nodes.peekLast(), newNode;

        if (lastChar != 0 && count != 0) {
            if (lastNode != null
                    && ((commandsReverse.getOrDefault(lastChar, '0') == lastNode.c)
                    || (lastChar != '.' && lastChar != ',' && lastChar == lastNode.c))) {

                if (lastChar == lastNode.c) {
                    lastNode.count += count;
                } else {
                    lastNode.count -= count;
                }

                if (lastNode.count == 0) {
                    nodes.removeLast();
                    return;
                }

                newNode = lastNode;
            } else {
                newNode = new Node(lastChar, count, level);
                nodes.add(newNode);
            }

            if (newNode.count < 0) {
                newNode.c = commandsReverse.get(newNode.c);
                newNode.count = -newNode.count;
            }
        }
    }

    public static String parseString(String code) {
        int position = 0;
        Deque<LinkedList<Node>> stack = new ArrayDeque<>();
        stack.push(new LinkedList<>());
        LinkedList<Node> currentLevel = stack.peek();

        char lastChar = 0;
        int count = 1;
        while (position < code.length()) {
            char c = code.charAt(position++);
            switch (c) {
                case '[':
                    addNode(currentLevel, lastChar, count, stack.size() - 1);
                    stack.push(new LinkedList<>());
                    prefixes.putIfAbsent(stack.size() - 1, String.join("", Collections.nCopies(stack.size() - 1, "  ")));
                    currentLevel = stack.peek();
                    lastChar = 0;
                    count = 1;
                    break;
                case ']':
                    stack.pop();
                    if (stack.size() > 0) {
                        addNode(currentLevel, lastChar, count, stack.size());

                        if (currentLevel.size() > 0) {
                            stack.peek().add(new Node("if (*p) do {\n", stack.size() - 1));
                            stack.peek().addAll(currentLevel);
                            stack.peek().add(new Node("} while (*p);\n", stack.size() - 1));
                        }

                        currentLevel = stack.peek();
                        lastChar = 0;
                        count = 1;
                    } else {
                        return "Error!";
                    }
                    break;
                default:
                    if (lastChar == 0) {
                        lastChar = c;
                    } else {
                        if (lastChar == c && c != '.' && c != ',') {
                            ++count;
                        } else {
                            if (commandsReverse.getOrDefault(c, '0') == lastChar) {
                                --count;
                            } else {
                                addNode(currentLevel, lastChar, count, stack.size() - 1);
                                lastChar = c;
                                count = 1;
                            }
                        }
                    }
                    break;
            }
        }

        if (stack.size() != 1) {
            return "Error!";
        }

        addNode(currentLevel, lastChar, count, stack.size() - 1);
        return getCode(currentLevel);
    }

    public static String translateToC(String input) {
        input = input.replaceAll("[^+-.,><\\[\\]]", "");

        int length;
        do {
            length = input.length();
            input = input.replaceAll("><|<>|\\+-|-\\+|\\[]", "");
        } while (length != input.length());
        return parseString(input);
    }
}