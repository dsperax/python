## How to run:

I recomend use [replit](https://replit.com/) to run. It's easy, fast and simple.

run the code on Run buttom: 

![image](https://user-images.githubusercontent.com/76974801/121957812-4c305d00-cd39-11eb-8ba8-27e3bed09e90.png)

Call the function with a n number:

Attention: The higher the number of n, the longer the processing takes and the more accurate pi tends to be. Accuracy is not guaranteed as points are generated randomly.

```
estimate_pi(n)
```
## Explanation

![image](https://user-images.githubusercontent.com/76974801/121959244-e8a72f00-cd3a-11eb-9e44-1fd6e12cd935.png)

The area of the circle is given by Pi * r² and we use a circle with r = 1, then Pi = area of circle.

The pois is in circle if the distance from the point to the center of the circle <= r. Knowing this, the sum of the points inside circle (red dots) must be the value of pi if they fill the entire circle. Therefore, the more points, the greater the precision. Let's not forget that some dots will be outside (purple dots)

exemple:

![image](https://user-images.githubusercontent.com/76974801/121959868-b8ac5b80-cd3b-11eb-9541-23a978f0b25a.png)

Pi value = 3.14159265359

based on that, we have to:

![image](https://user-images.githubusercontent.com/76974801/121960384-6586d880-cd3c-11eb-9950-1e8c8e76ad02.png)

radius = 1, so...

![image](https://user-images.githubusercontent.com/76974801/121960491-8bac7880-cd3c-11eb-9d8e-f4694cf381d0.png)
