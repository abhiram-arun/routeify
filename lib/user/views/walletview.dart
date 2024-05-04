import 'package:flutter/material.dart';
import 'package:frontend/Auth/views/login.dart';

class WalletView extends StatelessWidget {
  const WalletView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(
                child: Text("  "),
              ),
              SizedBox(
                child: Text(
                  "Wallet Balance is:",
                  style: TextStyle(fontSize: 25.0),
                ),
                height: 30.0,
              ),
              SizedBox(
                child: Text(
                  " ₹ 500 ",
                  style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 100.0,
                      color: Color.fromARGB(255, 179, 8, 8)),
                ),
                height: 120.0,
              ),
              ElevatedButton(child: Text("RECHARGE WALLET"), onPressed: () {}),
            ]),
      ),
    );
  }
}
