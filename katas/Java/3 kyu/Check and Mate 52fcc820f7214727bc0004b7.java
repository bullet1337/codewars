// https://www.codewars.com/kata/52fcc820f7214727bc0004b7
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class CheckAndMate {
    static PieceConfig[][] map;
    static PieceConfig king;
    static int[] plusMinusOnes = new int[]{-1, 1};

    static class Pair<T, V> {
        T first;
        V second;

        Pair(T f, V s) {
            first = f;
            second = s;
        }

        Pair() {}
    }

    static class Point extends Pair<Integer, Integer> {
        boolean enPassant;

        Point(int x, int y) {
            first = x;
            second = y;
        }

        public Point(int x, int y, boolean enPassant) {
            this(x, y);
            this.enPassant = enPassant;
        }

        @Override
        public int hashCode() {
            return Objects.hash(first, second);
        }

        @Override
        public boolean equals(Object obj) {
            return first.equals(((Point) obj).first) && second.equals(((Point) obj).second);
        }
    }

    public static boolean checkBounds(int x, int y) {
        return checkBound(x) && checkBound(y);
    }

    public static boolean checkBound(int b) {
        return 0 <= b && b <= 7;
    }

    public static Boolean checkPiece(PieceConfig piece, int player, String... conditions) {
        if (piece == null) {
            return null;
        }

        return !(piece.getOwner() == player) && (Stream.of(conditions).anyMatch(x -> piece.getPiece().equals(x)));
    }

    public static List<Pair<PieceConfig, Set<Point>>> checkRook(PieceConfig piece, boolean trace) {
        List<Pair<PieceConfig, Set<Point>>>  results = new ArrayList<>();
        Set<Point> points = null;

        for (int i : plusMinusOnes) {
            if (trace) {
                points = new HashSet<>();
            }
            for (int x = piece.getX() + i; checkBound(x); x += i) {
                if (trace) {
                    points.add(new Point(x, piece.getY()));
                }
                Boolean check = checkPiece(map[x][piece.getY()], piece.getOwner(), "rook", "queen");
                if (check != null) {
                    if (check) {
                        results.add(new Pair<>(map[x][piece.getY()], points));
                    }
                    break;
                }
            }
        }

        for (int j : plusMinusOnes) {
            if (trace) {
                points = new HashSet<>();
            }
            for (int y = piece.getY() + j; checkBound(y); y += j) {
                if (trace) {
                    points.add(new Point(piece.getX(), y));
                }
                Boolean check = checkPiece(map[piece.getX()][y], piece.getOwner(), "rook", "queen");
                if (check != null) {
                    if (check) {
                        results.add(new Pair<>(map[piece.getX()][y], points));
                    }
                    break;
                }
            }
        }

        return results;
    }

    public static List<Pair<PieceConfig, Set<Point>>> checkKnight(PieceConfig piece, boolean trace) {
        List<Pair<PieceConfig, Set<Point>>>  results = new ArrayList<>();
        Set<Point> points = null;

        for (int i = 1; i <= 2; ++i) {
            for (int ik : plusMinusOnes) {
                for (int j = 1; j <= 2; ++j) {
                    for (int jk : plusMinusOnes) {
                        if (i != j || ik != jk) {
                            int x = piece.getX() + i * ik;
                            if (!checkBound(x)) {
                                continue;
                            }

                            int y = piece.getY() + j * jk;
                            if (!checkBound(y)) {
                                continue;
                            }

                            Boolean check = checkPiece(map[x][y], piece.getOwner(), "knight");
                            if (check != null && check) {
                                if (trace) {
                                    points = new HashSet<>();
                                    points.add(new Point(x, y));
                                }
                                results.add(new Pair<>(map[x][y], points));
                            }
                        }
                    }
                }
            }
        }

        return results;
    }

    public static List<Pair<PieceConfig, Set<Point>>> checkPawn(PieceConfig piece, boolean trace) {
        List<Pair<PieceConfig, Set<Point>>>  results = new ArrayList<>();
        Set<Point> points = null;

        for (int i : plusMinusOnes) {
            int x = piece.getX() + i * (piece.getOwner() == 1 ? 1 : -1);
            if (!checkBound(x)) {
                continue;
            }

            int y = piece.getY() + (piece.getOwner() == 1 ? 1 : -1);
            if (!checkBound(y)) {
                continue;
            }

            Boolean check = checkPiece(map[x][y], piece.getOwner(), "pawn");
            if (check != null && check) {
                if (trace) {
                    points = new HashSet<>();
                    points.add(new Point(x, y));
                }
                results.add(new Pair<>(map[x][y], points));
            }
        }

        return results;
    }

    public static List<Pair<PieceConfig, Set<Point>>> checkBishop(PieceConfig piece, boolean trace) {
        List<Pair<PieceConfig, Set<Point>>>  results = new ArrayList<>();
        Set<Point> points = null;

        for (int i : plusMinusOnes) {
            for (int j : plusMinusOnes) {
                if (trace) {
                    points = new HashSet<>();
                }
                for (int x = piece.getX() + i, y = piece.getY() + j; checkBounds(x, y); x += i, y += j) {
                    if (trace) {
                        points.add(new Point(x, y));
                    }
                    Boolean check = checkPiece(map[x][y], piece.getOwner(), "bishop", "queen");
                    if (check != null) {
                        if (check) {
                            results.add(new Pair<>(map[x][y], points));
                        }
                        break;
                    }
                }
            }
        }

        return results;
    }

    public static List<Pair<PieceConfig, Set<Point>>> getChecks(PieceConfig piece, boolean trace, boolean all) {
        if (all) {
            return Stream.of(checkRook(piece, trace), checkKnight(piece, trace), checkPawn(piece, trace),
                             checkBishop(piece, trace)).flatMap(Collection::stream).collect(Collectors.toList());
        } else {
            List<Pair<PieceConfig, Set<Point>>> results = new ArrayList<>();
            results.addAll(checkRook(piece, trace));
            if (!results.isEmpty()) {
                return results;
            }

            results.addAll(checkKnight(piece, trace));
            if (!results.isEmpty()) {
                return results;
            }

            results.addAll(checkPawn(piece, trace));
            if (!results.isEmpty()) {
                return results;
            }

            results.addAll(checkBishop(piece, trace));
            return results;
        }
    }

    public static Set<PieceConfig> isCheck(PieceConfig[] arrPieces, int player) {
        init(arrPieces, player);

        return getChecks(king, false, true).stream().map(x -> x.first).collect(Collectors.toSet());
    }

    private static boolean tryMove(PieceConfig piece, Point p) {
        PieceConfig tmp = map[p.first][p.second + (p.enPassant ? (piece.getOwner() == 0 ? 1 : -1) : 0)];
        if (p.enPassant) {
            map[tmp.getX()][tmp.getY()] = null;
        }
        map[p.first][p.second] = new PieceConfig(piece.getPiece(), piece.getOwner(), p.first, p.second);
        map[piece.getX()][piece.getY()] = null;

        boolean result = getChecks(piece == king ? map[p.first][p.second] : king, false, false).isEmpty();

        if (p.enPassant) {
            map[tmp.getX()][tmp.getY()] = tmp;
        }
        map[piece.getX()][piece.getY()] = piece;
        map[p.first][p.second] = tmp;

        return result;
    }

    public static boolean isMate(PieceConfig[] arrPieces, int player) {
        init(arrPieces, player);

        List<Pair<PieceConfig, Set<Point>>> checks = getChecks(king, true, true);

        if (checks.isEmpty()) {
            return false;
        }

        for (Point move : getMoves(king)) {
            if (tryMove(king, move)) {
                return false;
            }
        }

        if (checks.size() > 1) {
            return true;
        }

        Set<Point> possibleMoves = checks.stream().flatMap(x -> x.second.stream()).collect(Collectors.toSet());
        for (PieceConfig piece : arrPieces) {
            if (piece != king && piece.getOwner() == king.getOwner()) {
                Set<Point> moves = getMoves(piece);
                moves.removeIf(x -> !x.enPassant && !possibleMoves.contains(x));
                for (Point move : moves) {
                    if (tryMove(piece, move)) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    private static Set<Point> getMoves(PieceConfig piece) {
        Set<Point> points = new HashSet<>();

        int x, y;
        switch (piece.getPiece()) {
            case "king":
                for (x = max(0, piece.getX() - 1); x <= min(7, piece.getX() + 1); ++x) {
                    for (y = max(0, piece.getY() - 1); y <= min(7, piece.getY() + 1); ++y) {
                        if ((x != piece.getX() || y != piece.getY())
                                && (map[x][y] == null || map[x][y].getOwner() != piece.getOwner())) {

                            points.add(new Point(x, y));
                        }
                    }
                }
                break;
            case "rook":
                for (int i : plusMinusOnes) {
                    for (x = piece.getX() + i; checkBound(x); x += i) {
                        points.add(new Point(x, piece.getY()));
                        if (map[x][piece.getY()] != null) {
                            break;
                        }
                    }
                }

                for (int j : plusMinusOnes) {
                    for (y = piece.getY() + j; checkBound(y); y += j) {
                        points.add(new Point(piece.getX(), y));
                        if (map[piece.getX()][y] != null) {
                            break;
                        }
                    }
                }
                break;
            case "knight":
                for (int i = 1; i <= 2; ++i) {
                    for (int ik : plusMinusOnes) {
                        for (int j = 1; j <= 2; ++j) {
                            for (int jk : plusMinusOnes) {
                                if (i != j || ik != jk) {
                                    x = piece.getX() + i * ik;
                                    if (!checkBound(x)) {
                                        continue;
                                    }

                                    y = piece.getY() + j * jk;
                                    if (!checkBound(y)) {
                                        continue;
                                    }

                                    if (map[x][y] == null) {
                                        points.add(new Point(x, y));
                                    }
                                }
                            }
                        }
                    }
                }
                break;
            case "pawn":
                y = piece.getY() + (piece.getOwner() == 1 ? 1 : -1);
                if (checkBound(y)) {
                    if (map[piece.getX()][y] == null) {
                        points.add(new Point(piece.getX(), y));
                        if (piece.getY() == (piece.getOwner() == 1 ? 1 : 6)) {
                            y += (piece.getOwner() == 1 ? 1 : -1);
                            if (checkBound(y) && map[piece.getX()][y] == null) {
                                points.add(new Point(piece.getX(), y));
                            }
                        }
                    }

                    y = piece.getY() + (piece.getOwner() == 1 ? 1 : -1);
                    for (int i : plusMinusOnes) {
                        x = piece.getX() + i * (piece.getOwner() == 1 ? 1 : -1);
                        if (!checkBound(x)) {
                            continue;
                        }

                        if (map[x][y] != null) {
                            if (map[x][y].getOwner() != piece.getOwner()) {
                                points.add(new Point(x, y));
                            }
                        } else {
                            PieceConfig enPassant = map[x][piece.getY()];
                            if (y == (piece.getOwner() == 1 ? 5 : 2) && enPassant != null
                                    && enPassant.getPiece().equals("pawn") && enPassant.getPrevX() == x
                                    && enPassant.getPrevY() == (enPassant.getOwner() == 0 ? 6 : 1)) {

                                points.add(new Point(x, y, true));
                            }
                        }
                    }
                }
                break;
            case "bishop":
                for (int i : plusMinusOnes) {
                    for (int j : plusMinusOnes) {
                        for (x = piece.getX() + i, y = piece.getY() + j; checkBounds(x, y); x += i, y += j) {
                            points.add(new Point(x, y));
                            if (map[x][y] != null) {
                                break;
                            }
                        }
                    }
                }
                break;
            case "queen":
                points.addAll(getMoves(new PieceConfig("bishop", piece.getOwner(), piece.getX(), piece.getY())));
                points.addAll(getMoves(new PieceConfig("rook", piece.getOwner(), piece.getX(), piece.getY())));
                break;
        }

        return points;
    }


    public static void init(PieceConfig[] arrPieces, int player) {
        map = new PieceConfig[8][8];
        for (PieceConfig piece : arrPieces) {
            map[piece.getX()][piece.getY()] = piece;
            if (piece.getOwner() == player && piece.getPiece().equals("king")) {
                king = piece;
            }
        }
    }
}