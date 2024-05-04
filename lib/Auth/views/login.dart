import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:frontend/Admin/views/adminhome.dart';
import 'package:frontend/user/views/userhome.dart';

class Login extends StatelessWidget {
  const Login({super.key});

  @override
  Widget build(BuildContext context) {
    final _screenheight = MediaQuery.of(context).size.height;
    final _screenwidth = MediaQuery.of(context).size.width;
    return Scaffold(
      body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsets.only(bottom: 0.8),
                child: Text('kili',style: TextStyle(fontSize: 45,fontWeight: FontWeight.bold, color:Color.fromARGB(255, 179, 8, 8),),
                ),
              ),
              SizedBox(height: 20,),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: TextField(
                       decoration: InputDecoration(
                              filled: true,
                              prefixIcon: Icon(Icons.person_2),
                              fillColor: Color.fromARGB(255, 255, 248, 248),
                
                              // focusColor: AdvColors.loginfield,
                              // hoverColor: AdvColors.loginfield,
                              enabledBorder: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(35),
                                  borderSide: BorderSide(width: 0.1)),
                              focusedBorder: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(35),
                                  borderSide: BorderSide(width: 0.5)),
                              disabledBorder: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(35),
                              ),
                              hintText: "Username",
                       ),
                ),
              ),
              SizedBox(height: 10.0,),
                Padding(
                  padding: const EdgeInsets.all( 8.0),
                  child: TextField(
                              decoration: InputDecoration(
                                filled: true,
                                prefixIcon: Icon(Icons.key),
                                fillColor: Color.fromARGB(255, 255, 248, 248),
                    
                                // focusColor: AdvColors.loginfield,
                                // hoverColor: AdvColors.loginfield,
                                enabledBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(35),
                                    borderSide: BorderSide(width: 0.1)),
                                focusedBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(35),
                                    borderSide: BorderSide(width: 0.5)),
                                disabledBorder: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(35),
                                ),
                                hintText: "Password",
                              ),
                                  ),
                ),
                SizedBox(height: 10.0),
                ElevatedButton(
                  child: Text('LOGIN'),
                  onPressed: (){
                     Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => Userhome(),
                    ),
                  );
                  }), 
              TextButton(
                        child: Text("User",),
                        onPressed: ()
                          {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => Userhome(),
                    ),
                  );
                }),
              TextButton(
                        child: Text("Admin"),
                        onPressed: () {
                           Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => AdminHome(),
                    ),
                  );
                        }
              ),
            ],
          ),
        ),
      );
  }
}
