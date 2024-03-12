def countValidWords(sentence: str) -> int:
    startList = sentence.split()
    count = 0

    for word in startList:
        if word.isalpha() and word.islower():
            count += 1
        else:
            punctuation_count = 0
            index_punctuation = -1
            for i in range(len(word)):
                if not word[i].isalpha():
                    punctuation_count += 1
                    index_punctuation = i

            if punctuation_count == 2:
                index_first_p = word.find('-')
                index_second_p = -1

                if '.' in word:
                    index_second_p = word.find('.')
                elif ',' in word:
                    index_second_p = word.find(',')
                elif '!' in word:
                    index_second_p = word.find('!')

                if -1 in [index_first_p, index_second_p]:
                    continue
                else:
                    if 0 < index_first_p < len(word) - 1 and index_second_p == len(word) - 1:
                        if index_second_p - index_first_p > 1:
                            count += 1

            elif punctuation_count == 1:
                if word[index_punctuation] == '-' and 0 < index_punctuation < len(word) - 1:
                    count += 1
                elif word[index_punctuation] in [',', '.', '!'] and index_punctuation == len(word) - 1:
                    count += 1
                else:
                    continue

    return count


# sentence = "alice and  bob are playing stone-game10"
# sentence = "!this  1-s b8d!"
# sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# sentence = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
# print(countValidWords(sentence))
