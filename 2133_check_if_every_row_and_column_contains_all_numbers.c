bool checkValid(int** matrix, int matrixSize, int* matrixColSize) {
    int flag = 1;
    int flag_number = 0;

    for (int i = 1; i <= matrixSize; i++) {
        flag_number += i * i;
    }

    int curr_number;
    for (int x = 0; x < matrixSize; x++) {
        curr_number = 0;
        for (int y = 0; y < matrixSize; y++) {
            curr_number += matrix[x][y] * matrix[x][y];
        }
        if (curr_number != flag_number) {
            flag = 0;
            break;
        }
    }

    for (int y = 0; y < matrixSize; y++) {
        curr_number = 0;
        for (int x = 0; x < matrixSize; x++) {
            curr_number += matrix[x][y] * matrix[x][y];
        }
        if (curr_number != flag_number) {
            flag = 0;
            break;
        }
    }

    if (flag) return true;
    else return false;
}