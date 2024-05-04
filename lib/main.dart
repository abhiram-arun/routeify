import 'package:flutter/material.dart';
import 'package:frontend/Auth/views/login.dart';
import 'package:frontend/user/views/userhome.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Kili',
      theme: ThemeData(
        colorScheme:
            ColorScheme.fromSeed(seedColor: Color.fromARGB(255, 179, 8, 8)),
        useMaterial3: true,
      ),
      home: const Userhome(),
    );
  }
}
