import 'package:flutter/material.dart';
import 'package:dropdown_search/dropdown_search.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  @override
  Widget build(BuildContext context) {
    final List<String> items = [
      'Karicode',
      'Kallumthazham',
      'RandamKutty',
      'Kadappakada',
      'Railway Station',
      'Chinnakada',
    ];
    String? selectedValue;
    final _screenheight = MediaQuery.of(context).size.height;
    final _screenwidth = MediaQuery.of(context).size.width;
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: _screenheight * 0.09,
          ),
          Padding(
            padding: EdgeInsets.only(left: _screenwidth * 0.05),
            child: Text(
              "Hello",
              style: TextStyle(
                  fontSize: _screenwidth * 0.07, fontWeight: FontWeight.bold),
            ),
          ),
          SizedBox(
            height: _screenheight * 0.05,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: DropdownSearch<String>(
              popupProps: PopupProps.menu(
                showSelectedItems: true,
                disabledItemFn: (String s) => s.startsWith('I'),
              ),
              items: items,
              dropdownDecoratorProps: DropDownDecoratorProps(
                dropdownSearchDecoration: InputDecoration(
                  labelText: "From",
                  hintText: "Starting Destination",
                ),
              ),
              onChanged: print,
            ),
          ),
          SizedBox(
            height: _screenheight * 0.01,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: DropdownSearch<String>(
              popupProps: PopupProps.menu(
                showSelectedItems: true,
                disabledItemFn: (String s) => s.startsWith('I'),
              ),
              items: items,
              dropdownDecoratorProps: DropDownDecoratorProps(
                dropdownSearchDecoration: InputDecoration(
                  labelText: "To",
                  hintText: "End Destination",
                ),
              ),
              onChanged: print,
            ),
          ),
        ],
      ),
    );
  }
}
