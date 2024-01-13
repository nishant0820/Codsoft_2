/*// inline function
#include<iostream>
using namespace std;
inline int add(int a,int b){
    return(a+b);
}
int main(){
    cout<<"Addition of a and b is "<<add(2,3);
    return 0;
}/*/

/*// single Inheritance
#include<iostream>
using namespace std;
class Employee{
    public:
    float salary=6000;
};
class Programmer: public Employee{
    public:
    float bonus=5000;
};
int main(){
    Programmer p1;
    p1.salary;
    p1.bonus;
}*/

/*// Multiple Inheritance
#include<iostream>
using namespace std;
class Employee{
    public:
    char name="nishant";
};
class Salary{
    public:
    float salary=3000;
};
class Bonus: public Employee: public Salary{
    public:
    flaot bonus=3000;
}
int main(){
    Bonus b1;
    b1.name;
    b1.salary;
    b1.bonus;
}*/

/*// Multilevel Inheritance
#include<iostream>
using namespace std;
class Employee{
    public:
    char name="Nishant";
};
class Salary: public Employee{
    public:
    float salary=2000;
}
class Bonus: public Salary{
    public:
    float bonus=900;
}
int main(){
    Bonus b1;
    b1.name;
    b1.salary;
    b1.bonus;
}*/

/*// Hybrid Inheritance
#include<iostream>
using namespace std;
class Employee{
    public:
    char name="Nishant";
}
class Salary: public Employee{
    public:
    float salary=9000;
}
class Bonus: public Employee{
    public:
    float bonus=800;
}
class Final: public Salary: public Bonus{
    public:
    char addresss="ABC";
}
int main(){
    Final f1;
    f1.name;
    f1.salary;
    f1.bonus;
    f1.address;
}*/

/*// Default Constructor
#include<iostream>
using namespace std;
class Employee{
    public:
    Employee(){
        cout<<"Default Constructor."<<endl;
    }
}
int main(){
    Employee e1;
}*/

/*// Parameterized Constructor
#include<iostream>
using namespace std;
class Employee{
    private:
    int salary;
    int bonus;
    public:
    Employee(int s,int b){
        salary=s;
        bonus=b;
    }
    void display(){
        cout<<id<<" "<<name<<" "<<salary<<" "<<endl;
    }
};
int main(){
    Employee e1=Employee(101,200);
    e1.display();
    return 0;
}*/

/*// Function Overloading
#include<iostream>
using namespace std;
class Add{
    public:
    static int add(int a,int b){
        return (a+b);
    }
    static int add(int a,int b,int c){
        return (a+b+c);
    }
};
int main(){
    Add a;
    cout<<a.add(1,2)<<endl;
    cout<<a.add(1,2,3)<<endl;
}*/

/*#include<iostream>
using namespace std;
class Mult{
    public:
    static int mul(int a,int b){
        return a*b;
    }
    static int mul(int a,int b, int c){
        return a*b*c;
    }
};
int main(){
    Mult m;
    cout<<m.mul(2,3)<<endl;
    cout<<m.mul(2,3,4)<<endl;
}*/

// Friend class and private access specifier
/*#include<iostream>
using namespace std;
class A{
    private:
    int a,int b;
    public:
    void show(){
        a=10;b=20;
        cout<<a<<b;
    }
    friend class B;
};
class B{
    public:
    void display(A obj){
        obj.a=30; obj.b=40;
        cout<<obj.a<<obj.b;
    }
};
int main(){
    A a1;
    a1.show();
    B b1;
    b1.display(a1);
}*/

/*// Protected access specifier
#include<iostream>
using namespace std;
class A{
    protected:
    int a,b;
    public:
    void show(){
        a=10; b=20;
        cout<<a<<b<<endl;
    }
};
class B: protected A{
    public:
    void display(){
        a=30;b=40;
        cout<<a<<b<<endl;
    }
};
int main(){
    B b1;
    b1.display();
}*/

// Structure
#include<iostream>
using namespace std;
struct Emp{
    string name;
    int salary;
};
int main(){
    struct Emp E;
    E.name="Nisha";
    E.salary=9000;
    cout<<sizeof(E.name)<<" bytes";
    
}