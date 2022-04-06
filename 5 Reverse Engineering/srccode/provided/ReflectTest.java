import java.lang.reflect.*;

class ReflectTest
{
    public static void main(String [] args) throws Exception
    {
        Test t = new Test();
        // TestTest t = new TestTest();

        Class c = t.getClass();

        System.out.println("The name of the class is " + c.getName());

        Constructor con = c.getConstructor();
        System.out.println("The constructor is called " + con.getName());
    
        // gets public methods
        Method [] methods = c.getMethods();
        System.out.println();
        for (Method method : methods)
            System.out.println(method.getName());

        // gets private methods
        System.out.println();
        Method [] allmethods = c.getDeclaredMethods();
        for (Method method : allmethods)
            System.out.println(method.getName());

        System.out.println();

        // uses public method found in allmethods
        Method methodcall1 = c.getDeclaredMethod("method3", int.class);
        methodcall1.invoke(t, 3);

        System.out.println();

        // call private method found in allmethods
        Method methodcall2 = c.getDeclaredMethod("method2");
        methodcall2.setAccessible(true);
        methodcall2.invoke(t);
    }
}