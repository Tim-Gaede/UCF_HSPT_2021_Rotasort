// Solution for Octopus (HSPT 2021 - On Site)
// Author: Atharva Nagarkar

#include <bits/stdc++.h>

using namespace std;

/*
* For this problem, one can see that performing a right cyclic shift on a subarray
* is the same as taking the last element in the subarray and placing it in front of
* the subarray. This can be generalized to simply taking one element out of the array
* and placing it somewhere else. Now we wish to see the minimum number elements to
* move to make the array sorted. This is equivalant to keeping maximum number of things
* the same in the array; one can realize that this value is the LIS (longest increasing subsequence)
* in the array. Thus, the answer to our problem is N - LIS(array), the total number of elements
* minus maximum number to keep the same = minimum number to move.
*/

int main() {

    // read in number of test cases
    int tests;
    cin >> tests;

    while(tests--) {

        // read in number of integers in the array
        int n;
        cin >> n;
        
        // keep a map with an invariant, which is that if there are two keys
        // in the map x < y, then dp[x] < dp[y]. If this is not the case,
        // then keeping around y is useless since you can build off x with a
        // strictly better answer
        map<int, int> dp;

        int ans = 1;
        for(int i = 0; i < n; ++i) {
            int x;
            cin >> x;

            // first lets see where to insert this element
            auto it = dp.upper_bound(x);

            // if this is the first element in the array, then it's answer is just 1
            if(it == dp.begin()) {
                dp[x] = 1;
                continue;
            }

            // get the best answer of the previous element
            // our current answer is the previous element's answer + 1
            it = prev(it);
            dp[x] = it->second + 1;
            ans = max(ans, dp[x]);

            // after inserting the answer for the current element, a bunch of entries
            // so while bad entries exist, remove them
            while(true) {
                it = dp.upper_bound(x);
                if(it == dp.end()) break;
                if(it->second <= dp[x]) {
                    dp.erase(it);
                } else {
                    break;
                }
            }
        }

        // print the answer!
        cout << n - ans << '\n';

    }

    return 0;
}

//69
