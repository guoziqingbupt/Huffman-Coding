import HuffmanEncode
import HuffmanDecode

text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccccc" \
       "cccddddddddddddddddeeeeeeeeefffff"

if __name__ == "__main__":

    # generate root
    root = HuffmanEncode.encodeHelper(text)

    # encode
    codeWord = HuffmanEncode.huffmanEncode(text, root)
    print(codeWord)

    # decode
    print(HuffmanDecode.huffmanDecode(codeWord, root))
