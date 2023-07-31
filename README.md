# Morse Code Util

This is the business logic for my portfolio project on kankawabata.com/morse_code. Some of the code here were lifted out of my previous kivy implementation see [here](https://github.com/kkawabat/morse-code-kivy)

## signal encoding
The Morse Engine "signal" is a sequence of number and alternating "U"s and "D"s representing key not pressed state and keydown state respectively. The number represents the duration of the states in 10ms. 

So for example the signal:

```
23U1D1U1D1U1D1U1D
```

represents 230ms (23 * 10ms) of key not pressed, followed by 10ms of key pressed followed by 10ms of key released, etc.



