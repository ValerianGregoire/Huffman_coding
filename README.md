# Huffman_coding
An algorithm to encode any message using Huffman coding

## Context
This code was made for computer science engineering students from the UTC a few months ago as an example on how to encode a string using Huffman encoding algorithm.

## Important fact
I think I was able to code a proper encoding algorithm, but I must admit that it is quite complicated to check and to decode the encoded messages as the weights of each character lead to arbitrary paths in the min heap tree, which lead to:
>letustestthisencoding

becoming:
>0010 0100 0111 0011 0101 0111 0100 0101 0111 0111 0100 1101 0101 0100 0000 0101 0110 0111 1101 0000 1100

which is decrypted as:
>TTOADNDONDDTHHLSHAEDSA

That is not so nice, but at least we get a series of ones and zeroes.

### On a more serious note, the weight of each character does follow the encoding rules, which means that the odds for the algorithm to be correct are high.
Only the decrypting key is missing now but can be (and will be) implemented at some point in time.
