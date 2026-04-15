#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdint>
using namespace std;


class Solution {
   public:
    /*
     Sliding window (j, i]
     contains 0 or 1 copy of a char -> 1 bit per char = 16B
     both indexies walks ~ n
    */
    int SlidingWindow(string s) {
        bitset<128> entries;
        int j = -1;
        char ret, exp;
        int best = 0;
        for (int i = 0; i < s.size(); i++) {
            exp = s[i];
            if (entries[exp]) {
                do {
                    ret = s[++j];
                    entries[ret] = false;
                } while (ret != exp);
            }
            entries[exp] = true;
            best = max(best, i - j);
        }
        return best;
    }

    /*
     Window of [i,j] due to unsigned JumpTable log2(5*10^4) ~ 15.61 -> uint16_t[128]
     zero encoding character absence in JT.
    */
    int JumpTable(string s) {
        uint16_t JT[128] = {};

        int j = 0;
        int best = 0;
        char exp;
        for (int i = 0; i < s.size(); i) {
            exp = s[i];
            j = max<int>(j, JT[exp]);
            JT[exp] = ++i;
            best = max(best, i - j);
        }
        return best;
    }
};