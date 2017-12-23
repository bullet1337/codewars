// https://www.codewars.com/kata/54eb33e5bc1a25440d000891
import java.util.*;
import java.util.stream.Collectors;

public class Decompose {

    class State {
        long current, sum;
        LinkedList<Long> result;

        public State(long n) {
            this.current = n - 1;
            this.sum = 0;
            this.result = new LinkedList<>();
        }

        public State(State other, boolean skipCurrent) {
            this.current = other.current - 1;
            this.sum = skipCurrent ? other.sum : other.sum + other.current * other.current;
            this.result = new LinkedList<>(other.result);

            if (!skipCurrent) {
                this.result.push(other.current);
            }
        }
    }

    public String decompose(long n) {
        long nSquare = n * n;

        Deque<State> states = new ArrayDeque<>();
        states.push(new State(n));

        LinkedList<Long> result = null;
        State state;
        while ((state = states.poll()) != null) {
            if (state.sum == nSquare) {
                result = new LinkedList<>(state.result);
                break;
            } else if (state.current > 0 && state.sum < nSquare) {
                states.push(new State(state, true));
                states.push(new State(state, false));
            }
        }

        return String.join(" ", result.stream().map(Object::toString).collect(Collectors.toList()));
    }
}