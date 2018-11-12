package me.henryfbp.myapplication;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);

        System.out.println(stuff(20));
    }

    // Example of simple Java syntax. Used in 'Java crash course'.
    public java.lang.Integer stuff(Integer argument) {

        if (argument >= 20) {
            return (argument + 200);
        }

        String msg = "Hello there!";

        if (msg.contains("the")) {
            return 20;
        } else {
            return -1;
        }
    }
}