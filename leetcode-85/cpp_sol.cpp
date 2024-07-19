class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        int mx_a = 0;
        int i, j, k;
        int height, width;

        vector<int> acc(m, 0);

        for (i = 0 ; i < n ; ++i) {
            for (j = 0 ; j < m ; ++j) {
                if (matrix[i][j] == '1') {
                    ++acc[j];
                } else {
                    acc[j] = 0;
                }
            }
            for (j = 0; j < m; ++j) {
                height = 100000;
                for (k = j; k < m && height != 0; ++k) {
                    height = min(height, acc[k]);
                    width = (k - j + 1);
                    mx_a = max(mx_a, height * width);
                }
            }
        }
        return mx_a;
        
    }
};
