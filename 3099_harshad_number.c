int sumOfTheDigitsOfHarshadNumber(int x) {
    int sum_numbers = 0;
    int number = x;
    while (x > 0) {
        sum_numbers += x % 10;
        x = (int) x / 10;
    }
    if (number % sum_numbers == 0) {
        return sum_numbers;
    } else {
        return -1;
    }
}