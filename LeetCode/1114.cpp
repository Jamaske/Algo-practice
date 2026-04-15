#include <iostream>
#include <fstream>
#include <cstdint>
#include <functional>
using namespace std;


class Foo {
   private:
    bool latch2 = true;
    bool latch3 = true;

   public:
    Foo() {
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        latch2 = false;
    }

    void second(function<void()> printSecond) {
        while (latch2) continue;
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        latch3 = false;
    }

    void third(function<void()> printThird) {
        while (latch3) continue;
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};