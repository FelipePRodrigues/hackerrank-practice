from string import ascii_lowercase as alphabet


def designerPdfViewer(h, word):
    word_letters = list(set(word))
    max_height = 0

    for letter in word_letters:
        if h[alphabet.index(letter)] > max_height:
            max_height = h[alphabet.index(letter)]

    return max_height * len(word)


class TestDesignerPdfViewer:
    def test_1(self):
        assert designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc') == 9

    def test_2(self):
        assert designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba') == 28
