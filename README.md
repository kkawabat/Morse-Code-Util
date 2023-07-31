# Morse Code Util

This is the business logic for my portfolio project on kankawabata.com/morse_code. Some of the code here were lifted out of my previous kivy implementation see [here](https://github.com/kkawabat/morse-code-kivy)

## usage
The `MorseEngine` class takes one parameter `tapping_speed`. tapping_speed determines the duration that the user needs to press to register as a dot/dash/short pause/long pause. The smaller the number the quicker the user will have to tap.



## signal encoding
The Morse Engine "signal" is a sequence of number and alternating "U"s and "D"s, such as the one seen below:

```
23U1D1U1D1U1D1U1D
```

There are two states when transmitting morse code the pressed and unpressed states. the number in the signal represents the number of frame (10ms increments) of the state and the U/D following after indicates the state (unpressed/pressed respectively)  

So for example in the above signal `23U` represents 23 frames (230ms) of the key not being pressed followed by 1 frame of the key being pressed (`1d`), etc.





