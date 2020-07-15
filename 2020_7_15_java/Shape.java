public class Shape {
    double width = 0;  double height =0;
    Shape(double a, double b) {  
        width = a; height = b; 
    }

    double area() { 
        return width * height; 
    }
}