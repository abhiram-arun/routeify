import 'package:flutter/material.dart';

class Qrgen extends StatelessWidget {
  const Qrgen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
                    child: Padding(
                      padding: EdgeInsets. all(20.0),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Container(height: 200,width: 200,
                            child: SizedBox(child: Image.asset('assets/images/qrpic.jpg',))),
                          Padding(
                            padding: const EdgeInsets.all(20.0),
                            child: Text("Scan QR code to pay",style: TextStyle(fontWeight: FontWeight.bold,fontSize: 20,color: Color.fromARGB(255, 179, 8, 8),),),
                          ),
                        ],
                      ),
                    ),
        ),
      ),
    );
  }
}