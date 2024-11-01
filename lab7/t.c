 #include <stdio.h>
 
 int a=7;
 int b=11;
 int c = 6;
 int main()
 {
    if(a > b)
    {
        if(a > c)
        {
            printf("%d", a);
        }
    }
    else
    {
        if (b > c)
        {
            printf("%d", b);;
        }
        else
        {
            printf("%d", c);
        }
        
    }
    return 0;
}