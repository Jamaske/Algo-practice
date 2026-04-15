#include <iostream>
#include <fstream>
#include <cstdint>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
   public:
    double lazyFullSort(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(), nums2.begin(), nums2.end());
        sort(nums1.begin(), nums1.end());
        int size = nums1.size();
        return static_cast<double>(nums1[size >> 1] + nums1[(size - 1) >> 1]) / 2;
    }

    double SortingMerge(vector<int>& nums1, vector<int>& nums2) {
        int size = nums1.size() + nums2.size(), i = 0;
        nums1.push_back(INT32_MAX);
        nums2.push_back(INT32_MAX);

        vector<int>::iterator src1 = nums1.begin(), src2 = nums2.begin();
        while (i < (size - 1) >> 1) {
            if (*src1 <= *src2)
                src1++;
            else
                src2++;
            i++;
        }
        int res;
        if (*src1 <= *src2) {
            res = *src1++;
        } else {
            res = *src2++;
        }

        if (size & 1) {
            return static_cast<double>(res);
        } else {
            return static_cast<double>(res + min(*src1, *src2)) / 2;
        }
    }
};

// OMG auditorial was wild