import 'package:flutter/material.dart';
import 'package:frontend/user/views/homeview.dart';
import 'package:frontend/user/views/userview.dart';
import 'package:frontend/user/views/walletview.dart';

class Userhome extends StatefulWidget {
  const Userhome({super.key});

  @override
  State<Userhome> createState() => _UserhomeState();
}

class _UserhomeState extends State<Userhome> {
  int currentIndex = 0;
  final screens = [
    HomeView(),
    WalletView(),
    UserView(),
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: screens[currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        onTap: (index) => setState(() => {currentIndex = index}),
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(icon: Icon(Icons.wallet), label: "Wallet"),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: "User")
        ],
      ),
    );
  }
}
