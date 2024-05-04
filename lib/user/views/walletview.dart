import 'package:flutter/material.dart';

class WalletView extends StatelessWidget {
  const WalletView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.center,
        children:[
          SizedBox(child: Text("  "),height: 100.0,),

          SizedBox(child: Text("Wallet Balance is:",style: TextStyle(fontSize: 25.0),),height: 100.0,),
          SizedBox(child: Text(" 500 ",style: TextStyle(fontWeight: FontWeight.bold,fontSize: 50.0),),height: 120.0,),
          ElevatedButton(child: Text("RECHARGE WALLET"), onPressed: () {}),
      ]
      ),
      );
  }
}
