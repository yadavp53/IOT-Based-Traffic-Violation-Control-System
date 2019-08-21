
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX
float Amillis = millis();
String Status = "";
int v1 = 5000;
int v2 = 10000;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

pinMode(13, 1);
pinMode(8, 1);
pinMode(9, 1);
digitalWrite(13, 0);
digitalWrite(8, 0);
digitalWrite(9, 0);


  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}

void loop() { // run over and over
  if (mySerial.available()) {
    String num = mySerial.readString();
    Serial.println(num + "&" + Status);
    delay(100);
  }
int  nowMills = millis();
int  diff = nowMills - Amillis;
  if (diff > 0 and diff < v1)
      {
        digitalWrite(8, 0);
        digitalWrite(9, 1);
        Status = "Green&";
        }

      if (diff > v1 and diff < v2)
      {
        digitalWrite(8, 1);
        digitalWrite(9, 0);
        Status = "Red&";
        
        }
      if (diff > v2){
        Amillis = nowMills;
      }
  

}
