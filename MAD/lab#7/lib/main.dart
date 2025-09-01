// ignore_for_file: use_key_in_widget_constructors

import 'package:flutter/material.dart';
import 'dart:async';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'APP',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color.fromARGB(255, 173, 58, 183),
        ),
        useMaterial3: true,
      ),
      home: Splashscreen(),
    );
  }
}

class Splashscreen extends StatefulWidget {
  const Splashscreen({super.key});

  @override
  State<Splashscreen> createState() => _SplashscreenState();
}

class _SplashscreenState extends State<Splashscreen> {
  @override
  void initState() {
    super.initState();
    Timer(Duration(seconds: 2), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => MainDrawerScreen()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: Colors.cyan,
        child: Center(
          child: Text(
            "Classico",
            style: TextStyle(
              fontSize: 34,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
        ),
      ),
    );
  }
}

class MainDrawerScreen extends StatelessWidget {
  const MainDrawerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('USER APP'),

        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            UserAccountsDrawerHeader(
              accountName: Text("AbdullahMohsin"),
              accountEmail: Text("abdullahmohsinune@gmail.com"),
              currentAccountPicture: CircleAvatar(
                backgroundImage: NetworkImage(
                  "data:image/png;base64,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", // Replace with your image URL
                ),
              ),
              decoration: BoxDecoration(
                color: const Color.fromARGB(255, 24, 100, 161),
              ),
            ),
            ListTile(
              title: Text('Home'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: Text('Settings'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SettingsScreen()),
                );
              },
            ),
            ListTile(
              title: Text('Material'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => materialScreen()),
                );
              },
            ),
          ],
        ),
      ),
      body: DefaultTabController(
        length: 3,
        child: Column(
          children: [
            TabBar(
              tabs: [
                Tab(icon: Icon(Icons.home), text: 'Home'),
                Tab(icon: Icon(Icons.settings), text: 'Settings'),
                Tab(icon: Icon(Icons.search), text: 'Material'),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  TabPage(title: 'Home'),
                  TabPage(title: 'Settings'),
                  TabPage(title: 'Material'),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class TabPage extends StatelessWidget {
  final String title;
  const TabPage({required this.title});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(height: 20),
          Container(
            height: 100,
            width: 100,
            color: const Color.fromARGB(255, 51, 231, 192),
            child: Center(child: Text('NAV-> $title')),
          ),
          Container(
            height: 100,
            width: 100,
            color: Colors.blue,
            child: Center(child: Text('R')),
          ),
          Container(
            height: 100,
            width: 100,
            color: const Color.fromARGB(255, 51, 255, 0),
            child: Center(child: Text('G')),
          ),
          Container(
            height: 100,
            width: 100,
            color: const Color.fromARGB(255, 26, 96, 228),
            child: Center(child: Text('B')),
          ),
        ],
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  final String title;
  const DetailScreen({required this.title});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Detail from $title'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Center(child: Text('This is the detail page from $title')),
    );
  }
}

// ignore: camel_case_types
class materialScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Material Page'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            height: 500,
            width: 500,
            color: Colors.red,
            child: Center(child: Text('Container 1')),
          ),
          SizedBox(height: 100),
          Container(
            height: 230,
            width: 400,
            color: Colors.green,
            child: Center(child: Text('Container 2')),
          ),
        ],
      ),
    );
  }
}

class SettingsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Settings'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Center(child: Text('Settings Page')),
    );
  }
}
