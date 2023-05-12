#define PIR = 2;
#define led = 3;

int estadoPIR = 0;

void setup() {
  pinMode(PIR, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  estadoPIR = digitalRead(PIR);
  if (estadoPIR == HIGH) {
    digitalWrite(led, HIGH);
    Serial.println("Movimentação detectada");
  } 
  else {
    digitalWrite(led, LOW);
    Serial.print("Nenhum movimento detectado");
  }
  delay(100);
}


