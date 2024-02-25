int maxScore(char* s) {
    int index, max_score, left, right, len;
    max_score = len = index = 0;

    while (s[index] != '\0') index += 1;

    len = index;
    index = 1;

    while (s[index] != '\0') {
        left = right = 0;
        for (int i = 0; i < index; i++) {
            if (s[i] == '0') left += 1;
        }
        for (int j = index; j < len; j++) {
            if (s[j] == '1') right += 1;
        }

        if (left + right > max_score) max_score = left + right;
        index += 1;
    }
    return max_score;
}
