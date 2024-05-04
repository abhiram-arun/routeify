import 'package:flutter/material.dart';
import 'package:frontend/Admin/views/adminhomeview.dart';
import 'package:frontend/Admin/views/adminuserview.dart';

class AdminHome extends StatefulWidget {
  const AdminHome({super.key});

  @override
  State<AdminHome> createState() => _AdminHomeState();
}

class _AdminHomeState extends State<AdminHome> {
  @override
  int currentIndex = 0;
  final screens = [
    AdminHomeView(),
    AdminUserView(),
  ];
  Widget build(BuildContext context) {
    return Scaffold(
      body: screens[currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        onTap: (index) => setState(() => {currentIndex = index}),
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.bus_alert), label: "Ticket"),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: "User"),
        ],
      ),
    );
  }
}
