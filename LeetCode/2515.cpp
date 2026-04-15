#include <iostream>
#include <fstream>
#include <cstdint>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
   public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int size = words.size();
        if (words[startIndex] == target) return 0;
        int i = startIndex, j = startIndex, dist = 0;

        while (true) {
            ++dist;
            if (++i == size) i = 0;
            if (--j == -1) j = size - 1;
            if (words[i] == target || words[j] == target) return dist;
        }
    }
};