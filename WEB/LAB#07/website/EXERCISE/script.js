// Task 1
var username = "JohnDoe";
var age = 25;
document.writeln("Username: " + username);
document.writeln("Age: " + age);
document.writeln("<br>");

// Task 2
var num = 10; // You can change this value to test different cases
if (num > 0) {
    document.writeln("The number is positive.");
    document.writeln("<br>");
} else if (num < 0) {
    document.writeln("<br>");
    document.writeln("The number is negative.");
} else {
    document.writeln("<br>");
    document.writeln("The number is zero.");
}
document.writeln("<br>");
// Task 3
for (var i = 0; i <= 20; i++) {
    if (i % 2 === 0) {
        document.writeln("<br>");
        document.writeln(i);
    }
}

// Task 4
document.writeln("<br>");
var x = 1;
while (x <= 10) {
    document.writeln("<br>");
    document.writeln(x * 2);
    x++;
}
document.writeln("<br>");
// Task 5document.writeln("<br>");
var fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];
for (var j = 0; j < fruits.length; j++) {
    document.writeln("<br>");   
    document.writeln(fruits[j]);
}