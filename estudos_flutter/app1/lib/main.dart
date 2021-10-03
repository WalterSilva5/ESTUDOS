import 'package:flutter/material.dart';
main(){
  runApp(
    MaterialApp(
      title: "contador de pessoas",
      home: Stack(children: <Widget>[
        Image.asset(
          "images/restaurant.jpg",
          fit: BoxFit.cover,
          height:1000.0,
        ),Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
        Text("Pessoas: 0",
        style: TextStyle(color: Colors.white,
        fontWeight: FontWeight.bold)),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FlatButton(
            child: Text("+1", style: TextStyle(fontSize: 40.0, color: Colors.white),),
            onPressed: (){print("teste");},),

            Padding(
              padding: EdgeInsets.all(30.0),
              child: FlatButton(
                child: Text("-1", style: TextStyle(fontSize: 40.0, color: Colors.white),),
                onPressed: (){print("teste");},),
            ),

           
          ],),
        Text("pode entrar",
        style: TextStyle(color: Colors.red,
        fontStyle: FontStyle.italic,
        fontSize: 30.0,
        )),
      ],)
      ],)
      ));
}