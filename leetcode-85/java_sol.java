class Solution {
    public int maximalRectangle(char[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int mx_a = 0;
        int i, j, k;
        int height, width;
        int[] acc = new int[m];

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
                for (k = j; k < m; ++k) {
                    height = Math.min(height, acc[k]);
                    if (height == 0) {
                        break;
                    }
                    width = (k - j + 1);
                    mx_a = Math.max(mx_a, height * width);
                }
            }
        }
        return mx_a;
    }
}
