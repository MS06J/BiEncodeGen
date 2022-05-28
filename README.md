# Binary-Encoding-Pattern-Generator-for-3D-Structured-Light-Scanning
A simple program to generate black and white pattern for structured light scanning. You can use it in game engine or use with a projector.
The pattern is tested with Unity engine. In order to avoid light leak in the engine, transparent edges are added to four sides of the pattern. You can adjust the width by adjusting the side variable in the function, which is by default 1 pixel.
Size parameters of the function only refer to the pattern part, so the autual output will be slightly larger than the value assigned because of transparent edges.
Num parameter refer to number of line pair. If num=1, you will get 2 stripes,if num=2, you will get 4 stripes,3 for 8 stripes and so on. 
It is recommended the width do not differ to far from the original size, which is 1*power(2,num). Big sizing factor will make the edge of black and white stripes become gray.
