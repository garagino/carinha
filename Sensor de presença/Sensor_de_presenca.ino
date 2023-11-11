#include <Arduino.h>

#define PIN_PIR 2
#define PIN_LED 3

bool pir_state = false;
bool pir_last_state = false;
long pir_time = 0;
int people_count = 0;
long last_time = 0;

void motionDetected();
void noMotionDetected();
void printPeopleCount();

void setup() {
  pinMode(PIN_PIR, INPUT);
  pinMode(PIN_LED, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  pir_last_state = pir_state;
  pir_state = digitalRead(PIN_PIR);

  if (pir_state == true) {
    if (pir_last_state == false) {
      motionDetected();
    }
  }
  else {
    noMotionDetected();
  }

  if (millis() - last_time > 20000) {
    printPeopleCount();
    last_time = millis();
  }

  delay(100);
}

void motionDetected() {
  digitalWrite(PIN_LED, HIGH);
  people_count++;
  Serial.println("Movimentação detectada");
}

void noMotionDetected() {
  digitalWrite(PIN_LED, LOW);
  Serial.print("Nenhum movimento detectado");
}

void printPeopleCount() {
  Serial.print("Pessoas detectadas: ");
  Serial.println(people_count);
}


