
class WindowWeights:

    def create_window(left, right, weighter):
        # creates a function that yields a tuple of words, context and weight
        def window(document):
            doc_len = len(document)
            for iW, word in enumerate(document):
                for i in reversed(range(1, left)):
                    ictx = iW - i
                    if ictx <= 0:
                        break
                    ctx = document[ictx]
                    yield weighter(word, ctx, i, left)
                for i in range(1, right):
                    ictx = iW + i
                    if ictx >= doc_len:
                        break
                    ctx = document[ictx]
                    yield weighter(word, ctx, i, right)
        return window

    def weight_harmonic(word, context, dist, windowSize):
        # the harmonic weighing
        weight = 1.0 / dist
        return (word, context, weight)

    def weight_word2vec(word, context, dist, windowSize):
        # The word2vec weighing
        # In the paper, the word2vec weight is written as
        #      weight = (1.0 * dist) / windowSize
        # But that makes no sens to have a bigger weight for distant words,
        # so I inversed the formula
        weight = 1.0 * windowSize / dist
        return (word, context, weight)